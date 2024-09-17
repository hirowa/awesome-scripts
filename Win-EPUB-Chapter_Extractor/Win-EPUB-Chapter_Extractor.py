import os
import fitz  # PyMuPDF
import csv
import shutil
import re
import sys

# Suppress stderr (CSS warnings) using context manager for cleaner control
class SuppressStderr:
    def __enter__(self):
        self.old_stderr = sys.stderr
        sys.stderr = open(os.devnull, 'w')

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stderr.close()
        sys.stderr = self.old_stderr

# Function to sanitize file names and ensure they are not longer than 100 characters
def sanitize_filename(filename, max_length=100):
    sanitized_name = re.sub(r'[<>:"/\\|?*]', '_', filename)
    if len(sanitized_name) > max_length:
        sanitized_name = sanitized_name[:max_length - 3] + "..."  # Truncate and add '...'
    return sanitized_name

# Function to extract chapters and subchapters from TOC with hierarchical numbering
def extract_chapters_from_toc(epub_file, epub_folder):
    chapters = []
    book_title = os.path.basename(epub_file).replace('.epub', '')  # Get book title from file name

    # Load the EPUB file
    try:
        with SuppressStderr():
            doc = fitz.open(epub_file)
    except Exception as e:
        print(f"Error opening {epub_file}: {e}")
        return []

    toc = doc.get_toc()  # Get Table of Contents (TOC)

    if not toc:
        print(f"No TOC found in {epub_file}.")
        return []

    chapter_numbering = {1: 0, 2: 0, 3: 0}
    current_root_chapter = ""  # To store the last seen level 1 chapter

    for i, entry in enumerate(toc):
        level, title, page_number = entry
        full_title = title.replace('\n', ' ').strip()

        if level == 1:
            chapter_numbering[1] += 1
            chapter_numbering[2] = 0
            chapter_numbering[3] = 0
            chapter_label = f"{chapter_numbering[1]}"
            current_root_chapter = full_title  # Update the root chapter
            chapter_path = current_root_chapter  # For level 1, path is just the root
        elif level == 2:
            chapter_numbering[2] += 1
            chapter_numbering[3] = 0
            chapter_label = f"{chapter_numbering[1]}.{chapter_numbering[2]}"
            chapter_path = f"{current_root_chapter} -> {full_title}"  # Level 2 has root -> current chapter
        elif level == 3:
            chapter_numbering[3] += 1
            chapter_label = f"{chapter_numbering[1]}.{chapter_numbering[2]}.{chapter_numbering[3]}"
            chapter_path = f"{current_root_chapter} -> {toc[i-1][1].strip()} -> {full_title}"  # Level 3 has root -> parent -> current
        else:
            continue

        # Extract the text for the chapter using the chapter titles as boundaries
        chapter_text = extract_chapter_text(doc, toc, i)

        # Sanitize the file name
        sanitized_title = sanitize_filename(full_title)
        chapter_file_name = f"{chapter_label}_{sanitized_title}.txt"
        chapter_file_path = os.path.join(epub_folder, chapter_file_name)

        # Write the chapter content to a .txt file in the specified format
        with open(chapter_file_path, 'w', encoding='utf-8') as chapter_file:
            chapter_file.write(f"Book: {book_title}\n")
            chapter_file.write(f"Chapter #: {chapter_label}\n")
            chapter_file.write(f"Chapter Path: {chapter_path}\n")
            chapter_file.write(f"Content:\n{chapter_text}\n")

        # Count words in the chapter text
        word_count = count_words(chapter_text)

        # Append chapter data to the list
        chapters.append({
            'chapter_number': chapter_label,
            'chapter_title': full_title,
            'page_number': page_number,
            'word_count': word_count
        })

        print(f"Extracted chapter: {chapter_label} - {full_title} (Level: {level}, Page: {page_number}, Word Count: {word_count})")

    return chapters

# Function to extract text for a specific chapter using titles as boundaries
def extract_chapter_text(doc, toc, index):
    chapter_text = ""
    _, current_title, start_page = toc[index]
    next_title = toc[index + 1][1] if index + 1 < len(toc) else None  # Get the next chapter's title if it exists
    end_page = toc[index + 1][2] if index + 1 < len(toc) else len(doc)  # Until next chapter or end of document

    # Loop through the pages from start_page to end_page (inclusive)
    for page_num in range(start_page - 1, end_page):
        try:
            page = doc.load_page(page_num)
            page_text = page.get_text("text")

            # If we encounter the next chapter's title in the current page's text, stop appending
            if next_title and next_title in page_text:
                # Cut off the text at the point where the next chapter's title starts
                chapter_text += page_text.split(next_title)[0]
                break
            else:
                chapter_text += page_text

        except Exception as e:
            print(f"Error reading page {page_num}: {e}")
            continue

    # To prevent overflow from previous chapter, remove current title from the beginning if present
    if current_title in chapter_text:
        chapter_text = chapter_text.split(current_title, 1)[-1].strip()

    return chapter_text




# Function to count words in a given text
def count_words(text):
    words = text.split()
    return len(words)

# Function to process each EPUB file and write chapters with hierarchical numbering and word count to a CSV file
def process_epub_file(epub_file):
    epub_folder_name = sanitize_filename(os.path.splitext(epub_file)[0])
    epub_folder = sanitize_filename(epub_folder_name, 100)
    
    if not os.path.exists(epub_folder):
        os.mkdir(epub_folder)
    
    shutil.move(epub_file, os.path.join(epub_folder, epub_file))

    chapters = extract_chapters_from_toc(os.path.join(epub_folder, epub_file), epub_folder)

    if not chapters:
        return
    
    csv_file_name = sanitize_filename(os.path.splitext(epub_file)[0], 70) + "_chapters_info.csv"
    csv_file_path = os.path.join(epub_folder, csv_file_name)
    
    with open(csv_file_path, mode="w", newline="", encoding="utf-8") as csv_file:
        fieldnames = ['chapter_number', 'chapter_title', 'page_number', 'word_count']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        
        writer.writeheader()
        
        for chapter in chapters:
            writer.writerow({
                'chapter_number': chapter['chapter_number'],
                'chapter_title': chapter['chapter_title'],
                'page_number': chapter['page_number'],
                'word_count': chapter['word_count']
            })
    
    print(f"Chapters from {epub_file} saved to {csv_file_path}")

# Function to process all EPUB files in the current directory
def process_epubs_in_directory():
    epub_files = [f for f in os.listdir() if f.endswith(".epub")]
    for epub_file in epub_files:
        print(f"Processing {epub_file}...")
        process_epub_file(epub_file)

# Run the script
if __name__ == "__main__":
    process_epubs_in_directory()

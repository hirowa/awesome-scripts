import sys
import os
from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file using PyPDF2."""
    text = ""
    try:
        reader = PdfReader(pdf_path)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    except Exception as e:
        print(f"Error processing {pdf_path}: {e}")
    return text

def read_file(file_path):
    """Read file content based on file type."""
    ext = os.path.splitext(file_path)[1].lower()
    if ext == '.pdf':
        return extract_text_from_pdf(file_path)
    elif ext in ('.txt', '.md'):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            return ""
    else:
        print(f"Unsupported file format: {file_path}")
        return ""

def merge_files(file_paths, output_path):
    """Merge multiple files into one output file with separators and filenames."""
    try:
        with open(output_path, 'w', encoding='utf-8') as outfile:
            for file_path in file_paths:
                if not os.path.exists(file_path):
                    print(f"File does not exist: {file_path}")
                    continue

                content = read_file(file_path)
                header = f"----- {os.path.basename(file_path)} -----\n"
                outfile.write(header)
                outfile.write(content)
                outfile.write("\n\n")
        print(f"Merged file saved as {output_path}")
    except Exception as e:
        print(f"Error writing output file: {e}")

def get_file_paths():
    """
    Prompt the user to input file paths by dragging and dropping them into the terminal.
    The user should separate each file path by a space.
    """
    file_input = input("Drag and drop your files here (separated by space) and press Enter:\n")
    # Split by quotes if present, otherwise split on whitespace.
    # This approach handles cases when paths have spaces.
    if '"' in file_input:
        # Split using quotes, ignoring empty parts
        file_paths = [p.strip() for p in file_input.split('"') if p.strip() and p.strip() != ' ']
    else:
        file_paths = file_input.split()
    return file_paths

if __name__ == "__main__":
    if len(sys.argv) > 2:
        # First argument is output file, remaining are input files.
        output_file = sys.argv[1]
        input_files = sys.argv[2:]
    else:
        # Prompt user for file paths
        output_file = input("Enter output filename (e.g., merged.txt): ").strip()
        input_files = get_file_paths()
    
    if not output_file.lower().endswith('.txt'):
        output_file += '.txt'
    
    merge_files(input_files, output_file)

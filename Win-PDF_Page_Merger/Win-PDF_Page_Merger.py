import os
import fitz  # PyMuPDF

# Get the current working directory
working_directory = os.getcwd()

# Iterate over all files in the directory
for filename in os.listdir(working_directory):
    if filename.endswith('.pdf'):
        # Open the original PDF
        original_pdf = fitz.open(filename)

        # Create a new empty PDF
        new_pdf = fitz.open()

        # Create a new page in the new PDF with the combined dimensions of all original pages
        combined_width = max(page.rect.width for page in original_pdf)
        combined_height = sum(page.rect.height for page in original_pdf)
        new_page = new_pdf.new_page(width=combined_width, height=combined_height)

        # Set the initial y-offset to 0
        y_offset = 0

        # Iterate over all pages of the original PDF
        for page_num in range(original_pdf.page_count):
            page = original_pdf.load_page(page_num)  # Load the page
            rect = page.rect  # Get the dimensions of the page

            # Insert the page into the new page at the correct offset
            new_page.show_pdf_page(fitz.Rect(0, y_offset, rect.width, y_offset + rect.height), original_pdf, page_num)

            # Update the y_offset for the next page
            y_offset += rect.height

        # Save the new merged PDF with '_merged' suffix
        new_filename = os.path.splitext(filename)[0] + '_merged.pdf'
        new_pdf.save(new_filename)
        new_pdf.close()
        original_pdf.close()

print("All PDFs have been merged into a single page per file.")

import os
import subprocess
from pypdf import PdfReader, PdfWriter

def crop_pdf(input_pdf, output_pdf, first_page_crops, other_pages_crops):
    # Load the PDF
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    # Define crop parameters
    first_page_top, first_page_right, first_page_bottom = first_page_crops
    other_pages_top, other_pages_right, other_pages_bottom = other_pages_crops

    # Loop through all the pages
    for page_num, page in enumerate(reader.pages):
        # Get the current page media box (page size and position)
        media_box = page.mediabox

        if page_num == 0:
            # Crop the first page (top, right, and bottom)
            media_box.lower_left = (media_box.lower_left[0], media_box.lower_left[1] + first_page_bottom)
            media_box.upper_right = (media_box.upper_right[0] - first_page_right, media_box.upper_right[1] - first_page_top)
        else:
            # Crop the rest of the pages (top, right, and bottom)
            media_box.lower_left = (media_box.lower_left[0], media_box.lower_left[1] + other_pages_bottom)
            media_box.upper_right = (media_box.upper_right[0] - other_pages_right, media_box.upper_right[1] - other_pages_top)

        # Add the cropped page to the writer
        writer.add_page(page)

    # Save the cropped PDF to a temporary file
    temp_pdf = output_pdf.replace("_processed", "_temp")
    with open(temp_pdf, "wb") as temp_file:
        writer.write(temp_file)

    # Use QPDF to eliminate hidden content and produce the final output
    qpdf_command = [
        "qpdf", "--linearize", temp_pdf, output_pdf
    ]
    subprocess.run(qpdf_command)

    # Remove the temporary file
    os.remove(temp_pdf)


def process_pdfs_in_directory():
    # Find all PDF files in the working directory
    for filename in os.listdir():
        if filename.endswith(".pdf"):
            input_pdf = filename
            output_pdf = filename.replace(".pdf", "_processed.pdf")

            # Set the crop values for the first page and other pages
            first_page_crops = (482, 146, 165.82)  # Crop top, right (only), and bottom for first page
            other_pages_crops = (150, 146, 32.31)  # Crop top, right (only), and bottom for other pages

            print(f"Processing {input_pdf}...")
            crop_pdf(input_pdf, output_pdf, first_page_crops, other_pages_crops)
            print(f"Saved cropped PDF as {output_pdf}")


if __name__ == "__main__":
    process_pdfs_in_directory()

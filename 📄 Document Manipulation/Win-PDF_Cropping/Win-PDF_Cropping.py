import fitz  # PyMuPDF
import os

def crop_pdf_at_label(pdf_path, label="Total de Movimientos"):
    # Open the PDF file
    doc = fitz.open(pdf_path)
    label_found = False

    # Start checking from the last page and move backward
    for page_num in range(len(doc) - 1, -1, -1):
        page = doc.load_page(page_num)
        text = page.get_text("text")
        
        # Look for the label in the text
        if label in text:
            label_found = True
            # Find the rectangle where the label is located
            blocks = page.get_text("blocks")
            for block in blocks:
                if label in block[4]:
                    label_y_position = block[1]  # Y-coordinate of the top of the block containing the label
                    print(f'Label found on page {page_num + 1} at Y-coordinate: {label_y_position}')
                    
                    # Crop everything including and below the label
                    rect = page.rect
                    new_rect = fitz.Rect(rect.x0, rect.y0, rect.x1, label_y_position)
                    page.set_cropbox(new_rect)
                    
            break

    if label_found:
        # Save the cropped PDF
        output_path = pdf_path.replace('.pdf', '_cropped.pdf')
        doc.save(output_path)
        print(f'Cropped PDF saved as: {output_path}')
    else:
        print(f"Label '{label}' not found in {pdf_path}. No cropping done.")
    
    doc.close()

def crop_pdfs_in_directory(directory="."):
    # Iterate through all PDF files in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(directory, filename)
            print(f"Processing {pdf_path}...")
            crop_pdf_at_label(pdf_path)

# Call the function to crop PDFs in the current directory
if __name__ == "__main__":
    crop_pdfs_in_directory()

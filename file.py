from pdf2image import convert_from_path
import os

pdf_folder = "pdfs"
output_folder = "pdfs/thumbnails"
os.makedirs(output_folder, exist_ok=True)

for file in os.listdir(pdf_folder):
    if file.endswith(".pdf"):
        pdf_path = os.path.join(pdf_folder, file)
        pages = convert_from_path(pdf_path, first_page=1, last_page=1)

        name = file.replace(".pdf", ".png")
        pages[0].save(os.path.join(output_folder, name), "PNG")
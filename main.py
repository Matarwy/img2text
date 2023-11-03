from PIL import Image
import pytesseract
from os import path
from docx import Document

# Create a new Word document
doc = Document()
for i in range(1, 31):
    filepath = path.relpath(f'img/{i}.jpg')
    # Open the image
    image = Image.open(filepath)

    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    # Use pytesseract to extract text from the image
    text = pytesseract.image_to_string(image)

    # Add the extracted text to the Word document
    doc.add_paragraph(text)

# Save the Word document
doc.save('output.docx')


from PIL import Image
import pytesseract
from os import path
for i in range(1, 31):
    filepath = path.relpath(f'img/{i}.jpg')
    image = Image.open(filepath)
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    text = pytesseract.image_to_string(image)
    with open(f'txt/{i}.txt', 'w') as file:
        file.write(text)


import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Tanveer\AppData\Local\Tesseract-OCR\tesseract.exe'
img = Image.open('text.png')
output = pytesseract.image_to_string(img)

print(output)
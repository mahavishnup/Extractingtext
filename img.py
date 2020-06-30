import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
str = (pytesseract.image_to_string(r'1.png'))
with open('img.txt', 'w') as f:
    f.write(str)
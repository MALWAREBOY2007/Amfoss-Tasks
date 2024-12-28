from PIL import Image, ImageEnhance, ImageFilter
import pytesseract

image=Image.open("check.png")

image=image.convert("L")

enhancing_image=ImageEnhance.Contrast(image)

image=enhancing_image.enhance(2)

ext_text=pytesseract.image_to_string(image).strip()
try:
    result=eval(ext_text)
    print(result)
except Exception as e:
    print(e)

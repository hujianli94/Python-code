from PIL import Image
from pyocr import tesseract
# 使用PIL打开图片
im = Image.open('pic.png')
# OCR识别
code = tesseract.image_to_string(im)
print(code)

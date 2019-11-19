from PIL import Image
from pyocr import tesseract

pic_list = ['pic1.png','pic2.png']
for i in pic_list:
    im = Image.open(i)
    im = im.convert('L')# 图片转换为灰色图像
    # 保存转换后的图片
    im.save("temp.png")
    code = tesseract.image_to_string(im)
    print(code)

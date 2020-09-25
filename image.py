from PIL import Image
import pytesseract
import cv2


# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = r'/usr/local/Cellar/tesseract/4.1.1/bin/tesseract'
tessdata_dir_config = r'--tessdata-dir "/usr/local/Cellar/tesseract-lang/4.0.0/share/tessdata"'

# # Converts image grayscale
# im_gray = cv2.imread('Screen Shot 2020-07-20 at 11.43.33 AM.png', cv2.IMREAD_GRAYSCALE)
# (thresh, im_bw) = cv2.threshold(im_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
# thresh = 127
# im_bw = cv2.threshold(im_gray, thresh, 255, cv2.THRESH_BINARY)[1]
#
#
# cv2.imwrite('product.png', im_bw)
#
# # Simple image to string
# print("First Test ...")
# print(pytesseract.image_to_string(Image.open('malayalamtext.png'), lang='mal'))
print("Second Test...")
# print(pytesseract.image_to_string(Image.open('product.png'), lang='mal', config=tessdata_dir_config))
print("Third Test")
print(pytesseract.image_to_string(Image.open('image_trial.png'), lang='mal', config=tessdata_dir_config))
print("Over")

def starttest(im):
    text = pytesseract.image_to_string(Image.open(im), lang='mal', config=tessdata_dir_config)
    print(text)
    return text

# im = Image.open('screenshot.png')
# width, height = im.size
# print(im.size)
# for x in range(width):
#     for y in range(height):
#         val = im.getpixel((x, y))
#         print(val)






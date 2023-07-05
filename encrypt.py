from LSBSteg import *

steg = LSBSteg(cv2.imread("image.jpg"))
img_encoded = steg.encode_text("my message")
cv2.imwrite("my_new_image.png", img_encoded)
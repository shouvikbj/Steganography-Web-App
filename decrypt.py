from LSBSteg import *
import os

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

im = cv2.imread(f"{APP_ROOT}/static/new_image.png")
steg = LSBSteg(im)
print("Text value:",steg.decode_text())
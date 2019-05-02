import cv2
from matplotlib import pyplot as plt 
from PIL import Image
import pytesseract
import editdistance
import os
from math import inf
import sys


def main():
	img = cv2.imread(sys.argv[1])
	img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	imq = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,33,9)
	# imq = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

	f2 = "{}.png".format(os.getpid())
	cv2.imwrite(f2, imq)

	text = pytesseract.image_to_string(Image.open(f2))
	os.remove(f2)

	print(text)

	plt.imshow(imq)
	plt.show()
if __name__ == "__main__":
	main()
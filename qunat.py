import cv2
from matplotlib import pyplot as plt 

def main():
	img = cv2.imread('37.jpg')
	img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	imq = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,3)
	plt.imshow(imq)
	plt.show()
if __name__ == "__main__":
	main()
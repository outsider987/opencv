import numpy as np
import cv2
# here is api for opencv cv2.IMREAD_GRAYSCALE
img = cv2.imread("test.jpg")
cv2.namedWindow("Image")
cv2.imshow("Image", img)
cv2.waitKey (0)
img.relase()
cv2.destroyAllWindows()

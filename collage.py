import cv2
import numpy as np

sun = cv2.imread('pic.jpg')
earth = cv2.imread('earth.jpg')
cv2.imshow('pic1',sun)
cv2.imshow('pic2',earth)
cv2.waitKey()
cv2.destroyAllWindows()

sun.shape
earth.shape

sun = sun[10:600, 30:700]
cv2.imshow('sun',sun)
cv2.waitKey()
cv2.destroyAllWindows()

earth = earth[10:600, 30:700]
cv2.imshow('earth',earth)
cv2.waitKey()
cv2.destroyAllWindows()

#Collage
pic = np.hstack((sun,earth))
cv2.imshow('sun_earth',pic)
cv2.waitKey()
cv2.destroyAllWindows()

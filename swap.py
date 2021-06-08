import cv2
import numpy as np

mama = cv2.imread('mama.jpg')
papa = cv2.imread('papa.jpg')
cv2.imshow('pic1',mama)
cv2.imshow('pic2',papa)
cv2.waitKey()
cv2.destroyAllWindows()

mama.shape
papa.shape

px1,px2,px3,px4 = 50,600,200,700
mx1,mx2,my1,my2 = 50,600,200,700
papa_face = papa[px1:px2,px3:px4]
mama_face = mama[mx1:mx2,my1:my2]
cv2.imshow('pic1',mama_face)
cv2.imshow('pic2',papa_face)
cv2.waitKey()
cv2.destroyAllWindows()

papa = cv2.imread('papa.jpg')
papa[px1:px2,px3:px4] = mama_face
mama = cv2.imread('mama.jpg')
mama[mx1:mx2,my1:my2] = papa_face

#photo after swapping
cv2.imshow('pic1',mama)
cv2.imshow('pic2',papa)
cv2.waitKey()
cv2.destroyAllWindows()

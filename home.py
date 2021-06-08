import cv2
import numpy as np

image = np.zeros((600,1200,3))

fontScale = 2
Titlepos = (400,50)
Title = "SWEET HOME"
font = cv2.FONT_HERSHEY_SIMPLEX
color = (0,0,255)
thickness = 4
image = cv2.putText(image, Title, Titlepos, font, fontScale, color, thickness, cv2.LINE_AA, False)

cv2.rectangle(image,(200,300),(1000,600),[0,255,0],2)
cv2.line(image,(200,300),(300,100),[0,255,0],2)
cv2.line(image,(400,300),(300,100),[0,255,0],2)
cv2.line(image,(400,300),(400,600),[0,255,0],2)
cv2.line(image,(900,100),(300,100),[0,255,0],2)
cv2.line(image,(900,100),(1000,300),[0,255,0],2)
cv2.line(image,(250,400),(350,400),[0,255,0],2)
cv2.line(image,(250,400),(250,600),[0,255,0],2)
cv2.line(image,(350,400),(350,600),[0,255,0],2)
cv2.line(image,(250,400),(300,450),[0,255,0],2)
cv2.line(image,(300,450),(350,400),[0,255,0],2)
cv2.line(image,(300,450),(300,600),[0,255,0],2)
cv2.rectangle(image,(600,350),(800,450),[0,255,0],2)
cv2.line(image,(650,350),(650,450),[0,255,0],2)
cv2.line(image,(700,350),(700,450),[0,255,0],2)
cv2.line(image,(750,350),(750,450),[0,255,0],2)
cv2.circle(image,(300,200),30,[0,255,0],2)

#pic of a Home
cv2.imshow("hi", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

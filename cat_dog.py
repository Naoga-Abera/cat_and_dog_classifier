import cv2

font = cv2.FONT_HERSHEY_DUPLEX
font_color = (0, 255, 0)
thickness = 2
font_scale = 1

#The path of the picture
img=cv2.imread('sheep13.png')
#haarcascade Classifier for Dog
sheep_cascade=cv2.CascadeClassifier('sheep.xml')
#conversion of picture to gray
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#search for the object you want in the photos
find_sheep = sheep_cascade.detectMultiScale(gray, 1.9, 15)
if len(find_sheep) > 0:
    print("This is Sheep")
else:
    print("This is Goat")
cv2.imshow('result', img)
cv2.waitKey(0)

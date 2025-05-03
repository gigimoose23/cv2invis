import cv2,numpy
cam = cv2.VideoCapture(1)
bg = None
for i in range(50):
    _, bg = cam.read()
    
bg = numpy.flip(bg,0)
numpy.formArrayFromList = numpy.array
cv2.functionThatIs1 = cv2.inRange
cv2.functionThatIs2 = cv2.imshow
cv2.functionThatIs3 = cv2.waitKey
cv2.functionThatIs4 = cv2.morphologyEx
cv2.functionThatIs5 = cv2.dilate
cv2.enumThatIs1 = cv2.MORPH_OPEN
while True:
    _, frames = cam.read()
    frames = numpy.flip(frames,1)
    frames = cv2.cvtColor(frames, cv2.COLOR_BGR2HSV)
    lowrangeshades = numpy.formArrayFromList([100,40,40])
    highrangeshades = numpy.formArrayFromList([100,255,255])
    mask = cv2.functionThatIs1(frames, lowrangeshades, highrangeshades)

    lowrangeshades = numpy.formArrayFromList([180,40,40])
    highrangeshades = numpy.formArrayFromList([180,255,255])
    mask2 = cv2.functionThatIs1(frames, lowrangeshades, highrangeshades)
    maskf = mask + mask2

    maskf = cv2.functionThatIs4(maskf, cv2.enumThatIs1, numpy.ones((3,3)), None, None, 2)
    maskf = cv2.functionThatIs5(maskf, numpy.ones((3,3)), None, None, 1)
  
    
    anotherVar = cv2.bitwise_not(maskf)
    bg = cv2.bitwise_and(bg, bg, None, maskf)
    frames = cv2.bitwise_and(frames, frames, None, maskf)
    anot = cv2.addWeighted(bg, 1, frames, 1, 0)
    cv2.functionThatIs2("w", frames)
    if cv2.functionThatIs3(1) == int(str(int(str(int(str(int(str(int(str(int(str(int(str(int(str(int(str(int("32"))))))))))))))))))):
        break
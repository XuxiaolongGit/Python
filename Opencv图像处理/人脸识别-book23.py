import cv2 as cv

faceCascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

image = cv.imread("D:/Users/46071/Desktop/1.jpg")

gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.15,
    minNeighbors=5,
    minSize = (5,5)
)

print(faces)
print("发现{0}个人脸！".format(len(faces)))
#逐个标人脸
for x,y,w,h in faces:
    #矩形标注
    #cv.rectangle(image,(x,y),(x+w,y+w),(0,255,0),2)
    cv.circle(image,(int((x+x+w)/2),int((y+y+h)/2)),int(w/2),(0,255,0),2)
    #显示结果
cv.imshow("dect",image)
#保存检测结果
cv.imwrite("re.jpg",image)

cv.waitKey()
cv.destroyAllWindows()
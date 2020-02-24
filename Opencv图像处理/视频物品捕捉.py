import cv2 as cv
import numpy as np

def extrace_object_demo():
    #下面的函数中填 视频的路径或者 0(摄像头)
    capture = cv.VideoCapture()
    while(True):
        ret,frame = capture.read()
        if ret == False:
            break
        hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
        # 绿色的物体色彩范围 对照RGB转HSV对比图
        lower_hsv=np.array([37,43,46])
        upper_hsv = np.array([77,255,255])

        mask = cv.inRange(hsv,lowerb=lower_hsv,upperb=upper_hsv)
        #还原捕捉的色彩，否则是白色
        dst = cv.bitwise_and(frame,frame,mask = mask)
        cv.imshow("video",frame)
        cv.imshow("mask",mask)
        cv.imshow("带色彩mask",dst)
        c = cv.waitKey(40)
        if c == 27:
            break
src = cv.imread("D:/Users/46071/Desktop/1.jpg")
#通道分离与合并
# b,g,r = cv.split(src)
# cv.imshow("bule",b)
# cv.imshow("green",g)
# cv.imshow("red",r)
#通道合并
# src = cv.merge([b,g,r])
def image_catch(image):

    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    # 绿色的物体色彩范围 对照RGB转HSV对比图
    lower_hsv = np.array([0, 0, 0])
    upper_hsv = np.array([180, 255, 46])

    mask = cv.inRange(hsv, lowerb=lower_hsv, upperb=upper_hsv)
    cv.imshow("original", image)
    cv.imshow("mask", mask)

image_catch(src)
#cv.imshow("test",src)
#cv.namedWindow("test",cv.WINDOW_AUTOSIZE)

cv.waitKey()

cv.destroyAllWindows()
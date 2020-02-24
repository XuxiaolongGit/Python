import cv2 as cv
import numpy as np
#同大小图片的四则运算
def add_demo(m1,m2):
    dst = cv.add(m1,m2)
    cv.imshow("add_demo",dst)


def subtract_demo(m1,m2):
    dst = cv.subtract(m1,m2)
    cv.imshow("subtract_demo",dst)


def divide_demo(m1,m2):
    dst = cv.divide(m1,m2)
    cv.imshow("divide_demo",dst)


def multiply_demo(m1,m2):
    dst = cv.multiply(m1,m2)
    cv.imshow("multiply_demo",dst)
#
def others(m1):
    #图片的像素均值
    average = cv.mean(m1)
    #图片的均值和方差
    M1,dev1 = cv.meanStdDev(m1)
    print(M1,dev1)
    h,w = m1.shape[:2]
    img = np.zeros([h,w],np.uint8)
    m,dev = cv.meanStdDev(img)
    print(m,dev)
print("---------Hello Python+Opencv -----------")
src = cv.imread("D:/Users/46071/Desktop/1.jpg")
cv.namedWindow("input image",cv.WINDOW_FREERATIO)

cv.imshow("input image",src)
others(src)
cv.waitKey(0)
cv.destroyAllWindows()
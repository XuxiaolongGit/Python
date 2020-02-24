import cv2 as cv
import numpy as np
'''
模糊操作
均值模糊，中值模糊，自定义模糊，原理是数学卷积
1.基于离散卷积
2.定义好每个卷积核
3.不同卷积得到不同的卷积效果
4.模糊是卷积的一种表象
'''
#均值模糊
def blur_demo(image):
    #元组是 水平方向，垂直方向模糊程度
    dst = cv.blur(image,(1,3))
    cv.imshow("blur_demo",dst)
#中值模糊 对椒盐噪声 有很好的效果
def median_blur_demo(image):
    dst = cv.medianBlur(image,5)
    cv.imshow("median_blur_demo",image)
#自定义模糊
def custom_blur_demo(image):
    kernel = np.ones([5,5],np.float32)/25
    dst = cv.filter2D(image,-1,kernel=kernel)
    # dst =cv.medianBlur(image,5)
    cv.imshow("custom_blur_demo",5)
#锐化
def custom_blur_shapen(image):
    kernel = np.array([[0-1,0],[-1,5,-1],[0,-1,0]],np.float32)
    dst = cv.filter2D(image,-1,kernel=kernel)
    cv.imshow("custom_blur_shapen",dst)
print("---------Hello Python+Opencv -----------")
src = cv.imread("D:/Users/46071/Desktop/2.png")
cv.namedWindow("input image",cv.WINDOW_FREERATIO)

cv.imshow("input image",src)
cv.waitKey(0)
cv.destroyAllWindows()
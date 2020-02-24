import cv2 as cv
import numpy as np

#泛洪填充
def fill_color_demo(image):
    copyImg = image.copy()
    h,w = image.shape[:2]
    mask = np.zeros([h+2,w+2],np.uint8)
    #第一个元组 起始像素点
    #第二个元组 填充的颜色BGR
    #第三组 第四组  填充的像素范围
    cv.floodFill(copyImg,mask,(30,30),(0,255,255),(100,100,100),(50,50,50),cv.FLOODFILL_FIXED_RANGE)
    cv.imshow("fill_color_demo",copyImg)


#二值填充
def fill_binary(image):
    image = np.zeros([400,400,3],np.uint8)
    image[100:300,100:300,:]=255
    cv.imshow("fill_binary",image)

    mask = np.ones([402,402,1],np.uint8)
    mask[101:301,101:301] = 0
    cv.floodFill(image,mask,(200,200),(0,0,255),cv.FLOODFILL_MASK_ONLY)
    cv.imshow("filled binary",image)

#ROI即选择区域
print("---------Hello Python+Opencv -----------")
src = cv.imread("D:/Users/46071/Desktop/2.png")
cv.namedWindow("input image",cv.WINDOW_FREERATIO)

cv.imshow("input image",src)
#面部区域的范围
face = src[50:250,100:300]
gray = cv.cvtColor(face,cv.COLOR_BGR2GRAY)
backface = cv.cvtColor(gray,cv.COLOR_GRAY2BGR)
src[50:250,100:300] = backface
cv.imshow("face",src)
cv.waitKey(0)
cv.destroyAllWindows()
import cv2 as cv
import numpy as np

def logic_demo(m1,m2):
    #逻辑与
    dst = cv.bitwise_and(m1,m2)
    #取反
    dst2 = cv.bitwise_not(m1,m2)
    #逻辑或
    dst3 = cv.bitwise_or(m1,m2)
    #异或
    dst3 = cv.bitwise_xor(m1,m2)

# 对比度亮度调节
def contrast_brightness_demo(image,c,b):
    h,w,ch= image.shape
    blank = np.zeros([h,w,ch],image.dtype)
    dst = cv.addWeighted(image,c,blank,1-c,b)
    cv.imshow("adjust-contrast-brightness",image)



print("---------Hello Python+Opencv -----------")
src = cv.imread("D:/Users/46071/Desktop/1.jpg")
cv.namedWindow("input image",cv.WINDOW_FREERATIO)

contrast_brightness_demo(src,1.5,50)
cv.imshow("input image",src)
cv.waitKey(0)
cv.destroyAllWindows()
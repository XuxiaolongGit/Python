import cv2 as cv

#cv.bitwise_not()
'''像素取反'''
#cv.getTickCount()   cv.getTickFrequency()
'''获得时间戳，一般会调用两次，
然后(t2-t1)/cv.getTickFrequency()计算中间过程时间'''

#以下函数展示了同一图片在不同色彩空间的样子
#其中调用了色彩空间转换的API
def color_space_demo(image):
    gray = cv.cvtColor(image,cv.COLOR_BAYER_BG2GRAY)
    cv.imshow("gray",gray)
    hsv = cv.cvtColor(image,cv.COLOR_BGR2HSV)
    cv.imshow("hsv",hsv)
    yuv = cv.cvtColor(image,cv.COLOR_BGR2YUV)
    cv.imshow("yuv",yuv)
    Ycrcb =cv.cvtColor(image,cv.COLOR_BGR2YCrCb)
    cv.imshow("Ycrcb",Ycrcb)


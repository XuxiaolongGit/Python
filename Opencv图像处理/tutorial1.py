import cv2 as cv
import numpy as np
def video_demo():
    # 0默认为第一个是摄像头，也可以填 视频路径（无声音）
    captrue = cv.VideoCapture(0)
    while(True):
        ret,frame=captrue.read()
        #摄像头正过来
        frame =cv.flip(frame,1)
        cv.imshow("video",frame)
        c=cv.waitKey(50)
        if c==27:
            break
def getImageInfo(image):
    print(type(image))
    print(image.shape)
    print(image.size)
    print(image.dtype)
    pixel_data = np.array(image)
    print(pixel_data)
src = cv.imread("D:\\Users\\46071\\Desktop\\1.jpg")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)

cv.imshow("input image",src)
getImageInfo(src)
#写入图像，可以更改后缀名格式
#cv.imwrite("path",src)
#调用摄像头

#video_demo()
cv.waitKey()

cv.destroyAllWindows()
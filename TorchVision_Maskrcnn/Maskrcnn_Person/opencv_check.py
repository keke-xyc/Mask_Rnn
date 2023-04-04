import cv2
import matplotlib.pyplot as plt
import numpy as np

imgtmp = cv2.imread(r'..\test5.png')
img = cv2.resize(imgtmp, (0, 0), fx=1, fy=4, interpolation=cv2.INTER_NEAREST)

# print(img)
# 将图片转化为灰度图像
gray = cv2.cvtColor(img, code=cv2.COLOR_BGR2GRAY)
# 将灰度图像进行高斯模糊
gray1 = cv2.GaussianBlur(gray, (5, 5), 0)  # 高斯模糊

# 进行轮廓的检测
canny = cv2.Canny(gray1, 10, 20)
contours, hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print(' ———————————————— ')
print(len(contours))
print(' ———————————————— ')

for i in range(0, len(contours)):
    x, y, w, h = cv2.boundingRect(contours[i])
    if w < 10 or h < 10 or x < 10 or y < 10:
        continue
    area = cv2.contourArea(contours[i])
    if w * h < 1000:
        continue
    if w < 500:
        continue
    if len(contours[i]) < 30:
        continue
    print(' ———————————————— ')
    print(x, y, w, h)
    print(' ———————————————— ')
    cv2.drawContours(img, contours, i, (0, 0, 255), 2)
    cv2.imshow("th1", img)
    '''print(contours[i])'''
    cv2.waitKey()
    # cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 1)

# cv2.drawContours(img,contours,-1,(0,255,0),1)

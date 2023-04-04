import cv2
import io
from io import BytesIO
import binascii
import json
import numpy as np
import PIL
import os.path as osp
from labelme.logger import logger
from labelme import PY2
from labelme import QT4
import PIL.Image
import base64
from labelme import utils


# 转化成json字典
def dict_json(flags, imageData, shapes, imagePath, imageHeight=100,
              imageWidth=100):
    '''
    :param imageData: str
    :param shapes: list
    :param imagePath: str
    :return: dict
    '''
    return {"version": "4.5.6", "flags": flags, "shapes": shapes,
            'imagePath': imagePath.split('/')[-1], "imageData": imageData,
            'imageHeight': imageHeight,
            'imageWidth': imageWidth}


# 生成imagedata
def load_image_file(filename):
    try:
        image_pil = PIL.Image.open(filename)
    except IOError:
        logger.error('Failed opening image file: {}'.format(filename))
        return
    # apply orientation to image according to exif
    image_pil = utils.apply_exif_orientation(image_pil)
    with io.BytesIO() as f:
        ext = osp.splitext(filename)[1].lower()
        if PY2 and QT4:
            format = 'PNG'
        elif ext in ['.jpg', '.jpeg']:
            format = 'JPEG'
        else:
            format = 'PNG'
        image_pil.save(f, format=format)
        f.seek(0)
        return f.read()


if __name__ == '__main__':
    # 读取图片
    img_name = "test4"
    image_Path = r"..\test4.png"
    # 生成图片数据, 此处需要更改文件路径及名称
    #     image_Path = 'C:\Users\xcy\Desktop\pic2\' + img_name
    img = cv2.imread(image_Path)

    # 指定label标签
    # label = "wrong"
    label = "browser"
    imageData = load_image_file(image_Path)
    imageData = base64.b64encode(imageData).decode('utf-8')
    imageHeight = img.shape[0]
    imageWidth = img.shape[1]
    imagePath = image_Path[-12:]
    gray = cv2.cvtColor(img, code=cv2.COLOR_BGR2GRAY)
    gray1 = cv2.GaussianBlur(gray, (5, 5), 0)
    canny = cv2.Canny(gray1, 10, 10)
    contours, hierarchy = cv2.findContours(canny, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
    newshapes = []
    shapes = []
    # 定义边框属性
    shape_type = "polygon"
    # 遍历轮廓
    for i in range(len(contours)):
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
        epsilon = cv2.arcLength(contours[i], True)
        # 多边拟合

        #         approx = cv2.approxPolyDP(contours[i], epsilon, True)
        #         adp = cv2.drawContours(filled_img, [approx], 0, (0, 255, 0), 1)
        #         approx = cv2.approxPolyDP(contours[i], epsilon, True)
        adp = cv2.drawContours(img, contours, i, (0, 255, 0), 1)
        approx = adp
        approx_points = []
        # 生成需要的坐标点
        aa = contours[i]
        for m in range(len(aa)):
            approx_point_x = np.float(((aa)[m][0])[0])
            approx_point_y = np.float(((aa)[m][0])[1])
            point = [approx_point_x, approx_point_y]
            # print("point =", point)
            approx_points.append(point)
        #         print(approx_points)
        # 组合写的json成员
        flags = {}
        line_color = None
        fill_color = None
        group_id = None
        newshapes.append(
            {"label": label,
             # "line_color": line_color,
             # "fill_color": fill_color,
             "points": approx_points,
             "group_id": group_id,
             "shape_type": shape_type,
             "flags": flags})
    data_final = dict_json(flags, imageData, newshapes, imagePath,
                           imageHeight,
                           imageWidth)

    json_file = '../' + img_name + '.json'
    print(json_file)
    print("json_file =", json_file)
    json.dump(data_final, open(json_file, 'w'))

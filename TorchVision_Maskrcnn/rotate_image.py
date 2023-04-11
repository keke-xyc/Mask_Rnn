import os
import cv2
def getAllFiles(targetDir):
    listFiles = os.listdir(targetDir)
    return listFiles

def images_generate(paths):
    target_dir = paths + '/' + 'PNGImages'
    list_files = getAllFiles(target_dir)
    for i in list_files:
        mask_path = paths + '/' + 'PedMasks'
        old_path = target_dir + '/' + i
        x = i[:-4] + '_gt.png'
        mask_paths = mask_path + '/' + x
        old_img = cv2.imread(old_path)
        img = cv2.imread(mask_paths)
        img_old1_name = i[:-4] + '_1.png'
        img_mask1_name = i[:-4] + '_1_gt.png'
        img_old1_path = paths + '/' + 'newimages' + '/' + img_old1_name
        img_mask1_path = paths + '/' + 'newmasks' + '/' + img_mask1_name
        img_old1 = cv2.flip(old_img, 0)
        img_mask1 = cv2.flip(img, 0)
        cv2.imwrite(img_old1_path, img_old1)
        cv2.imwrite(img_mask1_path, img_mask1)
        img_old2_name = i[:-4] + '_2.png'
        img_mask2_name = i[:-4] + '_2_gt.png'
        img_old2_path = paths + '/' + 'newimages' + '/' + img_old2_name
        img_mask2_path = paths + '/' + 'newmasks' + '/' + img_mask2_name
        img_old2 = cv2.flip(old_img, 1)
        img_mask2 = cv2.flip(img, 1)
        cv2.imwrite(img_old2_path, img_old2)
        cv2.imwrite(img_mask2_path, img_mask2)
        img_old3_name = i[:-4] + '_3.png'
        img_mask3_name = i[:-4] + '_3_gt.png'
        img_old3_path = paths + '/' + 'newimages' + '/' + img_old3_name
        img_mask3_path = paths + '/' + 'newmasks' + '/' + img_mask3_name
        img_old3 = cv2.flip(old_img, -1)
        img_mask3 = cv2.flip(img, -1)
        cv2.imwrite(img_old3_path, img_old3)
        cv2.imwrite(img_mask3_path, img_mask3)
        img_old3_name = i[:-4] + '_4.png'
        img_mask3_name = i[:-4] + '_4_gt.png'
        img_old3_path = paths + '/' + 'newimages' + '/' + img_old3_name
        img_mask3_path = paths + '/' + 'newmasks' + '/' + img_mask3_name
        img_old3 = cv2.rotate(old_img, cv2.ROTATE_90_CLOCKWISE)
        img_mask3 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
        cv2.imwrite(img_old3_path, img_old3)
        cv2.imwrite(img_mask3_path, img_mask3)
        img_old3_name = i[:-4] + '_5.png'
        img_mask3_name = i[:-4] + '_5_gt.png'
        img_old3_path = paths + '/' + 'newimages' + '/' + img_old3_name
        img_mask3_path = paths + '/' + 'newmasks' + '/' + img_mask3_name
        img_old3 = cv2.rotate(old_img, cv2.ROTATE_180)
        img_mask3 = cv2.rotate(img, cv2.ROTATE_180)
        cv2.imwrite(img_old3_path, img_old3)
        cv2.imwrite(img_mask3_path, img_mask3)
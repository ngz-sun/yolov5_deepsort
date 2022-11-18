import cv2
import xml.etree.ElementTree as ET
import numpy as np
import xml.dom.minidom
import os



def main():
    # JPG文件的地址
    img_path = r"E:\nanguozheng\yolov4-pytorch\VOCdevkit\VOC2007\JPEGImages/"
    # XML文件的地址
    anno_path = r"E:\nanguozheng\yolov4-pytorch\VOCdevkit\VOC2007\Annotations/"
    # 存结果的文件夹

    cut_path = './data'
    if not os.path.exists(cut_path):
        os.makedirs(cut_path)
        # 获取文件夹中的文件
    imagelist = os.listdir(img_path)
    # print(imagelist
    for image in imagelist:
        image_pre, ext = os.path.splitext(image)
        img_file = img_path + image
        img = cv2.imread(img_file)
        xml_file = anno_path + image_pre + '.xml'
        # DOMTree = xml.dom.minidom.parse(xml_file)
        # collection = DOMTree.documentElement
        # objects = collection.getElementsByTagName("object")

        tree = ET.parse(xml_file)
        root = tree.getroot()
        # if root.find('object') == None:
        #     return
        obj_i = 0
        for obj in root.iter('object'):
            obj_i += 1
            print(obj_i)
            cls = obj.find('name').text
            xmlbox = obj.find('bndbox')
            b = [int(float(xmlbox.find('xmin').text)), int(float(xmlbox.find('ymin').text)),
                 int(float(xmlbox.find('xmax').text)),
                 int(float(xmlbox.find('ymax').text))]
            img_cut = img[b[1]:b[3], b[0]:b[2], :]
            path = os.path.join(cut_path, cls)
            # 目录是否存在,不存在则创建
            mkdirlambda = lambda x: os.makedirs(x) if not os.path.exists(x) else True
            mkdirlambda(path)
            try:
                cv2.imwrite(os.path.join(cut_path, cls, '{}_{:0>2d}.jpg'.format(image_pre, obj_i)), img_cut)
            except:
                continue

            print("&&&&")


if __name__ == '__main__':
    main()

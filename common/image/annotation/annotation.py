import cv2
import numpy as np
import json
from common.image.annotation import color_map
from common.fs import files

def drawAnnotationWithCoco(img, anno):
    thickness = 5

    if 'annotations' in anno:
        for item in anno['annotations']:
            cat_id = item['category_id']
            seg = item['segmentation']
            
            poly = np.array(seg)

            poly = poly.reshape(1,-1,2)

            cv2.polylines(img, np.array(poly), True, color_map.COCO_CATEGORIES[cat_id]['color'], thickness)

    return img


def readAndDrawImageByAnnotationWithCoco(img_path, anno_path):
    img = cv2.imread(img_path)
    anno = {}
    with open(anno_path, 'rb') as f:
        buf = f.read()
        encoding_name = files.find_character_set(buf)
        anno = json.loads(buf.decode(encoding_name))
    return drawAnnotationWithCoco(img, anno)
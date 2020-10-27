import cv2

def encode_image(img, ext):
    extension = ext
    if ext[0] != '.':
        extension = '.' + extension
    return cv2.imencode(extension, img)
        
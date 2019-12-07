#coding=utf-8
'''
Created on 2019年9月12日

@author: watsons
'''

import cv2
import dlib
import numpy
import sys

PREDICTOR_PATH = "predictor.dat"

# Returns the default face detector
detector = dlib.get_frontal_face_detector()

# This object is a tool that takes in an image region containing some object
# and outputs a set of point locations that define the pose of the object.
# The classic example of this is human face pose prediction, where you take
# an image of a human face as input and are expected to identify the locations
# of important facial landmarks such as the corners of the mouth and eyes,
# tip of the nose, and so forth.
predictor = dlib.shape_predictor(PREDICTOR_PATH)

def get_landmarks(img):
    """
    Get face landmarks from a rectangle region in image.
    Args:
        img: a cv2 image object.
        rect:
    Retrun:
         1 * 68 numpy matrix corresponding to landmark points.
    """
    rects = detector(img, 1) # 1 is upsampling factor.
    return [numpy.matrix([[p.x, p.y] for p in predictor(img, rect).parts()]) for rect in rects]

def annotate_landmarks(img, landmarks, font_scale = 0.3):
    """
    Annotate face landmarks on image. 
    Args:
        img: a cv2 image object.
        landmarks: numpy matrix consisted of points.
    Return:
        annotated image.
    """
    img = img.copy()
    for idx, point in enumerate(landmarks):
        pos = (point[0, 0], point[0, 1])
        cv2.putText(img, str(idx), pos,
                    fontFace=cv2.FONT_ITALIC,#FONT_HERSHEY_SCRIPT_SIMPLEX
                    fontScale=font_scale,
                    color=(0, 0, 255))
        cv2.circle(img, pos, 1, color=(255, 255, 255))
    return img

if __name__ == '__main__':
    """
    mark face key point in image.
    """
    if len(sys.argv) < 2:
        print 'please run with python test_shape_prdictor.py <imgfile> <outfolder>'
        exit(1)
    imgfile = sys.argv[1]
    outfolder = sys.argv[2]
    img = cv2.imread(imgfile, cv2.IMREAD_COLOR)
    faces_landmarks = get_landmarks(img)
    for idx, landmarks in enumerate(faces_landmarks):
        img_marked = annotate_landmarks(img, landmarks)
        cv2.imwrite(outfolder + "annotation_"+str(idx)+".png", img_marked)
    pass
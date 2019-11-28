#coding=utf-8
'''
Created on 2019年10月10日

@author: watsons
'''

import os
import sys
import glob

import dlib

if __name__ == '__main__':
    options = dlib.shape_predictor_training_options()
    
    options.oversampling_amount = 300
    # I'm also reducing the capacity of the model by explicitly increasing
    # the regularization (making nu smaller) and by using trees with
    # smaller depths.
    options.nu = 0.05
    options.tree_depth = 2
    options.be_verbose = True
    
    training_xml_path = os.path.join('train', "training_with_face_landmarks.xml")
    print training_xml_path
    dlib.train_shape_predictor(training_xml_path, "predictor.dat", options)
    
    # Now that we have a model we can test_shape_predictor it.  dlib.test_shape_predictor()
    # measures the average distance between a face landmark output by the
    # shape_predictor and where it should be according to the truth data.
    #print("\nTraining accuracy: {}".format(
    #   dlib.test_shape_predictor(training_xml_path, "predictor.dat")))
    # The real test_shape_predictor is to see how well it does on data it wasn't trained on.  We
    # trained it on a very small dataset so the accuracy is not extremely high, but
    # it's still doing quite good.  Moreover, if you train it on one of the large
    # face landmarking datasets you will obtain state-of-the-art results, as shown
    # in the Kazemi paper.
    testing_xml_path = os.path.join('test', "testing_with_face_landmarks.xml")
    print("Testing accuracy: {}".format(
        dlib.test_shape_predictor(testing_xml_path, "predictor.dat")))
    
    pass

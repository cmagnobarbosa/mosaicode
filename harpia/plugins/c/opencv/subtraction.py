#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Subtraction class.
"""
from harpia.GUI.fieldtypes import *
from harpia.plugins.c.opencv.opencvplugin import OpenCVPlugin


class Subtraction(OpenCVPlugin):
    """
    This class contains methods related the Subtraction class.
    """
    # -------------------------------------------------------------------------

    def __init__(self):
        OpenCVPlugin.__init__(self)

        # Appearance
        self.help = "Realiza a subtração de duas imagens."
        self.label = "Subtraction"
        self.color = "180:10:10:150"
        self.in_ports = [{"type":"HRP_IMAGE",
                          "name":"first_image",
                          "label":"First Image"},
                         {"type":"HRP_IMAGE",
                          "name":"first_image",
                          "label":"First Image"}
                         ]
        self.out_ports = [{"type":"HRP_IMAGE",
                           "name":"output_image",
                           "label":"Output Image"}]
        self.group = "Arithmetic and logical operations"

        self.header = r"""
// And, Xor, Division, subtraction, sum, or,
//multiplication need images with the same size
void adjust_images_size(IplImage * img1, IplImage * img2, IplImage * img3){
    if(img1->width != img2->width || img1->height != img2->height){
    int minW,minH;
    if(img1->width > img2->width)
        minW = img2->width;
    else
        minW = img1->width;

    if(img1->height > img2->height)
        minH = img2->height;
    else
        minH = img1->height;

    cvSetImageROI(img2, cvRect( 0, 0, minW, minH ));
    cvSetImageROI(img1, cvRect( 0, 0, minW, minH ));
    cvSetImageROI(img3, cvRect( 0, 0, minW, minH ));
    }
}
"""
        self.function_call = \
            'if(block$id$_img_i0 && block$id$_img_i1){\n' + \
            'block$id$_img_o0 = cvCloneImage(block$id$_img_i0);\n' + \
            'adjust_images_size(block$id$_img_i0, ' + \
            'block$id$_img_i1, block$id$_img_o0);\n' + \
            'cvSub(block$id$_img_i0, ' + \
            'block$id$_img_i1, block$id$_img_o0,0);\n' + \
            'cvResetImageROI(block$id$_img_o0);\n' + \
            '}\n'

# -----------------------------------------------------------------------------

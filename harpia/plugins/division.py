#!/usr/bin/env python
 # -*- coding: utf-8 -*-

from harpia.GUI.fieldtypes import *

class Division():

# ------------------------------------------------------------------------------
    def __init__(self):
        self.id = -1
        self.type = "23"

    # ----------------------------------------------------------------------
    def get_help(self):#Função que chama a help
        return"realiza a divisão de duas imagens."

    # ----------------------------------------------------------------------
    def generate(self, blockTemplate):
        import opencvcommon
        blockTemplate.header += opencvcommon.adjust_images_size()

        blockTemplate.imagesIO = \
            'IplImage * block$$_img_i1 = NULL;\n' + \
            'IplImage * block$$_img_i2 = NULL;\n' + \
            'IplImage * block$$_img_o1 = NULL;\n'
        blockTemplate.functionCall = '\nif(block$$_img_i1){\n' + \
                                     'block$$_img_o1 = cvCreateImage(cvSize(block$$_img_i1->width,block$$_img_i1->height),block$$_img_i1->depth,block$$_img_i1->nChannels);\n' + \
                                     'adjust_images_size(block$$_img_i1, block$$_img_i2, block$$_img_o1);\n' + \
                                     'cvDiv(block$$_img_i1, block$$_img_i2, block$$_img_o1,1);' + \
                                     '\ncvResetImageROI(block$$_img_o1);}\n'
        blockTemplate.dealloc = 'cvReleaseImage(&block$$_img_o1);\n' + \
                                'cvReleaseImage(&block$$_img_i1);\n' + \
                                'cvReleaseImage(&block$$_img_i2);\n'

    # ----------------------------------------------------------------------
    def __del__(self):
        pass

    # ----------------------------------------------------------------------
    def get_description(self):
        return {"Type": str(self.type),
            "Label": "Division",
            "Icon": "images/division.png",
            "Color": "180:10:10:150",
            "InTypes": {0: "HRP_IMAGE", 1: "HRP_IMAGE"},
            "OutTypes": {0: "HRP_IMAGE"},
            "Description": "Divide two images.",
            "TreeGroup": "Arithmetic and logical operations"
            }

    # ----------------------------------------------------------------------
    def set_properties(self, data):
        pass

    # ----------------------------------------------------------------------
    def get_properties(self):
        return {}

    # ----------------------------------------------------------------------
    def get_xml(self):
        return """
 <properties>
      <block type='"""+ str(self.type) + """' id='"""+ str(self.id) + """'>
      </block>
</properties>
    """
# ------------------------------------------------------------------------------


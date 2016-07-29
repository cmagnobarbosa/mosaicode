#!/usr/bin/env python
 # -*- coding: utf-8 -*-

from harpia.s2icommonproperties import APP, DIR
import gettext
_ = gettext.gettext
gettext.bindtextdomain(APP, DIR)
gettext.textdomain(APP)

from harpia.GUI.fieldtypes import *

class Sobel():

# ------------------------------------------------------------------------------
    def __init__(self):
        self.id = -1
        self.type = "80"
        self.masksize = 3
        self.xorder = 1
        self.yorder = 1

    # ----------------------------------------------------------------------
    def get_help(self):#Função que chama a help
        return "Operação de filtragem que utiliza uma máscara Sobel para realçar cantos e bordas da imagem."
    # ----------------------------------------------------------------------
    def generate(self, blockTemplate):
        blockTemplate.imagesIO = \
            'IplImage * block$$_img_i1 = NULL;\n' + \
            'IplImage * block$$_img_o1 = NULL;\n' + \
            'IplImage * block$$_img_t = NULL;\n'
        blockTemplate.functionCall = '\nif(block$$_img_i1){\n' + \
                                     'block$$_img_o1 = cvCreateImage(cvSize(block$$' + \
                                     '_img_i1->width,block$$_img_i1->height), IPL_DEPTH_32F,block$$' + \
                                     '_img_i1->nChannels);\n' + \
                                     'cvSobel(block$$_img_i1, block$$_img_o1 ,' + self.xorder + ',' + self.yorder + ',' + self.masksize + ' );}\n'
        blockTemplate.dealloc = 'cvReleaseImage(&block$$_img_o1);\n' + \
                                'cvReleaseImage(&block$$_img_i1);\n' + \
                                'cvReleaseImage(&block$$_img_t);\n'

    # ----------------------------------------------------------------------
    def __del__(self):
        pass

    # ----------------------------------------------------------------------
    def get_description(self):
        return {"Type": str(self.type),
            "Label": _("Sobel"),
            "Icon": "images/sobel.png",
            "Color": "250:180:80:150",
            "InTypes": {0: "HRP_IMAGE"},
            "OutTypes": {0: "HRP_IMAGE"},
            "Description": _("Filtering operation that uses the Sobel mask to enhance edges on the image."),
            "TreeGroup": _("Gradients, Edges and Corners")
            }

    # ----------------------------------------------------------------------
    def set_properties(self, data):
        self.masksize = data["masksize"]
        self.xorder = data["xorder"]
        self.yorder = data["yorder"]

    # ----------------------------------------------------------------------
    def get_properties(self):
        return {"xorder":{"name": "X Axis Derivate Order",
                            "type": HARPIA_INT,
                            "value": self.xorder,
                            "lower":0,
                            "upper":6,
                            "step":1
                            },
                "yorder":{"name": "Y Axis Derivate Order",
                            "type": HARPIA_INT,
                            "value": self.yorder,
                            "lower":0,
                            "upper":6,
                            "step":1
                            },
                "masksize":{"name": "Mask Size",
                            "type": HARPIA_INT,
                            "value": self.masksize,
                            "lower":1,
                            "upper":7,
                            "step":2
                            }
                 }

    # ----------------------------------------------------------------------
    def get_xml(self):
        return """
 <properties>
      <block type='"""+ str(self.type) + """' id='"""+ str(self.id) + """'>
        <property name='masksize' value='"""+ str(self.masksize) + """' />
        <property name='xorder' value='"""+ str(self.xorder) + """' />
        <property name='yorder' value='"""+ str(self.yorder) + """' />
      </block>
</properties>
    """
# ------------------------------------------------------------------------------

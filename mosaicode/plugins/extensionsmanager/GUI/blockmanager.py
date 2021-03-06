#!/usr/bin/env python
# -*- coding: utf-8 -*-
# noqa: E402
"""
This module contains the BlockManager class.
"""
import os
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('GtkSource', '3.0')
from gi.repository import Gtk
from gi.repository import GtkSource
from mosaicomponents.stringfield import StringField
from mosaicomponents.combofield import ComboField
from mosaicomponents.colorfield import ColorField
from mosaicomponents.commentfield import CommentField
from mosaicomponents.codefield import CodeField
from mosaicomponents.openfilefield import OpenFileField
from mosaicode.GUI.blocknotebook import BlockNotebook
from mosaicode.GUI.fieldtypes import *
from mosaicode.plugins.extensionsmanager.GUI.blockeditor import BlockEditor
from mosaicode.GUI.confirmdialog import ConfirmDialog
from mosaicode.GUI.buttonbar import ButtonBar
from mosaicode.model.blockmodel import BlockModel
from mosaicode.system import *
import gettext

_ = gettext.gettext


class BlockManager(Gtk.Dialog):
    """
    This class contains methods related the BlockManager class
    """

    # ----------------------------------------------------------------------
    def __init__(self, main_window):
        Gtk.Dialog.__init__(
                        self,
                        title=_("Block Manager"),
                        transient_for=main_window)

        self.main_window = main_window
        self.main_control = self
        self.set_default_size(400, 300)
        box = self.get_content_area()
        vbox = Gtk.VBox()
        box.pack_start(vbox, True, True, 0)

        # Block List
        self.block_notebook = BlockNotebook(self)
        self.update()
        vbox.pack_start(self.block_notebook, True, True, 0)

        # Button bar
        button_bar = ButtonBar()
        button_bar.add_button({
                "icone":Gtk.STOCK_NEW,
                "action": self.__new,
                "data":None
                })
        button_bar.add_button({
                "icone":Gtk.STOCK_EDIT,
                "action": self.__edit,
                "data":None
                })
        button_bar.add_button({
                "icone":Gtk.STOCK_DELETE,
                "action": self.__delete,
                "data":None
                })
        vbox.pack_start(button_bar, False, False, 0)

        self.show_all()
        self.show()

    # ----------------------------------------------------------------------
    def __new(self, widget=None, data=None):
        BlockEditor(self, BlockModel()).run()

    # ----------------------------------------------------------------------
    def __edit(self, widget=None, data=None):
        block = self.block_notebook.get_selected_block()
        if block is None:
            return
        BlockEditor(self, block).run()

    # ----------------------------------------------------------------------
    def __delete(self, widget=None, data=None):
        block = self.block_notebook.get_selected_block()
        if block is None:
            return
        result = ConfirmDialog(_("Are you sure?"), self).run()
        if result == Gtk.ResponseType.OK:
            self.main_window.main_control.delete_block(block)
            self.update()

    # ----------------------------------------------------------------------
    def add_new_block(self, block):
        self.main_window.main_control.add_new_block(block)

    # ----------------------------------------------------------------------
    def update(self):
        System()
        self.block_notebook.update_blocks(System.get_blocks())
# ----------------------------------------------------------------------

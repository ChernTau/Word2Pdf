# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWidgets
from Ui_WCP_UI import Ui_MainWindow


import urllib.request


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        global  my_openfile_path
        my_openfile = QtWidgets.QFileDialog.getOpenFileName(self, "OpenFile", "/")
        my_openfile_path = str(my_openfile)[2:-19]
        if my_openfile_path[-4:] == "docx" or my_openfile_path[-3:] == "doc":
            self.label.setText(my_openfile_path)
        else:
            QtWidgets.QMessageBox.warning(self, "Warning", "ERROR:Please select a file with the suffix docx or doc")

    @pyqtSlot()
    def on_pushButton_3_clicked(self):
        """
        Slot documentation goes here.
        """
        global my_savefile_path
        my_savefile = QtWidgets.QFileDialog.getSaveFileName(self, "SaveFile", "/")
        my_savefile_path = str(my_savefile)[2:-19]
        if my_savefile_path[-3:] == "pdf":
            self.label_2.setText(my_savefile_path)
        else:
            QtWidgets.QMessageBox.warning(self, "Warning", "ERROR:Please select a file with the suffix pdf" )


    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        """
        Slot documentation goes here.
        """
        try:
            file = open(my_openfile_path, 'rb')
            data = file.read()
            print(data)
            req = urllib.request.Request(
                "http://converter-eval.plutext.com:80/v1/00000000-0000-0000-0000-000000000000/convert", data)
            req.add_header('Content-Length', '%d' % len(data))
            req.add_header('Content-Type', 'application/octet-stream')

            # make the request
            res = urllib.request.urlopen(req)

            # write the response to a file
            pdf = res.read()
            f = open(my_savefile_path, 'wb')
            f.write(pdf)
        except NameError as reason:
            QtWidgets.QMessageBox.Information(self, "Information", "ERROR:"+str(reason))
        finally:
            self.label_3.setText("Success")


        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())

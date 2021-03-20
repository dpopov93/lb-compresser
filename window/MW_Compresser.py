#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
Qt interface for utility jsmin
Compress your JavaScript files

Author: Denis Popov
E-mail: d.popov93@mail.ru
Created: 20.03.2021
Version: 0.1

'''

from PyQt5.QtWidgets import QMainWindow, QWidget, QLineEdit, QPushButton, QFileDialog, QMessageBox
from os import path
from PyQt5 import uic
from PyQt5.QtGui import QIcon
from jsmin import jsmin

class MW_Compresser(QMainWindow):
    def __init__(self, app_path):
        super().__init__()
        uic.loadUi("window\\mw_compresser.ui", self)
        self.setWindowIcon(QIcon(app_path + path.sep + "icon" + path.sep + 'Compresser_Logo.ico'))
        self.file_storage = ""
        
        linepath_inputfile = self.linepath_inputfile
        linepath_outfile = self.linepath_outfile
        opendialog_inputfile = self.opendialog_inputfile
        opendialog_outfile = self.opendialog_outfile
        compress_button = self.compress_button
        
        opendialog_inputfile.clicked.connect(self.opendialog_inputfile_clicked)
        opendialog_outfile.clicked.connect(self.opendialog_outfile_clicked)
        compress_button.clicked.connect(self.compress_button_clicked)
        
    def opendialog_inputfile_clicked(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(self,"Select file for compress", "","Javascript Files (*.js)", options=options)
        if file_name:
            try:
                file = open(file_name, 'r')
            except Exception:
                QMessageBox.critical(self,"Error", "Get opening error")
            else:
                self.linepath_inputfile.setText(file_name)
            finally:
                file.close()
        
    def opendialog_outfile_clicked(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getSaveFileName(self, "Select output file","","Compressed Javascript (*.min.js)", options=options)
        if file_name:
            file_basename = path.basename(file_name)
            output_string = ""
            if file_basename[-7:] == ".min.js":
                output_string = file_name
            else:
                output_string = path.split(file_name)[0]
                if (path.split(file_name)[0][-1] != '/'):
                    output_string += '/'
                output_string += file_basename.split('.')[0] + '.min.js'
            self.linepath_outfile.setText(output_string)
    
    def compress_button_clicked(self):
        if self.linepath_inputfile.text() == "" or self.linepath_outfile.text() == "":
            return
        if path.basename(self.linepath_inputfile.text())[-3:] == '.js':
            try:
                with open(self.linepath_inputfile.text()) as js_file:
                    minified = jsmin(js_file.read())
            except:
                QMessageBox.critical(self,"Error reading file", "File " + self.linepath_inputfile.text() + ", can't be read!")
                return
            if path.basename(self.linepath_outfile.text())[-7:] == '.min.js':
                try:
                    if minified:
                        out_file = open(self.linepath_outfile.text(), "w")
                        out_file.write(''.join(minified.splitlines()))
                except:
                    QMessageBox.critical(self,"Error compressing file", "Please check output path permissions")
                else:
                    QMessageBox.information(self, "LuckyBoard Compresser", "Compression was successful")
                finally:
                    out_file.close()
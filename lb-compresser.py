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

import sys, os
from window.MW_Compresser import MW_Compresser
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MW_Compresser(os.path.dirname(os.path.realpath(__file__)))
    window.show()
    sys.exit(app.exec_())
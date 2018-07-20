# -*- coding: utf-8 -*-
'''
Created on Jul 19, 2018

@author: Angela
'''

import os


class File:
    def find_file(self, file_path):
        lists = os.listdir(file_path)
        lists.sort(key=lambda fn:os.path.getctime(file_path + '\\' + fn))
        latest_report = os.path.join(file_path, lists[-1])
        print('The latest file is', latest_report)
        return latest_report
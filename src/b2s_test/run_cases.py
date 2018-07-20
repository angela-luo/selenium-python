# -*- coding: utf-8 -*-
'''
Created on Jul 13, 2018
Updated on Jul 19, 2018

@author: Angela
'''

import unittest
import HTMLTestRunner
import time, os
from b2s_test.common.send_email import Email
from b2s_test.common.find_file import File

if __name__ == "__main__":
    testsuite = unittest.TestSuite()
    test_dir = os.path.dirname(__file__) + '\\test_cases'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern = 'test_*.py')
    path = os.path.abspath('..') +'\\report\\'
    now = time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime())
    file = path + now + '_TestReport.html'
    fp = open(file, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"B2S Test Report", description=u"B2S Test Cases")
    runner.run(discover)
    fp.close()
    
    f=File()
    report = f.find_file(path)
    attach_path= path + '\\screenshots'
    attach = f.find_file(attach_path)
    
    e=Email()
    e.send_email(report, attach, now)
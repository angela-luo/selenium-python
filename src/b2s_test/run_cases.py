'''
Created on Jul 13, 2018

@author: Angela
'''
import unittest
import HTMLTestRunner
import time, os

if __name__ == "__main__":
    testsuite = unittest.TestSuite()
    test_dir = os.path.dirname(__file__) + '\\test_cases'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern = 'test_*.py')
    path = os.path.abspath('..') +'\\report\\'
    now = time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime())
    file = path + now + '_TestReport.html'
    print(file)
    fp = open(file, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"B2S Test Report", description=u"B2S Test Cases")
    runner.run(discover)
    fp.close()
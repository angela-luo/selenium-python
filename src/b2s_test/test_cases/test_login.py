# -*- coding: utf-8 -*-
'''
Created on Jul 6, 2018

@author: Administrator
'''

import unittest, os, sys
p = os.path.abspath('..')
sys.path.append(p)
from b2s_test.page_objects.login_pg import Login 


class TestLogin(unittest.TestCase):
    """test cases for login"""

    def test_login01(self, username='demo', password= 'demo', program='wf_ui_test', var= 'wf', locale='en_US'):
        u"""test login of wf"""
        Login().login(username, password, program, var, locale)

    def test_login02(self, username='demo', password= 'demo', program='points_only', var= 'fis', locale='en_US'):
        """test login of fis"""
        Login().login(username, password, program, var, locale)
        
    def tearDown(self):
        pass
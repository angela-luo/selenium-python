'''
Created on Jul 6, 2018

@author: Angela
'''

import selenium
import os, sys
import time
from selenium import webdriver
from b2s_test.common.driver import Driver

class Login(object):


    def setUp(self):
        pass

    def tearDown(self):
        self.driver.quit()


    def login(self, username, password, program, var, locale):
        self=Driver()
        self.open_url()
        print(self.driver.title)
        self.driver.find_element_by_id('userid').clear()
        self.driver.find_element_by_id('userid').send_keys(username)
        self.driver.find_element_by_id('pword').clear()
        self.driver.find_element_by_id('pword').send_keys(password)
        self.driver.find_element_by_id('programid').clear()
        self.driver.find_element_by_id('programid').send_keys(program)
        self.driver.find_element_by_id('varid').clear()
        self.driver.find_element_by_id('varid').send_keys(var)
        self.driver.find_element_by_id('locale').clear()
        self.driver.find_element_by_id('locale').send_keys(locale)
        self.driver.find_element_by_xpath("//input[@type='submit']").click()
        print('Login successfully')

        
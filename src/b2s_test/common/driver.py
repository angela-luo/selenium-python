'''
Created on Jul 9, 2018

@author: Angela
'''
# -*- coding:utf-8 -*-
import configparser
import os, sys
from selenium import webdriver

root_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
config_path = root_dir+'\config\config.ini'    
config = configparser.ConfigParser()
config.read(config_path)
    
class Driver(object):
    '''
    Define browser driver
    '''  

        
    def driver(self):
        driver_path=root_dir+'\drivers'
        browser=config.get('browserType', 'browserName')
        
        if browser == 'Chrome':
            self.driver = webdriver.Chrome(driver_path + '\chromedriver.exe')
        elif browser == 'IE':
            self.driver = webdriver.Ie(driver_path + '\MicrosoftWebDriver.exe')
        elif browser == 'Firefox':
            self.driver = webdriver.Firefox
        else:
            self.driver = webdriver.Chrome(driver_path + '\chromedriver.exe')
        driver=self.driver   
        return driver
            
    def open_url(self, url='/b2r/pages/login.jsp'):
        driver=self.driver()
        server=config.get('testServer', 'URL')
        driver.get(server + url)
        driver.maximize_window()
        driver.implicitly_wait(10)

        
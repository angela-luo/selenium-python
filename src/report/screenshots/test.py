'''
Created on Jul 10, 2018

@author: Administrator
'''
import os
import sys
import configparser
from selenium import webdriver
#sys.path.append("..") 
#from b2s_test.page_objects.login_pg import *
import unittest

   
root_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
config_path = root_dir+'\config\config.ini'    
config = configparser.ConfigParser()
config.read(config_path)
    
class TestLogin(unittest.TestCase):
    '''
    Define browser driver
    ''' 
    def engine(self):
        driver_path= os.path.dirname(os.path.abspath('..')) + '\drivers'
        print(driver_path)
        browser=config.get('browserType', 'browserName')
        print(browser)
        if browser == 'Chrome':
            print(driver_path + '\chromedriver.exe')
            self.driver = webdriver.Chrome(driver_path + '\chromedriver.exe')
        elif browser == 'IE':
            self.driver = webdriver.Ie(driver_path + '\MicrosoftWebDriver.exe')
        elif browser == 'Firefox':
            self.driver = webdriver.Firefox
        else:
            self.driver = webdriver.Chrome(r'src\drivers\chromedriver.exe')
        driver=self.driver   
        return driver
        
            
    def open_url(self, url='/b2r/pages/login.jsp'):
        driver=self.engine()
        server=config.get('testServer', 'URL')
        driver.get(server + url)
        driver.maximize_window()
        driver.implicitly_wait(20)
    
    def login(self, username, password, program, var, locale):
        self.open_url()
        print(self.driver.current_url)
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
        print(self.driver.current_url)
        print(self.driver.title)
        
    def test_login(self):
        self.Login(username='demo', password= 'demo', program='wf_ui_test', var= 'wf', locale='en_US' )
       
if __name__ == "__main__":
    unittest.main()
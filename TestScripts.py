#coding:utf-8
import time
import unittest
from selenium import webdriver as wbd
from Log_Module import log_Module

class Test001(unittest.TestCase):
    def setUp(self):
        self.driver=wbd.Chrome(r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
        self.driver.get('file:///C:/Users/zhengbw/Desktop/demo_complete.html')
        self.log=log_Module()
        self.log_file=self.log.open_file()
    def tearDown(self):
        self.log.close_file(self.log_file)
        self.driver.close()

    def test_alert(self):
        self.log.save_log(self.log_file,"start test alert!")
        self.driver.find_element_by_xpath('/html/body/center/p[1]/table/tbody/tr[2]/td[2]/input').click()
        time.sleep(1)
        text=self.driver.switch_to_alert().text
        print text
        try:
            self.assertEqual(u'alert对话框',text)
        except AssertionError as e:
            self.log.save_log(self.log_file,"False")
            print "False"
        
        self.driver.switch_to_alert().accept()
        

if __name__=='__main__':
    unittest.main()

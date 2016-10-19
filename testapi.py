#coding:utf-8

import os
import time
import unittest
import autoit
from selenium import webdriver as wbd
import log_test as log

class TestComplete(unittest.TestCase):

    def setUp(self):
        driver=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
        self.dr=wbd.Chrome(driver)
        file_path=r'file:///C:/Python27/demo_complete.html'
        self.dr.get(file_path)
        time.sleep(1)
        self.log_file=log.open_log()
    def tearDown(self):
        self.log_file.close()
        self.dr.close()

    def test_alert(self):
        log.save_log(self.log_file,'start test alert')
        self.dr.find_element_by_name('alertbutton').click()
        time.sleep(1)
        self.assertEqual(self.dr.switch_to_alert().text,u'测试alert对话框')
        time.sleep(1)
        self.dr.switch_to_alert().accept()
        normal=False
        try:
            self.dr.switch_to_alert().accept()
        except:
            normal=True
        self.assertTrue(normal)

    
            
    def test_confirm_1(self):
        log.save_log(self.log_file,'start test confirm ok')
        self.dr.find_element_by_name('confirmbutton').click()
        time.sleep(1)
        self.assertRqual(self.dr.switch_to_alert().text,u'测试confirm对话框')
        time.sleep(0.1)
        self.dr.switch_to_alert().accept()
        time.sleep(0.1)
        self.assertEqual(self.dr.switch_to_alert().text,u'You presssed OK!')
        time.sleep(0.1)
        self.dr.switch_to_alert().accept()
        time.sleep(0.1)
        normal=False
        try:
            self.dr.switch_to_alert().accept()
        except:
            normal=True
        self.assertTrue(normal)
        

    def test_confirm_2(self):
        log.save_log(self.log_file,'start test confirm cancel')
        self.dr.find_element_by_name('confirmbutton').click()
        time.sleep(1)
        self.assertRqual(self.dr.switch_to_alert().text,u'测试confirm对话框')
        time.sleep(0.1)
        self.dr.switch_to_alert().accept()
        time.sleep(0.1)
        self.assertEqual(self.dr.switch_to_alert().text,u'You presssed Cancel!')
        time.sleep(0.1)
        self.dr.switch_to_alert().dismiss()
        normal=False
        try:
            self.dr.switch_to_alert().accept()
        except:
            normal=True
        self.assertTrue(normal)
    def test_select_1(self):
        log.save_log(self.log_file,'start test_select_1')
        test_value=u'苹果'
        self.dr.find_element_by_id('Selector').click()
        time.sleep(0.1)
        option_list=self.dr.find_element_by_id('Selector').find_elements_by_tag_name('option')
        for ii in option_list:
            if ii.text==test_value:
                ii.click()
        time.sleep(0.1)
        self.dr.find_element_by_id('Selector').click()
        self.dr.find_element_by_id('showSelectResult').click()
        time.sleep(0.1)
        self.assertEqual(self.dr.switch_to_alert().text,test_value)
        self.dr.switch_to_alert().accept()
        time.sleep(0.1)
        normal=False
        try:
            self.dr.switch_to_alert().accept()
        except:
            normal=True
        self.assertTrue(normal)
    


        

        
    def test_select_2(self):
        log.save_log(self.log_file,'start test_select_1')
        test_value=u'桃子'
        self.dr.find_element_by_id('Selector').click()
        time.sleep(0.1)
        option_list=self.dr.find_element_by_id('Selector').find_elements_by_tag_name('option')
        for ii in option_list:
            if ii.text==test_value:
                ii.click()
        time.sleep(0.1)
        self.dr.find_element_by_id('Selector').click()
        self.dr.find_element_by_id('showSelectResult').click()
        time.sleep(0.1)
        self.assertEqual(self.dr.switch_to_alert().text,test_value)
        self.dr.switch_to_alert().accept()
        time.sleep(0.1)
        normal=False
        try:
            self.dr.switch_to_alert().accept()
        except:
            normal=True
        self.assertTrue(normal)
    def test_select_3(self):
        log.save_log(self.log_file,'start test_select_1')
        test_value=u'香蕉'
        self.dr.find_element_by_id('Selector').click()
        time.sleep(0.1)
        option_list=self.dr.find_element_by_id('Selector').find_elements_by_tag_name('option')
        for ii in option_list:
            if ii.text==test_value:
                ii.click()
        time.sleep(0.1)
        self.dr.find_element_by_id('Selector').click()
        self.dr.find_element_by_id('showSelectResult').click()
        time.sleep(0.1)
        self.assertEqual(self.dr.switch_to_alert().text,test_value)
        self.dr.switch_to_alert().accept()
        time.sleep(0.1)
        normal=False
        try:
            self.dr.switch_to_alert().accept()
        except:
            normal=True
        self.assertTrue(normal)
    def test_select_4(self):
        log.save_log(self.log_file,'start test_select_1')
        test_value=u'葡萄'
        self.dr.find_element_by_id('Selector').click()
        time.sleep(0.1)
        option_list=self.dr.find_element_by_id('Selector').find_elements_by_tag_name('option')
        for ii in option_list:
            if ii.text==test_value:
                ii.click()
        time.sleep(0.1)
        self.dr.find_element_by_id('Selector').click()
        self.dr.find_element_by_id('showSelectResult').click()
        time.sleep(0.1)
        self.assertEqual(self.dr.switch_to_alert().text,test_value)
        self.dr.switch_to_alert().accept()
        time.sleep(0.1)
        normal=False
        try:
            self.dr.switch_to_alert().accept()
        except:
            normal=True
        self.assertTrue(normal)
    def test_select_5(self):
        log.save_log(self.log_file,'start test_select_1')
        test_value=u'芒果'
        self.dr.find_element_by_id('Selector').click()
        time.sleep(0.1)
        option_list=self.dr.find_element_by_id('Selector').find_elements_by_tag_name('option')
        for ii in option_list:
            if ii.text==test_value:
                ii.click()
        time.sleep(0.1)
        self.dr.find_element_by_id('Selector').click()
        self.dr.find_element_by_id('showSelectResult').click()
        time.sleep(0.1)
        self.assertEqual(self.dr.switch_to_alert().text,test_value)
        self.dr.switch_to_alert().accept()
        time.sleep(0.1)
        normal=False
        try:
            self.dr.switch_to_alert().accept()
        except:
            normal=True
        self.assertTrue(normal)
    def test_select_6(self):
        log.save_log(self.log_file,'start test_select_1')
        test_value=u'桔子'
        self.dr.find_element_by_id('Selector').click()
        time.sleep(0.1)
        option_list=self.dr.find_element_by_id('Selector').find_elements_by_tag_name('option')
        for ii in option_list:
            if ii.text==test_value:
                ii.click()
        time.sleep(0.1)
        self.dr.find_element_by_id('Selector').click()
        self.dr.find_element_by_id('showSelectResult').click()
        time.sleep(0.1)
        self.assertEqual(self.dr.switch_to_alert().text,test_value)
        self.dr.switch_to_alert().accept()
        time.sleep(0.1)
        normal=False
        try:
            self.dr.switch_to_alert().accept()
        except:
            normal=True
        self.assertTrue(normal)
    def test_RadioBox(self):
        log.save_log(self.log_file,'start test RadioBox')
        radio_list=[u'百度',u'阿里巴巴',u'腾讯',u'小米']
        radio_class_list=[u'Baidu',u'AliBaBa',u'Tencent',u'Mi']
        check_key=None
        time.sleep(2)
        for ii in self.dr.find_element_by_id('radio').find_elements_by_tag_name('input'):
            if ii.is_selected():
                self.assertEqual(ii.get.attribute('class'),radio_class_list[2],u'默认选中不是Tencent'+ii.get_attribute('class'))
                if check_key is None:
                    check_key='success'
                else:
                    check_key='error'
        self.assertEqual(check_key,'success','被选中的选项不止一个，也有可能是0个')

'''
    def test_upload(self):
        log.save_log(self.log_file,'start test_upload')
        self.dr.find_elememt_by_name('attach[]').click()
        log.save_log(self.log_file,'点击上传控件')
        autoit.win_wait_active("[CLASS:32770]",3)
        time.sleep(2)
        autoit.control_send("[CLASS:32770]","Edit1",r"C:\Python27\1.png")
        log.save_log(self.log_file,"输入上传文件路径")
        time.sleep(2)
        autoit.control_click("[CLASS#32770]","Button1")
        log.save_log(self.log_file,'点击打开按钮')
        time.sleep(2)
    '''

if __name__=='__main__':
    unittest.main()

#coding:utf-8

import os,time,datetime
from selenium import webdriver as wbd
import unittest
import log_test as log
class TestApi(unittest.TestCase):
    def setUp(self):
        driver=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
        self.chr=wbd.Chrome(driver)
        file_path=r'C:\Python27\demo_complete.html'
        self.chr.get(file_path)
        self.log_file=log.open_log()
    def tearDown(self):
        self.chr.close()
        self.log_file.close()
    def testUpload(self):pass
    def testAlert(self):
        log.save_log(self.log_file,'start test alert!')
        self.chr.find_element_by_name('alterbutton').click()
        time.sleep(1)
        alert_text=self.chr.switch_to_alert().text
        self.assertEqual(alert_text,u'测试alert对话框')
        self.chr.switch_to_alert().accept()
        time.sleep(1)
        self.chr.switch_to_default_content()
    def testConfirm_1(self):
        log.save_log(self.log_file,'start test confirm with ok!')
        self.chr.find_element_by_name('confirmbutton').click()
        time.sleep(1)
        confirm_text=self.chr.switch_to_alert().text
        time.sleep(1)
        self.assertEqual(confirm_text,u'测试confirm对话框')
        time.sleep(1)
        self.chr.switch_to_alert().accept()
        time.sleep(1)
        confirm_text1=self.chr.switch_to_alert().text
        time.sleep(1)
        self.assertEqual(confirm_text1,u'You pressed OK!')
        time.sleep(1)
        self.chr.switch_to_alert().accept()
        time.sleep(1)
        self.chr.switch_to_default_content()

    def testConfirm_2(self):
        log.save_log(self.log_file,'start test confirm with cancel!')
        self.chr.find_element_by_name('confirmbutton').click()
        time.sleep(1)
        confirm_text=self.chr.switch_to_alert().text
        time.sleep(1)
        self.assertEqual(confirm_text,u'测试confirm对话框')
        time.sleep(1)
        self.chr.switch_to_alert().dismiss()
        time.sleep(1)
        confirm_text2=self.chr.switch_to_alert().text
        time.sleep(1)
        self.assertEqual(confirm_text2,u'You pressed Cancel!')
        time.sleep(1)
        self.chr.switch_to_alert().accept()
        time.sleep(1)
        self.chr.switch_to_default_content()
    def testSelect_1(self):
        text='apple'
        log.save_log(self.log_file,'start test selector {}'.format(text))
        self.chr.find_element_by_id('Selector').click()
        time.sleep(1)
        optionList=self.chr.find_element_by_id('Selector').find_elements_by_tag_name('option')
        time.sleep(1)
        for i in optionList:
            if i.get_attribute('value')==text:
                log.save_log(self.log_file,text)
                i.click()

        self.chr.find_element_by_name('showSelectResult').click()
        time.sleep(1)
        alert_name=self.chr.switch_to_alert().text
        self.assertEqual(alert_name,u'苹果')
        time.sleep(1)
        self.chr.switch_to_alert().accept()
        time.sleep(1)
        self.chr.switch_to_default_content()

    def testSelect_2(self):
        text='peach'
        log.save_log(self.log_file,'start test selector {}'.format(text))
        self.chr.find_element_by_id('Selector').click()
        time.sleep(1)
        optionList=self.chr.find_element_by_id('Selector').find_elements_by_tag_name('option')
        time.sleep(1)
        for i in optionList:
            if i.get_attribute('value')==text:
                log.save_log(self.log_file,text)
                i.click()

        self.chr.find_element_by_name('showSelectResult').click()
        time.sleep(1)
        alert_name=self.chr.switch_to_alert().text
        self.assertEqual(alert_name,u'桃子')
        time.sleep(1)
        self.chr.switch_to_alert().accept()
        time.sleep(1)
        self.chr.switch_to_default_content()
    def testSelect_3(self):
        text='banana'
        log.save_log(self.log_file,'start test selector{}'.format(text))
        self.chr.find_element_by_id('Selector').click()
        time.sleep(1)
        optionList=self.chr.find_element_by_id('Selector').find_elements_by_tag_name('option')
        time.sleep(1)
        for i in optionList:
            if i.get_attribute('value')==text:
                log.save_log(self.log_file,text)
                i.click()

        self.chr.find_element_by_name('showSelectResult').click()
        time.sleep(1)
        alert_name=self.chr.switch_to_alert().text
        self.assertEqual(alert_name,u'香蕉')
        time.sleep(1)
        self.chr.switch_to_alert().accept()
        time.sleep(1)
        self.chr.switch_to_default_content()
    def testSelect_4(self):
        text='orange'
        log.save_log(self.log_file,'start test selector {}'.format(text))
        self.chr.find_element_by_id('Selector').click()
        time.sleep(1)
        optionList=self.chr.find_element_by_id('Selector').find_elements_by_tag_name('option')
        time.sleep(1)
        for i in optionList:
            if i.get_attribute('value')==text:
                log.save_log(self.log_file,text)
                i.click()

        self.chr.find_element_by_name('showSelectResult').click()
        time.sleep(1)
        alert_name=self.chr.switch_to_alert().text
        self.assertEqual(alert_name,u'桔子')
        time.sleep(1)
        self.chr.switch_to_alert().accept()
        time.sleep(1)
        self.chr.switch_to_default_content()
    def testSelect_5(self):
        text='grape'
        log.save_log(self.log_file,'start test selector {}'.format(text))
        self.chr.find_element_by_id('Selector').click()
        time.sleep(1)
        optionList=self.chr.find_element_by_id('Selector').find_elements_by_tag_name('option')
        time.sleep(1)
        for i in optionList:
            if i.get_attribute('value')==text:
                log.save_log(self.log_file,text)
                i.click()

        self.chr.find_element_by_name('showSelectResult').click()
        time.sleep(1)
        alert_name=self.chr.switch_to_alert().text
        self.assertEqual(alert_name,u'葡萄')
        time.sleep(1)
        self.chr.switch_to_alert().accept()
        time.sleep(1)
        self.chr.switch_to_default_content()
    def testSelect_6(self):
        text='mango'
        log.save_log(self.log_file,'start test selector {}'.format(text))
        self.chr.find_element_by_id('Selector').click()
        time.sleep(1)
        optionList=self.chr.find_element_by_id('Selector').find_elements_by_tag_name('option')
        time.sleep(1)
        for i in optionList:
            if i.get_attribute('value')==text:
                log.save_log(self.log_file,text)
                i.click()

        self.chr.find_element_by_name('showSelectResult').click()
        time.sleep(1)
        alert_name=self.chr.switch_to_alert().text
        self.assertEqual(alert_name,u'芒果')
        time.sleep(1)
        self.chr.switch_to_alert().accept()
        time.sleep(1)
        self.chr.switch_to_default_content()
    def testRadioBox(self):
        ra_list=['Baidu','AliBaBa','Tencent']
        log.save_log(self.log_file,'start test radiobox')
        radiolist=self.chr.find_element_by_xpath('//*[@id="radio"]').find_elements_by_tag_name('input')

        '''测试默认选中腾讯'''

        for ls in radiolist:
            if ls.is_selected():
                self.assertEqual(ls.get_attribute('class'),'Tencent',u'默认选中不是Tencent'+ls.get_attribute('class'))

        '''测试小米不可选中'''
        for ls in radiolist:
            bool=ls.get_attribute('disabled')
            if ls.get_attribute('class')=='Mi':
                if bool:
                    log.save_log(self.log_file,'Pass!')
                else:
                    log.save_log(self.log_file,'Fail!')

        '''测试百度、阿里、腾讯是否可选'''
        for i in ra_list:
            for ls in radiolist:
                if ls.get_attribute('class')==i:
                    log.save_log(self.log_file,i)
                    ls.click()
                    self.assertEqual(ls.get_attribute('class'),i)
                    time.sleep(1.5)
                
        
    def testCheckBox(self):
        normal=False
        checkbox_list=['web','training','friend','other']
        log.save_log(self.log_file,'start test checkbox')
        checkbox_option=self.chr.find_element_by_id('checkbox').find_elements_by_tag_name('input')
        checkbox_name=self.chr.find_element_by_id('checkbox').find_elements_by_tag_name('label')
        '''检查是否有默认选中'''
        for i in checkbox_option:
            if i.is_selected():
                log.save_log(self.log_file,'{} is selected!'.format(i.get_attribute('id')))
                normal=True
        if normal==False:
            log.save_log(self.log_file,'nothing is default selected!')
            
        '''测试四个选项的勾选与取消'''   
        for i in checkbox_list:
            for x in checkbox_option:
                if x.get_attribute('id')==i:
                    log.save_log(self.log_file,'勾选 {}'.format(x.get_attribute('id')))
                    time.sleep(1)
                    x.click()
                
        
        for x in checkbox_option:
            if x.is_selected():
                log.save_log(self.log_file,'取消勾选 {}'.format(x.get_attribute('id')))
                time.sleep(1)
                x.click()           
                
        
#if __name__=='__main__':
#    unittest.main()

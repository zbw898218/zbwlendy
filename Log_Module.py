#coding:utf-8
import os
import time
import datetime
'''
此模块是为log存储及读取提供方法：
初始化该模块，通过_fulpath（）会产生log文件完整路径

'''
class log_Module():
    def __init__(self,path=None):
        self._path=path

    def _fulpath(self):
        if not self._path:
            self._path=os.path.abspath('.')+'\zbw\log\\'+str(datetime.datetime.now().date())

        if not os.path.exists(self._path):
            os.makedirs(self._path)
        file_name='-'.join(str(datetime.datetime.now().time())[:2].split(':'))
        full_path=self._path+'\\'+file_name
        return full_path
'''
此方法打开日志文件，返回操作文件读写变量 f
'''
    def open_file(self):
        full_path=self._fulpath()

        f=open(full_path,'a')
        f.write('='*60)
        f.write('\n')
        return f
'''
此方法关闭日志文件
'''
    def close_file(self,f):
        f.close()
'''
此方法存储日志内容，通过open_file（）方法获得操作文件读写变量后，进行实际读写操作
'''
    def save_log(self,fc,text=None):
        time=str(datetime.datetime.now())[:-7]
        
        #fc.write('\t')
        if not text:
            fc.write(time)
            fc.write('\t')
            fc.write('*'*60)
        else:
            fc.write(time)
            fc.write('\t')
            fc.write(text)
            
'''
此方法提供读取日志文件方法
'''        
        
    def read_log(self,full_path=None):
        if not full_path:
            full_path=self._fulpath()
        try:
            with open(full_path,'r') as f:
                for line in f.readlines():
                    print line
        except Error:
            raise 'Failed to open the log file!'



        
        
        
        

#coding:utf-8
import os
import time
import datetime

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

    def open_file(self):
        full_path=self._fulpath()

        f=open(full_path,'a')
        f.write('='*60)
        f.write('\n')
        return f

    def close_file(self,f):
        f.close()
    def save_log(self,fc,text=None):
        time=str(datetime.datetime.now())[:-7]
        
        fc.write('\t')
        if not text:
            fc.write(time)
            fc.write('\t')
            fc.write('*'*60)
        else:
            fc.write(time)
            fc.write('\t')
            fc.write(text)
            
            
        
    def read_log(self):
        full_path=self._fulpath()
        with open(full_path,'r') as f:
            for line in f.readlines():
                print line



        
        
        
        

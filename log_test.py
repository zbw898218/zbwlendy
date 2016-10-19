#coding:utf-8
import os
from datetime import datetime as dt
import datetime
def open_log():
    '''
    以log/年-月-日/小时.txt 增量模式打开日志文件
    先检查log/年-月-日/目录是否存在，不存在就创建目录
    打开后，先写入一行分隔符
    ：return 日志文件的操作变量
    '''

    file_dir=os.path.abspath('zbw')+'\log\\'+str(dt.now().date())
    if not os.path.exists (file_dir):
        os.makedirs(file_dir)
    file_name=file_dir+'\\'+str(dt.now().time())[:2]+'.txt'
    f=open(file_name,'a+')
    f.write('*'*60)
    f.write('\n')
    return f

def save_log(file_ctrl,log_text=None):
    '''
    向日志文件格式化输入日志内容
    :param file_ctrl: 日志文件的操作变量
    :param log_text：日志内容，为None时写入以-组成的分隔符
    :return： 无
    '''
    if not log_text:
        file_ctrl.write('-'*60)
    else:
        file_ctrl.write(str(dt.now())[:-7])
        file_ctrl.write('\t')
        file_ctrl.write(log_text)
    file_ctrl.write('\n')

if __name__ == '__main__':
    a = open_log()
    save_log(a, '调试1……')
    save_log(a)
    save_log(a, '继续调试1……')
    a.close()
    a = open_log()
    save_log(a, '调试2……')

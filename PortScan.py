#!/usr/bin/python
# -*- coding:utf8 -*-

import socket, time, thread,sys
from time import sleep
# 设置socket超时时间
socket.setdefaulttimeout(3)


threadCount = 2000 #最大线程数
threadNum = 0 # 当前线程数

#准备扫描
def socket_port(ip,port):
    
    ''''
    输入IP和端口号，扫描判断端口是否开放
    '''
    global threadNum
    try:
        if port>=65535:
            print u'端口扫描结束'
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result=s.connect_ex((ip,port))
        if result==0:
            lock.acquire()
            wirteFile(str(port))
            print  ip,u':--------------------------->',port,u'端口开放'
            lock.release()
        s.close()
        threadNum = threadNum - 1
    except:
        print u'端口扫描异常'


def wirteFile(str):
    f = open('result.txt','w+')
    f.write(str)
    f.close()
    pass

def ip_scan(ip):
   
    global threadCount
    global threadNum
    try:
        print u'开始扫描 %s' % ip
        start_time=time.time()
        i = 1
        while True:
            if threadNum < threadCount:
                threadGo(ip,i)
                if i == 65535:
                    break
                else:
                    i = i + 1
                print u'当前端口:',str(i)
                print u'当前线程数:',threadNum
            else:
                pass
#                 sleep(0.5)
                #thread.sleep(0.5)
            # socket_port(ip,int(i))
            # print u'扫描端口',str(i)
        print u'扫描端口完成，总共用时 ：%.2f' %(time.time()-start_time)
    except:
        print u'扫描ip出错'



def threadGo(ip,i):        
    global threadCount
    global threadNum
    if threadNum < threadCount:
        thread.start_new_thread(socket_port,(ip,int(i)))
        threadNum = threadNum + 1
    else:
        pass
#         sleep(0.5)

 
if __name__=='__main__':
    url = '8.8.8.8'
    lock=thread.allocate_lock()
    ip_scan(url)
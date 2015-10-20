#-*-coding:utf8-*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header
#from follow_the_girl.models import tb_use_map_id,tb_follow_info
#from follow_the_girl.models import tb_follow_info

from lxml import etree
import os
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class mailhelper(object):
    '''
    这个类实现发送邮件的功能
    '''
    def __init__(self):

        self.mail_host="smtp.126.com"  #设置服务器
        self.mail_user="qiuzhongzi"    #用户名
        self.mail_pass="134556"   #密码
        self.mail_postfix="126.com"  #发件箱的后缀

    def send_mail(self,to_list,sub,content):
        me="xxoohelper"+"<"+self.mail_user+"@"+self.mail_postfix+">"
        msg = MIMEText(content,_subtype='plain',_charset='utf-8')
        msg['Subject'] = sub
        msg['From'] = me
        msg['To'] = ";".join(to_list)
        try:
            server = smtplib.SMTP()
            server.connect(self.mail_host)
            server.login(self.mail_user,self.mail_pass)
            server.sendmail(me, to_list, msg.as_string())
            server.close()
            return True
        except Exception, e:
            print str(e)
            return False


import MySQLdb

Con= MySQLdb.connect(host='localhost',user='root',passwd='itcast',db='thegirl')

cursor =Con.cursor()

sql ="select * from follow_the_girl_tb_follow_info"



cursor.execute(sql)

row=cursor.fetchone()
row=cursor.fetchone()
while True:
    fans = int(row[11])
    print row[12]
    print row[13]
    print type(fans)
    print fans
    if  fans > 5:
        mailto_list=['799244788@qq.com'] #此处填写接收邮件的邮箱
        if mailhelper().send_mail(mailto_list,u"女神更新啦",'fuck utf-8'):
            print 'seccess'
        else:
            print 'failed'
    else:
        time.sleep(10)

cursor.close()

Con.close()



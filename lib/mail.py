#coding=utf-8

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr
import conf.mail
import lib.log
import sys


def check_sina_email(e,p):
    smtpObj = smtplib.SMTP()
    smtpObj.connect("smtp.sina.com",25)
    print smtpObj.login(e,p)

def _formataddr(s):
    name, addr = parseaddr(s)
    encode = Header(name,'utf-8').encode()
    if isinstance(addr,unicode):
        addr = addr.encode('utf-8')
    return formataddr(( encode, addr ))

def send_mail(u,title,content):

    sender = conf.mail.sender
    smtphost = conf.mail.smtphost
    port = conf.mail.port
    password = conf.mail.password

    if isinstance(u,list):
        receivers = u
    else:
        receivers = [u]

    message = MIMEText(content, 'html', 'utf-8')
    message['From'] = _formataddr(sender)
    message['To'] =  _formataddr(u)

    subject = title 
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(smtphost,port)
        smtpObj.login(sender,password)
        smtpObj.sendmail(sender, receivers, message.as_string())
        lib.log.log("%s : 邮件发送成功" % (receivers))
    except smtplib.SMTPException:
        lib.log.log("Error : send error ")

if __name__ == "__main__":
    check_sina_email(sys.argv[1],sys.argv[2])
    check_sina_email("lemailtest@sina.com","1234qwer")

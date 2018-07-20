# -*- coding: utf-8 -*-
'''
Created on Jul 18, 2018

@author: Angela
'''
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from Lib.email.mime.multipart import MIMEMultipart
from Lib.email.mime.application import MIMEApplication

class Email:
    def send_email(self, latest_report, attach, now):
    # send server
        smtpserver = 'smtp.office365.com'
        user = 'aluo@bridge2solutions.com'
        password = 'Symbio123'
        sender = 'aluo@bridge2solutions.com'
        receiver = 'anjie.luo@symbio.com'
        
        subject = 'B2S Super Core Auto-Test Report'
        
        msg = MIMEMultipart()
        '''Open and read the latest report, then send report as main body of email'''
        f = open(latest_report, 'rb')
        content = f.read()
        f.close()
        text = MIMEText(content, 'html','utf-8')
        msg.attach(text)
        
        '''send attachments'''
        attHtml = MIMEText(content, 'html','utf-8')
        attHtml['Content-Type'] = 'application/octet-stream'
        attHtml.add_header('Content-Disposition', 'attachment', filename=('utf-8', '', now + "_test0.html"))
        msg.attach(attHtml)
        
        attTXT = MIMEApplication(open(attach, 'rb').read())
        attTXT['Content-Type'] = 'application/octet-stream'
        attTXT.add_header('Content-Disposition', 'attachment', filename=('utf-8', '', now + "_test0.txt"))
        msg.attach(attTXT)
        
        msg['subject'] = Header(subject, 'utf-8')
        msg['From'] = sender
        msg['To'] = receiver
        
        smtp = smtplib.SMTP()  
        smtp.connect(smtpserver)
        print('connected')
        smtp.starttls()
        smtp.login(user, password)
        print('login')
        smtp.sendmail(sender, receiver, msg.as_string())
        print('sended')
        smtp.quit()
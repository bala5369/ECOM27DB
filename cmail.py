mail_password='wzxy gham gcod kteu'
import smtplib
from email.message import EmailMessage
def send_mail(to,subject,body):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('balavardhan5369@gmail.com',mail_password)
    msg=EmailMessage()
    msg['From']='balavardhan5369@gmail.com'
    msg['To']=to
    msg['SUBJECT']=subject
    msg.set_content(body)
    server.send_message(msg)
    print('msg sent')
    server.close()
    
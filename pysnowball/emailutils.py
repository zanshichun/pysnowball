import smtplib
from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL

MAIL_HOST = "smtp.qq.com"
MAIL_USER = ""
MAIL_PASS = ""

MAIL_SENDER = ""

# 将每日盈亏情况发送到邮箱
def send_email_alert(recipient,ytdpl_val,purchased_val):
    MAIL_MESSAGE=MIMEText("较昨日盈亏：\t"+ytdpl_val+"\n"+"较购入盈亏值：\t"+purchased_val+"\n",'plain','utf-8')
    receivers = [recipient]
    try:
        smtpObj = SMTP_SSL(MAIL_HOST)
        smtpObj.ehlo(MAIL_HOST)
        # 登录到服务器
        smtpObj.login(MAIL_USER, MAIL_PASS)
        # 发送
        smtpObj.sendmail(MAIL_SENDER, receivers, MAIL_MESSAGE.as_string())
        # 退出
        smtpObj.quit()
        print('success')
        return True
    except smtplib.SMTPException as e:
        print('error', e)  # 打印错误
        return False
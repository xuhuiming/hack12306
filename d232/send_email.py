# coding=utf-8
import smtplib
from email.mime.text import MIMEText


def send_email():
	msg_from = '1142038555@qq.com'  # 发送方邮箱
	passwd = 'qhzunfdufjiffhha'  # 填入发送方邮箱的授权码
	msg_to = '1142038555@qq.com'  # 收件人邮箱

	subject = "抢到票了，快付钱"  # 主题
	content = "这是我使用pythonsmtplib及email模块发送的邮件"# 正文
	msg = MIMEText(content)
	msg['Subject'] = subject
	msg['From'] = msg_from
	msg['To'] = msg_to
	try:
	    s = smtplib.SMTP_SSL("smtp.qq.com", 465)# 邮件服务器及端口号
	    s.login(msg_from, passwd)
	    s.sendmail(msg_from, msg_to, msg.as_string())
	    print("发送成功")
	except s.SMTPException:
	    print("发送失败")
	finally:
	    s.quit()
# 这里调用函数的话引入的模块也会调用
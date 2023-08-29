import os
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv

s = smtplib.SMTP('smtp.gmail.com', 587)

#TLS 보안 시작
s.starttls()

load_dotenv()

#로그인 인증
s.login(os.getenv('GMAIL_ID'), os.getenv('GMAIL_PASSWORD'))

with open('test_result_today.txt', 'r') as file:
    file_context = file.read()

msg = MIMEText(file_context)
msg['Subject'] = '오늘 블로그 과제 확인 결과'

s.sendmail(os.getenv('GMAIL_ID'), os.getenv('GMAIL_ID'), msg.as_string())
s.quit()
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import date
from TeamF.mail import MAIL_FORMAT, STYLES

msg = MIMEMultipart('html')
msg['Subject'] = f'{date.today().strftime("%m/%d/%Y")}의 메일'
msg['From'] = 'myunghee1231@naver.com'
msg['To'] = 'lhs27733182@gmail.com'


mail_html = MAIL_FORMAT.format(
    STYLE=STYLES)
msg.attach(MIMEText(mail_html, 'html'))

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.ehlo()
    smtp.login('myunghee1231@naver.com', 'the1stme0102@!*')
    smtp.sendmail('myunghee1231@naver.com', 'myunghee1231@naver.com', msg.as_string())
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

host="smtp.gmail.com"
port=587
username="pratikshashah33@gmail.com"
password="utkarsha95"
from_email=username
to_list=["pratikshashah33@gmail.com"]

email_conn=smtplib.SMTP(host, port)
email_conn.ehlo()
email_conn.starttls()
email_conn.login(username, password)

the_msg=MIMEMultipart("alternative")
the_msg['Subject']="Hello there!"
the_msg["From"]=from_email

plain_txt="Testing the message"
html_txt="""\
<html>
  <head></head>
  <body>
   <p>Hey!<br>
    Testing this email <b>message</b>.Made by <a href='http://joincfe.com'>Team CEF</a>.
   </p>
  </body>
</html>
"""

part_1=MIMEText(plain_txt,'plain')
part_2=MIMEText(html_txt,"html")

the_msg.attach(part_1)
the_msg.attach(part_2)

print(the_msg.as_string())



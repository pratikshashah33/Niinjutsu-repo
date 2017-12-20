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
email_conn.sendmail(from_email,to_list,"Hello Pratiksha")
email_conn.quit()

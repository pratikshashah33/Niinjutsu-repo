from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import datetime

host="smtp.gmail.com"
port=587
username="pratikshashah33@gmail.com"
password="utkarsha95"
from_email=username
to_list=["pratikshashah33@gmail.com"]


class messageUser():
    message=[]
    user_details=[]
    email_messages=[]
    base_message="""Hi {name}!
    Thank you for the purchase on {date}
    We hope you are exicuted about usin it.Just as a
    remainder the purchase total was rs{total}
    Have a great one!

    Pratiksha
    """
    def set_detail(self,name,amount,email=None):
        name=name[0].upper()+name[1:].lower()
        amount="%.2f"%(amount)
        detail={
            "name":name,
            "amount":amount,
        }
        today=datetime.date.today()
        date_text='{today.month}/{today.day}/{today.year}'.format(today=today)
        detail['date']=date_text
        if email!=None:
            detail["email"]=email
            self.user_details.append(detail)
    def get_details(self):
        return self.user_details
    def make_messages(self):
        if len(self.user_details)>0:
            for detail in self.get_details():
                
                name=detail["name"]
                amount=detail["amount"]
                date=detail["date"]
                message=self.base_message
                new_message=message.format(
                    name=name,
                    date=date,
                    total=amount
                    )
                user_email=detail.get("email")
                if user_email:
                    user_data={
                        "email":user_email,
                        "message":new_message
                        }
                    self.email_messages.append(user_data)
                else:
                    self.message.append(new_message)
            return self.message
        return[]
    def send_email(self):
        self.make_messages()
        if len(self.email_messages) > 0:
            for detail in self.email_messages:
                user_email=detail["email"]
                user_messages=detail["message"]      
                try:
                    email_conn=smtplib.SMTP(host, port)
                    email_conn.ehlo()
                    email_conn.starttls()
                    email_conn.login(username, password)
                    the_msg=MIMEMultipart("alternative")
                    the_msg['Subject']="Hello there!"
                    the_msg["From"]=from_email
                    the_msg["To"]=to_list[0]
                    part_1=MIMEText(user_messages,'plain')
                    the_msg.attach(part_1)
                    print(the_msg.as_string)
                    email_conn.sendmail(from_email,to_list,the_msg.as_string())
                    email_conn.quit()
                except smtplib.SMTPException:
                    print("Error sending message")
            return True
        return False

obj=messageUser()
obj.set_detail("pratiksha",199,email="pratikshashah33@gmail.com")
obj.set_detail("iyor",231.898,email="pratikshashah33@gmail.com")
obj.set_detail("ghfg",6378.728,email="pratikshashah33@gmail.com")
obj.set_detail("yuebd",874.35,email="pratikshashah33@gmail.com")
obj.get_details()
obj.send_email()
#print(obj.make_messages())

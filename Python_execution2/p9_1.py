import datetime

class messageUser():
    message=[]
    user_details=[]
    base_message="""Hi {name}!
    Thank you for the purchase on {date}
    We hope you are exicuted about usin it.Just as a
    remainder the purchase total was rs{total}
    Have a great one!

    Pratiksha
    """
    def set_detail(self,name,amount):
        name=name[0].upper()+name[1:].lower()
        amount="%.2f"%(amount)
        detail={
            "name":name,
            "amount":amount,
        }
        today=datetime.date.today()
        date_text='{today.month}/{today.day}/{today.year}'.format(today=today)
        detail['date']=date_text
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
                return self.message
            return []
obj=messageUser()
obj.set_detail("pratiksha",199)
obj.set_detail("iyor",231.898)
obj.set_detail("ghfg",6378.728)
obj.set_detail("yuebd",874.35)
print(obj.get_details())

obj.make_messages()



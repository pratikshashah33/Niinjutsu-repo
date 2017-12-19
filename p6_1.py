default_names=["pratiksha","priyanka","shreya","utkarsha"]
default_amounts=[467.476,896.749,7685.5,454.56]
unf_message="""Hi {name}!
Thank you for the purchase on {date}.
We hope you are excited about using it.Just as a
remainder the purchase total was rs{total}.
Have a great one!
Pratiksha
"""
def make_messages(names,amounts):
    messages=[]
    if len(names)==len(amounts):
        i=0
        for name in names:
            new_amount="%.2f"%(amounts[i])
            new_msg=unf_message.format(
                    name=name,date='some date',
                    total=new_amount
                )
            i+=1
            print(new_msg)
make_messages(default_names,default_amounts)

import csv
import shutil
from tempfile import NamedTemporaryFile

def get_length(file_path):
    with open("data.csv","r") as csvfile:
        reader=csv.reader(csvfile)
        reader_list=list(reader)
        return len(reader_list)

def append_data(file_path,name,email):
    fieldnames=["id","name","email"]
    next_id=get_length(file_path)
    with open(file_path,"a") as csvfile:
        writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
        writer.writerow({
            "id":next_id,
            "name":name,
            "email":email,
            })

filename="data.csv"
temp_file=NamedTemporaryFile(delete=False)

with open(filename,"rb") as csvfile,temp_file:
    reader=csv.DictReader(csvfile)
    fieldnames=["id","name","email","amount","sent"]
    writer=csv.DictWriter(temp_file,fieldnames=fieldnames)
    #writer.writerheader()

    for row in reader:
        print(row)
        writer.writerow({
            "id":row["id"],
            "name":row["name"],
            "email":row["email"],
            "amount":"8712.763",
            "sent":"",
            })
shutil.move(temp_file.name,filename)
        
            

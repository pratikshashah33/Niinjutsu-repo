import csv

with open("data.csv","w+")as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(["Col 3","Col 4"])
    writer.writerow(["Data 5","Data 6"])


with open("data.csv","r") as csvfile:
    reader=csv.reader(csvfile)
    for row in reader:
        print(row)


with open("data.csv","a") as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(["Data 10","Data 11"])


with open("data.csv","r") as csvfile:
    reader=csv.reader(csvfile)
    for row in reader:
        print(row)




import csv
import os
with open('Python_CSV.csv','r') as file:
    csv_file=csv.reader(file)
    next(csv_file) #bo dong tieu de dau tien
    for row in csv_file:
        id,name,age,major,gpa=row  # row tra ve 1 tuple
        age=int(age)
        gpa=float(gpa)
        print("ID:{}, Name:{},Age:{},Major:{},GPA:{}".format(\
            id,name,age,major,gpa))
# doc file csv dung ten tieu de cot
with open('Python_CSV.csv','r') as file:
    csv_file=csv.DictReader(file, delimiter=',')
    for row in csv_file:
        print(row['GPA'])
# ghi file csv
csv_data_file='data_file.csv'
data=[[1,'Nguyen Van A',22,'CS',7.5],
[2,'Nguyen Van B',23,'CE',8.5],
[3,'Nguyen Van C',24,'CE',9.5],
[4,'Nguyen Van D',25,'CS',10.5],
[5,'Nguyen Van E',26,'CE',11.5]]
headers=['ID','Name','Age','Major','GPA']
print(os.getcwd())
with open(csv_data_file,'w',newline='', encoding='utf-8') as file:
    csv_writer=csv.writer(file,delimiter=',',
        quotechar='"',quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(headers)
    for row in data:
        csv_writer.writerow(row)
# canh c2:
csv_data_file2='data_file2.csv'
with open(csv_data_file2,'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=headers, delimiter=',',
        quotechar='"',quoting=csv.QUOTE_MINIMAL)
    writer.writeheader()
    for row in data:
        writer.writerow({
        headers[0]:row[0],\
        headers[1]:row[1],\
        headers[2]:row[2],\
        headers[3]:row[3],\
        headers[4]:row[4],\
        })
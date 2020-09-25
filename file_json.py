import json
with open('data_json.json','r') as file:
    data=json.load(file) #giai ma trong khi doc tiep json
print(data)

json_str='{"ID":1,"Name":"Nguyen Van C","Age":30,"Major":"CE","GPA":10.5}'
data2=json.loads(json_str)#giai ma chuoi json
print(data2)

#json writer
data={
    "ID":2,
    "Name":"Test",
    "Age":30,
    "Major":"CE",
    "GPA":11.5
}
with open('data_json.json','w')as file:
    json.dump(data, file, indent=4) #ma hoa chuoi duoc ghi trong file
    print(json.dumps(data, indent=4)) # ma hoa thanh ca doi tuong json
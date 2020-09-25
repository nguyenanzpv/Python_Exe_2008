import base64
if __name__=='__main__':
    message="this is python course"
    msg_bytes=message.encode('ascii')
    print('Message bytes: ',msg_bytes)
    base64_bytes=base64.b64encode(msg_bytes)
    print('base64 bytes: ',base64_bytes)
    base64_msg=base64.b64decode(base64_bytes)
    print('base64 msg: ',base64_msg)
    
# ma hoa nhi phan anh
with open('t3h.jpg','rb') as file:
    binary_file_data=file.read()
    base64_encode_data=base64.b64encode(binary_file_data)
    base64_msg=base64_encode_data.decode('utf-8')
print(base64_msg)

with open('t3h.txt','w') as file2:
    file2.write(base64_msg)

# cach 2
with open('t3h.txt','r') as file:
    data=file.readlines()
#bo cac khoang trang thua hay xuong dong
data=data[0].strip()
print(data)
base64_img_bytes=data.encode('utf-8')
with open('hinh_t3h.jpg','wb')as file3:
    decoded_img_data=base64.decodebytes(base64_img_bytes)
    file3.write(decoded_img_data)
    

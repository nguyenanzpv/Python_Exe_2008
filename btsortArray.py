number=int(input())
s=input()
list_input=[]
temp=[]
a=s.split()
stop1=0
stop2=0
stop3=0
for index in range(0,number):
    list_input.append(int(a[index]))
print(list_input)
temp=list_input.copy()
temp.sort()
print(temp)
for index in range(0,len(list_input)):
    if list_input[index]!=temp[index]:
        stop1=list_input[index]
        stop3=list_input[index+1]
        break
    print(stop1)
for z in range(len(list_input)-1,0,-1):
    if list_input[z]!=temp[z]:
        stop2=list_input[z]
        break
    print(stop2)
if stop2<=stop3:
    print("yes")
    print(stop1,stop2, end='')
    #print(stop2)

else:
    print("no")
        
        
       
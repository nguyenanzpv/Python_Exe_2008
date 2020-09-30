import sys

if __name__== '__main__':
    width=0
    height=0
    input_num= list(map(int, input().split()))
    if input_num[0] % input_num[2]==0:
        width=input_num[0]//input_num[2] #//chia lam tron phan nguyen xuong
    else:
        width=(input_num[0]//input_num[2])+1
    print('width {0}'.format(width))
    if input_num[1] % input_num[2]==0:
        height=input_num[1]//input_num[2]
    else:
        height=(input_num[1]//input_num[2])+1
    print('height {0}'.format(height))
    print(width+height)
    
    
def gt(number):
    if number==2:
        return 2*1
    else:
        return number * gt(number-1)

if __name__=='__main__':
    number=int(input())
    result=gt(number)
    print(result)
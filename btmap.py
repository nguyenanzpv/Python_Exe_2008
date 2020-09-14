# bai tap map and lamda
def fibonacci(number):
    # return a list of fibonacci numbers
    if number == 0:
        return []
    list_number = [0]
    for index in range(1, number + 1):
        if index == 1 or index == 2:
            list_number.append(1)
        else:
            value = list_number[index - 2] + list_number[index - 1]
            list_number.append(value)
    #print(list_number)
    return list_number

def binhphuong(listFibo):
    print(list(map(lambda x:x**3,listFibo)))

if __name__=='__main__':
    number=int(input())
    result=fibonacci(number)
    print(result)
    binhphuong(result)
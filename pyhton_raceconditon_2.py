import threading

# dung co che lock de bien x ko bi mat gia tri
# global variable x
x = 0

def increment():
    """
    function to increment global variable x
    """
    global x
    x += 1

def thread_task(lock):
    """
    task for thread
    calls increment function 100000 times.
    """
    for _ in range(100000):
        lock.acquire() #lock gia tri dang chay o thread lai ko cho thread khac dung
        increment()
        lock.release() # giai phong gia tri cho thread khac su dung

def main_task():
    global x
    # setting global variable x as 0
    x = 0

    # creating a lock
    lock = threading.Lock()

    # creating threads
    t1 = threading.Thread(target=thread_task, args=(lock,)) # co the truyen nhieu lock
    t2 = threading.Thread(target=thread_task, args=(lock,))

    # start threads
    t1.start()
    t2.start()

    # wait until threads finish their job
    t1.join()
    t2.join()
    
    # tao 2 thread nen ket qua la tang 200000 du chay lap 10 lan

if __name__ == "__main__":
    for i in range(10):
        main_task()
        print("Iteration {0}: x = {1}".format(i,x))
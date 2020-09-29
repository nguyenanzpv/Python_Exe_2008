# vi du 4: su dung processpool de quan ly multiprocessing
import multiprocessing
import concurrent.futures
import time

def do_something(seconds):
    print(f'Sleeping {seconds} seconds')
    time.sleep(seconds)
    return f'Done sleeping...{seconds}'
def main():
    start=time.perf_counter()
    processer = []
    with concurrent.futures.ProcessPoolExecutor() as excuter:
        results=[excuter.submit(do_something,1) for _ in range(10)] #1 la so giay tryen vao do_something
        for result in concurrent.futures.as_completed(results):
            print(result.result())
    finish=time.perf_counter()
    print(f'Finished4 in {round(finish-start,2)} second(s)')

# vi du khac dung map de gon code
import multiprocessing
import concurrent.futures
import time

def do_something2(seconds):
    print(f'Sleeping map {seconds} seconds')
    time.sleep(seconds)
    return f'Done sleeping map...{seconds}'
def main2():
    start=time.perf_counter()
    processer = []
    with concurrent.futures.ProcessPoolExecutor() as excuter:
        seconds=[5,4,3,2,1]
        results=excuter.map(do_something2,seconds)
        for result in results:
            print(result)
    finish=time.perf_counter()
    print(f'Finished5 in {round(finish-start,2)} second(s)')

if __name__=='__main__':
    main2()
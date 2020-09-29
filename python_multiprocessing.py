import multiprocessing
import time

start=time.perf_counter()

def do_something():
    print('Sleeping  1 seconds')
    time.sleep(1)
    print('Done sleep')
    
process_1=multiprocessing.Process(target=do_something) #tao ra 1 thread moi
process_2=multiprocessing.Process(target=do_something) #tao ra 1 thread moi

process_1.start()
process_2.start()

process_1.join() #yeu cau process_1 cho process_2 chay xong moi ket thuc -> dam bao process_1 chay nhanh hon process_2 cung ko bi ket thuc
process_2.join()

finish=time.perf_counter()

print(f'Finished in {round(finish-start,2)} second(s)')

# vi du 2:
start2=time.perf_counter()

def do_something():
    print('Sleeping  1 seconds')
    time.sleep(1)
    print('Done sleep')
 
# chuong trinh chay 1 lan roi doi 1 phut sau moi chay tiep lan 2   
for _ in range(10):
    process=multiprocessing.Process(target=do_something)
    process.start()
    process.join()
    
finish2=time.perf_counter()
print(f'Finished2 in {round(finish2-start2,2)} second(s)')

# vi du 3: fix cho vi du 2
start3=time.perf_counter()

def do_something():
    print('Sleeping  1 seconds')
    time.sleep(1)
    print('Done sleep')
 
# chuong trinh chay 1 lan roi doi 1 phut sau moi chay tiep lan 2
# fix no se start cung 1 luc
processer = []
for _ in range(10):
    process=multiprocessing.Process(target=do_something)
    process.start()
    processer.append(process)
    
for process in processer:
    process.join()
    
finish3=time.perf_counter()
print(f'Finished3 in {round(finish3-start3,2)} second(s)')






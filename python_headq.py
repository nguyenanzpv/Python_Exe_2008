import heapq
import sys

if __name__=='__main__':
    while True:
        num_numbers=int(input())
        if(num_numbers==0):
            sys.exit()
        heap=list(map(int,input().split()))
        heapq.heapify(heap)
        cost=0
        #print(len(heap))
        while len(heap)>0:
            first=heapq.heappop(heap) # lay phan tu nho nhat ra
            second=heapq.heappop(heap)
            cost += first+second            
            heapq.heappush(heap,first+second) #nhet ket qua cong vao heap
            print(cost)
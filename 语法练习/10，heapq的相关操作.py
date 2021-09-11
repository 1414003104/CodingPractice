import heapq as hp

pqueue=[]
hp.heappush(pqueue,(1,'A'))
hp.heappush(pqueue,(7,'B'))
hp.heappush(pqueue,(3,'C'))

print(hp.heappop(pqueue))
print(hp.heappop(pqueue))
print(hp.heappop(pqueue))
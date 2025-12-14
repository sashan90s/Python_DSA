# in this file, we will learn to use heap and list comprehension in python

import heapq


# how to push into heap
minHeap = []

heapq.heappush(minHeap, 3)
heapq.heappush(minHeap, 1)
heapq.heappush(minHeap, 2)
print(minHeap) # [1, 3, 2]

while minHeap:
    print(heapq.heappop(minHeap))

# output: 
# 1
# 2 
# 3

#OfflineClass



# for teacihng in live class #LiveClass
minHeap2 = []
for i in [5,1,4,6,0,7,9,3,4,2]: 
     heapq.heappush(minHeap2,i)
print(minHeap2) # [0, 1, 4, 3, 2, 7, 9, 6, 4, 5]


print("popping elements smallest to largest")
while minHeap2:
     print(heapq.heappop(minHeap2))

# now what if you want the ascending, largest to smallest
# Pushing elements from one heap to the other
print("push smallest to get largest")

minHeap3 = []
for i in [5,1,4,6,0,7,9,3,4,2]: 
     heapq.heappush(minHeap3, -1*i)
print(minHeap3, "this is minHeap3)")


list_comp = [heapq.heappop(minHeap3)* -1 for i in range(len(minHeap3))]



# list_comp_test = [heapq.heappop(minHeap3)* -1 for i in minHeap3] -- this is a problem, length is evaluated again and again
# we will explain this later. `For i in items ` should not be paired with any type of pop functions. 

# what is another way of writing this list comprehension?

# list_test = []
# for i in range(len(minHeap3)):
#      list_test.append(heapq.heappop(minHeap3)*-1)

print(list_comp)
# print(list_comp_test)

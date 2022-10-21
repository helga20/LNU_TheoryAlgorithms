'''import time
from random import *

n = int(input("Введіть n: "))
mylist = []
for i in range(0, n):
    mylist.append(randint(0, n))
print("Масив:", mylist)

start_time = time.time()
s = {}
for i in mylist:
    if i not in s:
        s[i] = s.get(i, 0)
    if i in s:
        s[i] = s.get(i, 0) + 1

d = {}
for key,val in s.items():
    d[val] = key
end_time = time.time() - start_time
print("Час:", end_time)
print("Макс. к-сть однакових елем.: ", max(d))'''




'''
from random import randint
import time

def max_ident_elem(arr, n): 
    counter = 0 #1
    for i in arr: #n-2
        temp = 0 #1
        for j in arr: 
            if i == j: #1
                temp += 1 #1
        if (temp > counter): #1
            counter = temp #1
    return counter #1
n = int(input("Введіть n: "))
arr = [randint(0, n) for i in range(n)]
print(arr)
start_time = time.time()
print("Макс. к-сть однак. елем.: ", max_ident_elem(arr, n))
end_time = time.time() - start_time
print("Час:", end_time)
'''








from random import randint
import time
#3n^2 + 3n + 2
def max_ident_elem(arr): 
    counter = 0 #1
    for i in arr: #n*(1+n*(1+2)+1+1)
        temp = 0 #1
        for j in arr: #n
            if i == j: #1
                temp += 1 #2
        if (temp > counter): #1
            counter = temp #1
    return counter #1
n = int(input("Введіть n: "))
arr = [randint(0, n) for i in range(n)]
print(arr)
start_time = time.time()
print("К-сть однак.: ", max_ident_elem(arr))
end_time = time.time() - start_time
print("Час:", end_time)



















'''from random import randint
#import time
def max_ident_elem(arr, n):
    counter = 1  
    for i in range(1, n):
        j = 0
        for j in range(1):
            if arr[i] == arr[j]:
                j += 1
        if i == j + 1:
            counter +=1
    return counter
n = int(input("Введіть n: "))
arr = [randint(0, n) for i in range(n)]
#start_time = time.time()
print(arr)
print("Максимальна к-сть однакових елем.: ", max_ident_elem(arr, n))
#end_time = time.time() - start_time
#print("Час:", end_time)'''











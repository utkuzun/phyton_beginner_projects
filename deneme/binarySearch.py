import random
import time


length = 500

liste = set()

while len(liste) < length:

    liste.add(random.randint(-3*length, 3*length)) 

liste = sorted(liste)



def naive_search(l, target):

    for mem in range(len(liste)):
        if l[mem] == target:
            return mem
    return -1


def binary_search(l, target, low=None, high=None):

    if low is None:
        low = 0

    if high is None:
        high = len(l)-1
    
    if high < low:
        return -1

    medium = (low + high) // 2

    if l[medium] == target:
        return medium
    elif l[medium] > target:
        return binary_search(l, target, low, medium -1)
    else:
        return binary_search(l, target, medium + 1, high)


start = time.time()
for mem in liste:
    naive_search(liste, mem)
end = time.time()

print("naive time is " + str(end - start))


start = time.time()
for mem in liste:
    binary_search(liste, mem)
end = time.time()

print("binary time is " + str(end - start))


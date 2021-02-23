import random
import time

def naive_search(l, target):

    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1


def binary_search(l, target, low=None, high=None):
    if low == None:
        low = 0
    if high == None:
        high = len(l) - 1

    if low > high:
        return -1

    midpoint = (high + low) // 2

    if l[midpoint] == target:
        return midpoint

    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint - 1)

    if target > l[midpoint]:
        return binary_search(l, target, midpoint +1 , high)

    


if __name__ == "__main__":
    # l =[2, 5, 6, 8, 87]

    # print(naive_search(l,5))
    # print(binary_search(l, 5))

    length = 1000
    random_list = [random.randint(-3*length,3*length) for i in range(length)]
    sorted_list = sorted(random_list)


    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()

    print("Naive Search done in " + str(end - start) + " seconds")

    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()

    print(" Binary Search done in " + str(end - start) + " seconds")


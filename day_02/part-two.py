lines = open('day_02/input.txt', "r").read().split('\n')

def allIncreaseOrDecrease(lst : list):
    arr = lst.copy()
    arr.sort()
    return lst==list(reversed(arr)) or lst == arr


def hasDuplicates(lst : list):
    return len(lst) != len(set(lst))


def maxGap(lst : list):
    result = 0
    for i in range(len(lst)-1):
        gap = abs(lst[i+1]-lst[i])
        if gap > result:
            result = gap
    return result


def myCheck(lst: list):
    return allIncreaseOrDecrease(lst) and maxGap(lst) <= 3 and not hasDuplicates(lst)


result = 0

for line in lines:
    lst = line.split(' ')
    lst = list(map(int, lst))
    if myCheck(lst):
        result += 1
    else:
        anyMatch = False
        for i in range(len(lst)):
            lstCopy = lst.copy()
            del lstCopy[i]
            if(myCheck(lstCopy)):
                anyMatch = True
        if anyMatch:
            result += 1

print(result)
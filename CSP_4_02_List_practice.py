
def bookends(li):
    first = li.pop(0)
    last = li.pop()
    return [first, last]


def inOrder(li):
    return li == sorted(li)


def find(li, target):
    for i in range(len(li)):
        if li[i] == target:
            return i
    return -1


def removeLowest(li):
    lowest = li[0]
    for num in li:
        if num < lowest:
            lowest = num
    li.remove(lowest)


def keepOrder(li, value):
    for i in range(len(li)):
        if value <= li[i]:
            li.insert(i, value)
            return
    li.append(value)


def merge(l1, l2):
    merged = []
    i = 0
    j = 0

    while i < len(l1) or j < len(l2):
        if j == len(l2) or (i < len(l1) and l1[i] <= l2[j]):
            merged.append(l1[i])
            i += 1
        else:
            merged.append(l2[j])
            j += 1

    return merged
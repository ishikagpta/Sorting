# -----------  Bubble Sort  -----------
def bubble_sort(list_a):
    for i in range(len(list_a)):
        for j in range(len(list_a) - 1):
            if list_a[j] > list_a[j + 1]:
                list_a[j], list_a[j + 1] = list_a[j + 1], list_a[j]

# -----------  Insertion Sort  -----------


def insertion_sort(list_a):
    for i in range(1, len(list_a)):
        key = list_a[i]
        j = i - 1
        while j >= 0 and key < list_a[j]:
            list_a[j + 1] = list_a[j]
            j -= 1
        list_a[j + 1] = key

# -----------  Merge Sort  -----------


def merge(inList, first, mid, last):
    size = last - first + 1
    tempList = [0] * size
    first1 = first
    last1 = mid
    first2 = mid + 1
    last2 = last
    index = 0
    while first1 <= last1 and first2 <= last2:
        if inList[first1] < inList[first2]:
            tempList[index] = inList[first1]
            first1 += 1
        else:
            tempList[index] = inList[first2]
            first2 += 1
        index += 1
    while first1 <= last1:
        tempList[index] = inList[first1]
        first1 += 1
        index += 1
    while first2 <= last2:
        tempList[index] = inList[first2]
        first2 += 1
        index += 1
    for index in range(size):
        inList[first] = tempList[index]
        first += 1


def merge_sort_rec(inList, first, last):
    if first < last:
        mid = (first + last) // 2
        merge_sort_rec(inList, first, mid)
        merge_sort_rec(inList, mid + 1, last)
        merge(inList, first, mid, last)


def merge_sort(inList):
    last = len(inList) - 1
    merge_sort_rec(inList, 0, last)


# -----------  Iterative Merge Sort  -----------

def merge_iterative(inList, temp, frm, mid, to):
    k = frm
    i = frm
    j = mid + 1
    while i <= mid and j <= to:
        if inList[i] < inList[j]:
            temp[k] = inList[i]
            i = i + 1
        else:
            temp[k] = inList[j]
            j = j + 1
        k = k + 1
    while i < len(inList) and i <= mid:
        temp[k] = inList[i]
        k = k + 1
        i = i + 1
    for i in range(frm, to + 1):
        inList[i] = temp[i]


def iterative_merge_sort(inList):
    low = 0
    high = len(inList) - 1
    temp = inList.copy()
    m = 1
    while m <= high - low:
        for i in range(low, high, 2 * m):
            frm = i
            mid = i + m - 1
            to = min(i + 2 * m - 1, high)
            merge_iterative(inList, temp, frm, mid, to)
            temp, inList = inList, temp
        m = 2 * m


# -----------  Quick Sort  -----------


def insertionSortPartialList(inList, first, last):
    for place in range(first + 1, last):
        temp = inList[place]
        i = place
        while i > 0 and inList[i - 1] > temp:
            inList[i] = inList[i - 1]
            i = i - 1
        inList[i] = temp


def quickSortRec(inList, first, last):
    if last - first < 4:
        insertionSortPartialList(inList, first, last)
        return
    mid = (first + last) // 2
    if inList[first] > inList[last]:
        inList[first], inList[last] = inList[last], inList[first]
    if inList[first] > inList[mid]:
        inList[first], inList[mid] = inList[mid], inList[first]
    if inList[mid] > inList[last]:
        inList[mid], inList[last] = inList[last], inList[mid]
    pivot = inList[mid]
    inList[last - 1], inList[mid] = inList[mid], inList[last - 1]
    left = first + 1
    right = last - 2
    done = False
    while not done:
        while inList[left] < pivot:
            left += 1
        while inList[right] > pivot:
            right -= 1
        if right > left:
            inList[left], inList[right] = inList[right], inList[left]
            left += 1
            right -= 1
        else:
            done = True
    inList[left], inList[last - 1] = inList[last - 1], inList[left]
    quickSortRec(inList, first, left - 1)
    quickSortRec(inList, left + 1, last)


def quick_sort(inList):
    quickSortRec(inList, 0, len(inList) - 1)

# -----------  Shell Sort  -----------


def shell_sort(inList):
    size = len(inList)
    gap = size // 2
    while gap > 0:
        for i in range(gap, size):
            temp = inList[i]
            j = i
            while j >= gap and temp < inList[j - gap]:
                inList[j] = inList[j - gap]
                j -= gap
            inList[j] = temp
        if gap == 2:
            gap = 1
        else:
            gap = int(gap / 2.2)
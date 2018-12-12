from time import time


def mergeSort(l):
    recursiveMergeSort(l, 0, len(l) - 1)


def recursiveMergeSort(l, left, right):
    if left >= right:
        return

    mid = int((left + right) / 2)

    recursiveMergeSort(l, left, mid)
    recursiveMergeSort(l, mid + 1, right)
    mergePartitions(l, left, mid, right)


def mergePartitions(l, left, mid, right):
    idLeft = left
    idRight = mid + 1
    tempList = []

    while True:
        if l[idLeft] < l[idRight]:
            tempList.append(l[idLeft])
            idLeft += 1

            if idLeft > mid:  # first subsequence ended. Thus lets copy the remaining elements from the right partition.
                for v in l[idRight:right + 1]:
                    tempList.append(v)
                break  # termitates the while loop

        else:  # Symmetric
            tempList.append(l[idRight])
            idRight += 1

            if idRight > right:  # second subsequence ended. Thus lets copy the remaining elements from the left partition.
                for v in l[idLeft:mid + 1]:
                    tempList.append(v)
                break  # termitates the while loop

    # Update the list with the computed ordered elements
    for i in range(left, right + 1):
        l[i] = tempList[i - left]


if __name__ == "__main__":
    l = list(range(600))
    start = time()
    mergeSort(l)
    end = time() - start
    print(end)

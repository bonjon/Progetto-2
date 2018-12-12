import sys
import random
import mergesort
from time import time

sys.setrecursionlimit(10000000)


def Quicksort(l, k, m):
    if len(l) <= 2:
        l.sort()
        return l
    c = medIndex(l, sampleMedianSelect(l, k, m))  # prendo l'indice del mediano
    l[0], l[c] = l[c], l[0]  # scambio il mediano con il primo elemento
    quickSortRicorsivo(l, 0, len(l) - 1)
    return (l)


def quickSortRicorsivo(l, i, f):
    if i >= f:
        return
    m = partitionQuick(l, i, f)
    quickSortRicorsivo(l, i, m - 1)
    quickSortRicorsivo(l, m + 1, f)


def partitionQuick(l, i, f):
    x = l[i]
    inf = i
    sup = f + 1
    while True:
        inf += 1
        while inf <= f and l[inf] <= x:
            inf += 1
        sup -= 1
        while l[sup] > x:
            sup -= 1

        if inf < sup:
            l[inf], l[sup] = l[sup], l[inf]
        else:
            break

    l[i], l[sup] = l[sup], l[i]
    return sup


def sottoinsieme(l, m):
    i = 0
    v = []
    index = []
    while (i < m):
        h = random.randint(0, len(l) - 1)
        if h not in index:
            v.append(l[h])
            index.append(h)
            i += 1
    return v


def sampleMedianSelect(l, k, m):
    if len(l) <= m:
        mergesort.mergeSort(l)
        return (l[k])
    else:
        V = sottoinsieme(l, m)
        x = sampleMedianSelect(V, int(len(V) / 2), m)
        A1 = []
        A2 = []
        A3 = []
        for i in range(len(l)):
            if l[i] < x:
                A1.append(l[i])
            elif l[i] == x:
                A2.append(l[i])
            else:
                A3.append(l[i])
        if k <= len(A1) - 1:
            return sampleMedianSelect(A1, k, m)
        elif k > (len(A1) + len(A2)) - 1:
            return sampleMedianSelect(A3, k - len(A1) - len(A2), m)
        else:
            return x


def medIndex(l, h):
    for i in range(0, len(l) - 1):
        if l[i] == h:
            return i


if __name__ == "__main__":
    L = list(range(10000))
    print(L)
    start = time()
    Quicksort(L, int(len(L) / 2), 10)
    end = time() - start
    print("Time --->", end)

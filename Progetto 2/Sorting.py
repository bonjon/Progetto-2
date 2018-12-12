# coding: utf-8 

from HeapMax import HeapMax
from __init__ import printSwitch
import random
from time import time
from math import ceil


def trivialSelect(l, k):
    if printSwitch.dumpOperations:
        print("trivialSelect of ", str(l), "with k", str(k))

    length = len(l)
    if k <= 0 or k > length:
        return None

    for i in range(0, k):
        minimum = i
        for j in range(i + 1, length):
            if l[j] < l[minimum]:
                minimum = j
        l[minimum], l[i] = l[i], l[minimum]

    if printSwitch.dumpOperations:
        print("   L'elemento nella posizione cercata: ", l[k - 1])
    return l[k - 1]


def quickSelectDet(l, k, minLen, whoami="QuickSelectDet"):
    if k <= 0 or k > len(l):
        return None
    return recursiveQuickSelectDet(l, 0, len(l) - 1, k, minLen, whoami)


def recursiveQuickSelectDet(l, left, right, k, minLen, whoami):
    if printSwitch.dumpOperations:
        condOutput(whoami, "recursiveQuickSelectDet({},{},{},{})".format(left, right, k,
                                                                         minLen) + "\n" + "[" + "- " * left + str(
            l[left:right + 1])[1:-1] + "- " * (len(l) - right - 1) + "]")

    if left == right:
        return l[left]

    # si usa stop per decidere quando smettere di ricorrere ed utilizzare un algoritmo diverso
    if len(l) < minLen:
        med = trivialSelect(l[left: right + 1], k - left)
        if printSwitch.dumpOperations:
            condOutput(whoami, "return:" + str(med))
        return med

    # compute groups of five
    numElem = right - left + 1
    numGroups = int(ceil(numElem / 5.0))
    median = []
    for i in range(0, numGroups):
        dimGroup = 5 if (i < numGroups - 1 or numElem % 5 == 0) \
            else (numElem - (numGroups - 1) * 5)
        a = left + i * 5
        b = left + i * 5 + dimGroup - 1

        if printSwitch.dumpOperations:
            condOutput(whoami, "dimGroup: " + str(dimGroup) + "\n" + "Compute median in group {}".format(l[a:b + 1]))
        m = trivialSelect(l[a:b + 1], int(ceil(dimGroup / 2.0)))
        median.append(m)

    if printSwitch.dumpOperations:
        condOutput(whoami, "Compute the median of " + str(median))

    vperno = quickSelectDet(median, ceil(len(median) / 2), minLen,
                            "Median Recursion on list {}".format(median))  # vperno è un valore e non un indice

    if printSwitch.dumpOperations:
        condOutput(whoami, "Partitioning wrt " + str(vperno))

    perno = partitionDet(l, left, right,
                         vperno)  # Watch: this is a new function which takes the pivot as the parameter

    posperno = perno + 1
    if posperno == k:
        if printSwitch.dumpOperations:
            condOutput(whoami, "return " + str(l[perno]))
        return l[perno]
    if posperno > k:
        if printSwitch.dumpOperations:
            condOutput(whoami, "Recursion on the LEFT partition.")
        return recursiveQuickSelectDet(l, left, perno - 1, k, minLen, whoami)
    else:
        if printSwitch.dumpOperations:
            condOutput(whoami, "Recursion on the RIGHT partition.")
        return recursiveQuickSelectDet(l, perno + 1, right, k, minLen, whoami)


def partitionDet(l, left, right, pivot):
    # nota: pivot è un valore dell'array l e non un indice!
    inf = left
    sup = right

    while True:
        while inf <= right and l[inf] <= pivot:
            if l[inf] == pivot and l[left] != pivot:
                l[left], l[inf] = l[inf], l[left]
            else:
                inf += 1

        while sup >= 0 and l[sup] > pivot:
            sup -= 1

        if inf < sup:
            l[inf], l[sup] = l[sup], l[inf]
        else:
            break

    l[left], l[sup] = l[sup], l[left]

    # if printSwitch.dumpOperations:
    #    print("- "*left + str(l[left:right + 1]) + " -"*(len(l) - right - 1))

    return sup


def quickSelectRand(l, k):  # k 1...n
    if k <= 0 or k > len(l):
        return None
    return recursiveQuickSelectRand(l, 0, len(l) - 1, k)


def recursiveQuickSelectRand(l, left, right, k):
    if printSwitch.dumpOperations:
        print("recursiveQuickSelectRand({},{},{})".format(left, right, k))

    if left > right:  # controllo superfluo
        return

    if left == right and k - 1 == left:
        return l[k - 1]

    mid = partition(l, left, right)
    if printSwitch.dumpOperations:
        print("mid: {}".format(mid))

    if k - 1 == mid:
        return l[mid]
    if k - 1 < mid:
        return recursiveQuickSelectRand(l, left, mid - 1, k)
    else:
        return recursiveQuickSelectRand(l, mid + 1, right, k)


def selectionSort(l):
    """ It sorts the given Python list in ascending order.
        The key idea is that at the k-th step, you put the the right element in position k.
        O(n^2)
    """
    for k in range(len(l) - 1):

        min_pos = k
        for j in range(k + 1, len(l)):
            if l[j] < l[min_pos]:
                min_pos = j

        l[min_pos], l[k] = l[k], l[min_pos]  # multiple assignment to avoid tmp var


def insertionSortDown(l):
    """ It sorts the given Python list in ascending order.
           Scan the list from the index k=1 to the end; assume the list is ordered before index k;
           at the k-th step, put the k-th element to the right position among the previous ones (from 0 to k-1).
           O(n^2)
       """
    for k in range(1, len(l)):

        if printSwitch.dumpOperations:
            print("scanning position {}".format(k))

        val = l[k]
        for pos in range(k):
            if l[pos] > val:

                if printSwitch.dumpOperations:
                    print("\t{}>{}".format(l[pos], val))
                break

        else:  # if I don't find that l[pos] > val
            pos = k  # This value for pos is just a flag to remember that from 0 to k, the list is already ordered
            if printSwitch.dumpOperations:
                print("From 0 to {}, everything is already ordered.".format(k))

        if pos < k:  # pos==k if no pos<k exists s.t. l[pos]>val. Do nothing, and continue from k+1.
            for j in range(k, pos, -1):
                l[j] = l[j - 1]
            l[pos] = val
            if printSwitch.dumpOperations:
                print("Shift to right and set l[{}]={}: ".format(pos, l[pos]) + str(l[:k + 1]))


def insertionSortUp(l):
    """ It sorts the given Python list in ascending order.
        Like insertionSortDown, but processing elements from right to left.
        O(n^2)
    """
    for k in range(1, len(l)):
        if printSwitch.dumpOperations:
            print("scanning position {}".format(k))

        val = l[k]
        for pos in range(k - 1, -1, -1):

            if printSwitch.dumpOperations:
                print("pos=", pos)

            if l[pos] <= val:
                if printSwitch.dumpOperations:
                    print("\t{}<={}".format(l[pos], val))
                break
        else:
            pos = -1  # Thus val is the minimum value in the first k positions.

        if pos < k - 1:

            for j in range(k, pos + 1, -1):
                l[j] = l[j - 1]
            l[pos + 1] = val

            if printSwitch.dumpOperations:
                print("Shift to right and set l[{}]={}: ".format(pos + 1, l[pos + 1]) + str(l[:k + 1]))
        else:
            if printSwitch.dumpOperations:
                print("From 0 to {}, everything is already ordered.".format(k))


def bubbleSort(l):
    """ Iteratively process all the list, swapping elements in the wrong positions. Once no swappings are necessary, the list is ordered.
    O(n^2)
    """
    swapped = True
    while swapped:
        swapped = False

        if printSwitch.dumpOperations:
            print(l)

        for j in range(len(l) - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
                swapped = True

                if printSwitch.dumpOperations:
                    print("Swap {} with {}".format(l[j + 1], l[j]))


def quickSort(l, det=False):
    recursiveQuickSort(l, 0, len(l) - 1, det)


def recursiveQuickSort(l, left, right, det=False):
    if printSwitch.dumpOperations:
        print("recursiveQuickSort({},{})".format(left, right))

    if left >= right:
        return

    mid = partition(l, left, right, det)
    recursiveQuickSort(l, left, mid - 1, det)
    recursiveQuickSort(l, mid + 1, right, det)

    if printSwitch.dumpOperations:
        print("- " * left + str(l[left:right + 1]) + " -" * (len(l) - right - 1))


def partition(l, left, right, det=False):
    inf = left
    sup = right + 1

    if not det:
        random.seed(1)
        mid = random.randint(left, right)
        l[left], l[mid] = l[mid], l[left]  # exchange first elem with the randomically chosen one

    mid = left  # the median is the first elem of the array

    if printSwitch.dumpOperations:
        print("Selected median:", l[mid])

    while True:
        inf += 1
        while inf <= right and l[inf] <= l[mid]:
            inf += 1

        sup -= 1
        while l[sup] > l[mid]:
            sup -= 1

        if inf < sup:
            l[inf], l[sup] = l[sup], l[inf]
        else:
            break

    l[mid], l[sup] = l[sup], l[mid]

    if printSwitch.dumpOperations:
        print("- " * left + str(l[left:right + 1]) + " -" * (len(l) - right - 1))

    return sup


def heapSort(l):
    """ L'heapSort segue la tecnica del selectionSort, ma utilizza una struttura dati piu' efficiente per l'estrazione del massimo: gli Heap.
        Si ricorda che un hep e' un albero binario che gode delle seguenti proprieta':
        - e' completo fino al penultimo livello
        - nei nodi dell'albero sono memorizzati gli elementi della collezione
        - chiave(padre(v)) > chiave(v) per ogni nodo v
    """
    heap = HeapMax(l);

    if printSwitch.dumpOperations:
        print("HEAPIFY")
    heap.heapify();  # costruisce l'heap
    if printSwitch.dumpOperations:
        print(heap.heap)

    if printSwitch.dumpOperations:
        print("SORTING")

    while not heap.isEmpty():  # finchè l'heap non è vuoto cancella il massimo, ordinando così gli elementi in modo crescente
        if printSwitch.dumpOperations:
            print("deleteMax()")
        heap.deleteMax()  # ATTENZIONE: per come implementata la deleteMax, nessun elemento viene realmente cancellato dalla lista passata in
        # argomento a HeapMax, ma spostato in fondo. Otteniamo un ordinamento crescente.
        if printSwitch.dumpOperations:
            print(heap.heap)


if __name__ == "__main__":
    l = list(range(1000))

    # selectionSort(l)
    # insertionSortUp(l)
    start = time()
    # bubbleSort(l)
    # quickSelectDet(l, 500, 5)
    # quickSort(l)
    # heapSort(l)
    end = time() - start
    print(end)
    print(l)

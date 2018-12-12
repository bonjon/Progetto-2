import Codice
import Sorting
from time import time
import mergesort


def test1(l):
    start = time()
    # Sorting.heapSort(l[0:10])
    # mergesort.mergeSort(l[0:10])
    # Sorting.bubbleSort(l[0:10])
    # Sorting.insertionSortUp(l[0:10])
    # Sorting.quickSort(l[0:10])
    # Sorting.selectionSort(l[0:10])
    # v=l[0:10]
    # v.sort()
    # Sorting.quickSelectRand(l[0:10],5)
    # Sorting.quickSelectDet(l[0:10],5,5)
    Codice.Quicksort(l[0:10], 5, 5)
    end = time() - start
    print("Primo tempo 10 elementi", end)

    start = time()
    # Sorting.heapSort(l[0:100])
    # mergesort.mergeSort(l[0:100])
    # Sorting.bubbleSort(l[0:100])
    # Sorting.insertionSortUp(l[0:100])
    # Sorting.quickSort(l[0:100])
    # Sorting.selectionSort(l[0:100])
    # v=l[0:100]
    # v.sort()
    # Sorting.quickSelectRand(l[0:100],50)
    # Sorting.quickSelectDet(l[0:100], 50, 5)
    Codice.Quicksort(l[0:100], 50, 5)
    end = time() - start
    print("Secondo tempo 100 elementi", end)

    start = time()
    # Sorting.heapSort(l[0:200])
    # mergesort.mergeSort(l[0:200])
    # Sorting.bubbleSort(l[0:200])
    # Sorting.insertionSortUp(l[0:200])
    # Sorting.quickSort(l[0:200])
    # Sorting.selectionSort(l[0:200])
    # v=l[0:200]
    # v.sort()
    # Sorting.quickSelectRand(l[0:200],100)
    # Sorting.quickSelectDet(l[0:200],100, 5)
    Codice.Quicksort(l[0:200], 100, 5)
    end = time() - start
    print("Terzo tempo 200 elementi", end)

    start = time()
    # Sorting.heapSort(l[0:300])
    # mergesort.mergeSort(l[0:300])
    # Sorting.bubbleSort(l[0:300])
    # Sorting.insertionSortUp(l[0:300])
    # Sorting.quickSort(l[0:300])
    # Sorting.selectionSort(l[0:300])
    # v=l[0:300]
    # v.sort()
    # Sorting.quickSelectRand(l[0:300],150)
    # Sorting.quickSelectDet(l[0:300], 150, 5)
    Codice.Quicksort(l[0:300], 150, 5)
    end = time() - start
    print("Quarto tempo 300 elementi", end)

    start = time()
    # Sorting.heapSort(l[0:400])
    # mergesort.mergeSort(l[0:400])
    # Sorting.bubbleSort(l[0:400])
    # Sorting.insertionSortUp(l[0:400])
    # Sorting.quickSort(l[0:400])
    # Sorting.selectionSort(l[0:400])
    # v=l[0:400]
    # v.sort()
    # Sorting.quickSelectRand(l[0:400],200)
    # Sorting.quickSelectDet(l[0:400], 200, 5)
    Codice.Quicksort(l[0:400], 200, 5)
    end = time() - start
    print("quinto tempo 400 elementi", end)

    start = time()
    # Sorting.heapSort(l[0:500])
    # mergesort.mergeSort(l[0:500])
    # Sorting.bubbleSort(l[0:500])
    # Sorting.insertionSortUp(l[0:500])
    # Sorting.quickSort(l[0:500])
    # Sorting.selectionSort(l[0:500])
    # v=l[0:500]
    # v.sort()
    # Sorting.quickSelectRand(l[0:500],250)
    # Sorting.quickSelectDet(l[0:500], 250, 5)
    Codice.Quicksort(l[0: 500], 250, 5)
    end = time() - start
    print("Sesto tempo 500 elementi", end)

    start = time()
    # Sorting.heapSort(l[0:600])
    # mergesort.mergeSort(l[0:600])
    # Sorting.bubbleSort(l[0:600])
    # Sorting.insertionSortUp(l[0:600])
    # Sorting.quickSort(l[0:600])
    # Sorting.selectionSort(l[0:600])
    # v=l[0:600]
    # v.sort()
    # Sorting.quickSelectRand(l[0:600],300)
    # Sorting.quickSelectDet(l[0:600], 300, 5)
    Codice.Quicksort(l[0: 600], 300, 5)
    end = time() - start
    print("Settimo tempo 600 elementi", end)

    start = time()
    # Sorting.heapSort(l[0:700])
    # mergesort.mergeSort(l[0:700])
    # Sorting.bubbleSort(l[0:700])
    # Sorting.insertionSortUp(l[0:700])
    # Sorting.quickSort(l[0:700])
    # Sorting.selectionSort(l[0:700])
    # v=l[0:700]
    # v.sort()
    # Sorting.quickSelectRand(l[0:700],350)
    # Sorting.quickSelectDet(l[0:700], 350, 5)
    Codice.Quicksort(l[0: 700], 350, 5)
    end = time() - start
    print("Ottavo tempo 700 elementi", end)

    start = time()
    # Sorting.heapSort(l[0:800])
    # mergesort.mergeSort(l[0:800])
    # Sorting.bubbleSort(l[0:800])
    # Sorting.insertionSortUp(l[0:800])
    # Sorting.quickSort(l[0:800])
    # Sorting.selectionSort(l[0:800])
    # v=l[0:800]
    # v.sort()
    # Sorting.quickSelectRand(l[0:800],400)
    # Sorting.quickSelectDet(l[0:800], 400, 5)
    Codice.Quicksort(l[0: 800], 400, 5)
    end = time() - start
    print("Nono tempo 800 elementi", end)

    start = time()
    # Sorting.heapSort(l[0:900])
    # mergesort.mergeSort(l[0:900])
    # Sorting.bubbleSort(l[0:900])
    # Sorting.insertionSortUp(l[0:900])
    # Sorting.quickSort(l[0:900])
    # Sorting.selectionSort(l[0:900])
    # v=l[0:900]
    # v.sort()
    # Sorting.quickSelectRand(l[0:900],450)
    # Sorting.quickSelectDet(l[0:900], 450, 5)
    Codice.Quicksort(l[0: 900], 450, 5)
    end = time() - start
    print("Decimo tempo 900 elementi", end)

    start = time()
    # Sorting.heapSort(l[0:1000])
    # mergesort.mergeSort(l[0:1000])
    # Sorting.bubbleSort(l[0:1000])
    # Sorting.insertionSortUp(l[0:1000])
    # Sorting.quickSort(l[0:1000])
    # Sorting.selectionSort(l[0:1000])
    # v=l[0:1000]
    # v.sort()
    # Sorting.quickSelectRand(l[0:1000],500)
    # Sorting.quickSelectDet(l[0:1000], 500, 5)
    Codice.Quicksort(l[0: 1000], 500, 5)
    end = time() - start
    print("Undicesimo tempo 1000 elementi", end)


if __name__ == "__main__":
    l = list(range(1000))
    test1(l)

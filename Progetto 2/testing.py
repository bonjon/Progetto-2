import random
import Codice
from time import time
import sys

sys.setrecursionlimit(10000000)
# Global parameters
amount = 10000
k = int(amount / 2)
m0 = 100
m1 = 5000
m2 = 10000


def test1():
    print("TEST 1: Lista già Ordinata \n")

    print("Caso con un m piccolo, es. 100")
    l = list(range(amount))
    start = time()
    Codice.Quicksort(l, k, m0)
    end = time() - start
    print("tempo impiegato-->", end)
    print("\n")

    print("Caso con m pari alla metà")
    l = list(range(amount))
    start = time()
    Codice.Quicksort(l, k, m1)
    end = time() - start
    print("tempo impiegato-->", end)
    print("\n")

    print("Caso con m pari alla lunghezza")
    l = list(range(amount))
    start = time()
    Codice.Quicksort(l, k, m0)
    end = time() - start
    print("tempo impiegato-->", end)
    print("\nEND.")


def test2():
    print("TEST 2: Lista Ordinata Inversamente\n")

    print("Caso con un m piccolo, es.100")
    l = list(range(amount, -1, -1))
    start = time()
    Codice.Quicksort(l, k, m0)
    end = time() - start
    print("tempo impiegato-->", end)
    print("\n")

    print("Caso con m pari alla metà")
    l = list(range(amount, -1, -1))
    start = time()
    Codice.Quicksort(l, k, m1)
    end = time() - start
    print("tempo impiegato-->", end)
    print("\n")

    print("Caso con m pari alla lunghezza")
    l = list(range(amount, -1, -1))
    start = time()
    Codice.Quicksort(l, k, m2)
    end = time() - start
    print("tempo impiegato-->", end)
    print("\nEND.")


def test3():
    print("TEST 3: Input Random")

    print("Caso con un m piccolo, es.100")
    basel = [random.randint(0, amount) for i in range(amount)]
    l = list(basel)
    start = time()
    Codice.Quicksort(l, k, m0)
    end = time() - start
    print("tempo impiegato-->", end)
    print("\n")

    print("Caso con m pari alla metà")
    basel = [random.randint(0, amount) for i in range(amount)]
    l = list(basel)
    start = time()
    Codice.Quicksort(l, k, m1)
    end = time() - start
    print("tempo impiegato-->", end)
    print("\n")

    print("Caso con m pari alla lunghezza")
    basel = [random.randint(0, amount) for i in range(amount)]
    l = list(basel)
    start = time()
    Codice.Quicksort(l, k, m2)
    end = time() - start
    print("tempo impiegato-->", end)
    print("\nEND.")


def test4():
    print("TEST 4: Lunghezza Lista Variabile, Input Random")

    print("Caso con m piccolo es.100")
    for i in range(50, 250, 5):
        random.seed(i)
        basel = [random.randint(0, (1 << 32) - 1) for j in range(1000 * i)]
        l = list(basel)
        k = int(len(l) / 2)
        start = time()
        Codice.Quicksort(l, k, m0)
        end = time() - start
        print(1000 * i, "tempo impiegato-->", end)
    print("\n")
    print("Caso con m pari alla metà")
    for i in range(50, 250, 5):
        random.seed(i)
        basel = [random.randint(0, (1 << 32) - 1) for j in range(1000 * i)]
        l = list(basel)
        k = int(len(l) / 2)
        start = time()
        Codice.Quicksort(l, k, m1)
        end = time() - start
        print(1000 * i, "tempo impiegato-->", end)
    print("\n")
    print("Caso con m pari alla lunghezza")
    for i in range(50, 250, 5):
        random.seed(i)
        basel = [random.randint(0, (1 << 32) - 1) for j in range(1000 * i)]
        l = list(basel)
        k = int(len(l) / 2)
        start = time()
        Codice.Quicksort(l, k, m2)
        end = time() - start
        print(1000 * i, "tempo impiegato-->", end)
    print("\nEND:")


def test5():
    print("TEST 5: m variabile, Input Random di 30 elementi")
    l = [random.randint(0, 30) for i in range(30)]
    for i in range(1, 31):
        m = i
        k = int(len(l) / 2)
        start = time()
        Codice.Quicksort(l, k, m)
        end = time() - start
        print(i, "tempo impiegato-->", end)
    print("END.")


if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
    test5()

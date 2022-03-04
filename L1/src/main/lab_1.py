# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random

def problema_1(text):
    """
    Să se determine ultimul (din punct de vedere alfabetic) cuvânt care poate apărea într-un text
    care conține mai multe cuvinte separate prin ” ” (spațiu).

    :param text: Textul unde se cauta ultimul cuvant din punct de vedera alfabetic
    :return: ultimul cuvant din punct de vedere alfabetic
    Complexitate: O(n)
    """
    words = text.split(" ")
    last_word = words[0]
    for word in words:
        if min(word, last_word) == last_word: last_word = word
    return last_word


def problema_3(v1, v2):
    """
    Să se determine produsul scalar a doi vectori rari care conțin numere reale. Un vector este rar
    atunci când conține multe elemente nule. Vectorii pot avea oricâte dimensiuni.
    :param v1: Primul vector rar
    :param v2: Al doilea vector rar
    :return: Produsul scalar al celor doi vectori
    Complexitate: O(n)
    """
    produs = 0
    for i in range(0, len(v1)):
        produs = produs + v1[i] * v2[i]
    return produs


def problema_4(text):
    """
    Să se determine cuvintele unui text care apar exact o singură dată în acel text.
    :param text: Textul in care
    :return: Lista cuvintelor care apar o singura data in text
    Complexitate O(n^2)
    """
    list = []
    words = text.split(" ")
    for word in words:
        if words.count(word) == 1:
            list.append(word)
    return list


def problema_5(numbers):
    """
    Pentru un șir cu n elemente care conține valori din mulțimea {1, 2, ..., n - 1} astfel încât o
    singură valoare se repetă de două ori, să se identifice acea valoare care se repetă.
    :param numbers: Lista de numere de la { 1, 2, ..., n-1 }
    :return: Numarul care se repeta
    Complexitate: O(1)
    """
    length = len(numbers)
    return sum(numbers) - (length * (length - 1)) / 2


def problema_6(numbers):
    """
    Pentru un șir cu n numere întregi care conține și duplicate, să se determine elementul
    majoritar (care apare de mai mult de n / 2 ori).
    :param numbers: Lista de numere
    :return: Numarul care apare de cele mai multe ori
    Complexitate: O(n)
    """
    if len(numbers) > 1:
        occurences = {}
        max = {"number": numbers[0], "occurences": 1}
        for number in numbers:
            if number not in occurences.keys():
                occurences[number] = 1
            else:
                occurences[number] += 1
            if (occurences[number] >= max["occurences"]):
                max["number"] = number
                max["occurences"] = occurences[number]
        return max["number"]
    return None


def problema_7(numbers, k):
    """
     Să se determine al k-lea cel mai mare element al unui șir de numere cu n elemente (k < n).
    :param numbers: Lista de numere in care se cauta al K-lea cel mai mare numar
    :param k: Al catelea element trebuie cautat
    :return: elementul gasit
    Complexitate: O(n)
    """
    pivot = random.choice(numbers)
    left = [x for x in numbers if x > pivot]
    mid = [x for x in numbers if x == pivot]
    right = [x for x in numbers if x < pivot]
    L, M = len(left), len(mid)

    if k <= L:
        return problema_7(left, k)
    elif k > L + M:
        return problema_7(right, k - L - M)
    else:
        return mid[0]


def problema_9(matrix, tuple1, tuple2):
    """
    Considerându-se o matrice cu n x m elemente întregi și o listă cu perechi formate din
    coordonatele a 2 căsuțe din matrice ((p,q) și (r,s)), să se calculeze suma elementelor din submatricile identificate de fieare pereche.
    :param matrix: Array bidimensioanl
    :param tuple1: Valorile coltului stanga sus
    :param tuple2: Valorile coltului dreapta jos
    :return: Suma elementelor din matrice determinata de cele doua colturi
    Complexitate: O(n*m)
    """
    sum = 0
    for i in range(tuple1[0], tuple2[0] + 1):
        for j in range(tuple1[1], tuple2[1] + 1):
            sum += matrix[i][j]
    return sum


def problema_10(matrix):
    """
    Considerându-se o matrice cu n x m elemente binare (0 sau 1) sortate crescător pe linii, să se
    identifice indexul liniei care conține cele mai multe elemente de 1.
    :param matrix: Array binar bidimensional
    :return: Linia pe care se afla cele mai multe elemente de 1.
    """
    row = -1
    n = len(matrix[0]) - 1
    m = len(matrix) - 1
    i = 0
    j = n
    while i < m and j != -1:
        while matrix[i][j] == 1 and j != -1:
            row = i
            j -= 1
        i += 1
    return row + 1


def canFill(matrix, i, j, current):
    return 0 <= i < len(matrix) and 0 <= j < len(matrix[0]) and matrix[i][j] == current


def fill(matrix, i, j, fillValue):
    dirI = [-1, 0, 0, 1]
    dirJ = [0, -1, 1, 0]
    
    current = matrix[i][j]

    matrix[i][j] = fillValue

    for k in range(4):
        if canFill(matrix, i + dirI[k], j + dirJ[k], current):
            fill(matrix, i + dirI[k], j + dirJ[k], fillValue)
                

def problema_11(matrix):
    """
    Considerându-se o matrice cu n x m elemente binare (0 sau 1), să se înlocuiască cu 1 toate
    aparițiile elementelor egale cu 0 care sunt complet înconjurate de 1.
    :param matrix: Array binar bidimensional
    :return: Array binar bidimensional cu toate zerourile inconjurate complet de 1 devin 1
    Complexitate: O(m*n)
    """
    (m, n) = (len(matrix), len(matrix[0]))
    #Vizitam toate elementele de pe prima si ultima linie
    for j in range(n):
        if matrix[0][j] == 0:
            fill(matrix, 0, j, -1)
        if matrix[m - 1][j] == 0:
            fill(matrix, m-1, j, -1)
    for i in range(m):
        if matrix[i][0] == 0:
            fill(matrix, i, 0, -1)
        if matrix[i][n-1] == 0:
            fill(matrix, i, n-1, -1)

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                matrix[i][j] = 1
            if matrix[i][j] == -1:
                matrix[i][j] = 0

    return matrix


def run_test():
    # Problema 1
    assert problema_1("Ana are mere rosii si galbene") == "si"
    assert problema_1("zzz abcd bcda cdae eadm fghe oew") == "zzz"
    assert problema_1("abcd bcad cdab dcab zap iwe qpwoe askdlj qowie rhj joqwiej zzap") == "zzap"

    # Problema 3
    assert problema_3([1, 0, 2, 0, 3], [1, 2, 0, 3, 1]) == 4
    assert problema_3([1, 0, 2, 0, 3], [1, 2, 0, 3, 0]) == 1
    assert problema_3([1, 0, 2, 0, 3], [0, 2, 0, 3, 0]) == 0

    # Problema 4
    assert problema_4("ana are ana are mere rosii ana") == ["mere", "rosii"]
    assert problema_4("text ext text ext tex") == ["tex"]
    assert problema_4("maria") == ["maria"]
    assert problema_4("") == [""]

    # Problema 5
    assert problema_5([1, 2, 3, 4, 2]) == 2
    assert problema_5([]) == 0
    assert problema_5([1, 2, 3, 4, 5, 5]) == 5
    assert problema_5([1, 2, 3, 4, 5, 1]) == 1

    # Problema 6
    assert problema_6([2, 8, 7, 2, 2, 5, 2, 3, 1, 2, 2]) == 2
    assert problema_6([5, 2, 8, 7, 2, 2, 5, 2, 3, 1, 2, 2]) == 2
    assert problema_6([5, 2, 8, 7, 2, 2, 5, 2, 3, 1, 5, 5]) == 5
    assert problema_6([]) == None

    # Problema 7
    assert problema_7([7, 4, 6, 3, 9, 1], 2) == 7
    assert problema_7([8, 4, 6, 3, 9, 1], 1) == 9
    assert problema_7([8, 4, 6, 3, 9, 1], 3) == 6

    assert problema_9([[0, 2, 5, 4, 1],
                       [4, 8, 2, 3, 7],
                       [6, 3, 4, 6, 2],
                       [7, 3, 1, 8, 3],
                       [1, 5, 7, 9, 4]], (1, 1), (3, 3)) == 38

    assert problema_9([[0, 2, 5, 4, 1],
                       [4, 8, 2, 3, 7],
                       [6, 3, 4, 6, 2],
                       [7, 3, 1, 8, 3],
                       [1, 5, 7, 9, 4]], (2, 2), (4, 4)) == 44

    assert problema_9([[0, 2, 5, 4, 1],
                       [4, 8, 2, 3, 7],
                       [6, 3, 4, 6, 2],
                       [7, 3, 1, 8, 3],
                       [1, 5, 7, 9, 4]], (0, 0), (0, 0)) == 0

    assert problema_10([[0, 0, 0, 1, 1],
                        [0, 1, 1, 1, 1],
                        [0, 0, 1, 1, 1]]) == 2

    assert problema_10([[0, 0, 0, 1, 1],
                        [0, 1, 1, 1, 1],
                        [0, 0, 1, 1, 1],
                        [0, 0, 1, 1, 1],
                        [0, 0, 1, 1, 1],
                        [0, 0, 1, 1, 1],
                        [1, 1, 1, 1, 1],
                        [0, 0, 1, 1, 1]]) == 7

    matrix = [
        [1, 1, 1, 1, 0, 0, 1, 1, 0, 1],
        [1, 0, 0, 1, 1, 0, 1, 1, 1, 1],
        [1, 0, 0, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 0, 1, 1, 0, 1],
        [1, 0, 0, 1, 1, 0, 1, 1, 0, 0],
        [1, 1, 0, 1, 1, 0, 0, 1, 0, 1],
        [1, 1, 1, 0, 1, 0, 1, 0, 0, 1],
        [1, 1, 1, 0, 1, 1, 1, 1, 1, 1]
    ]

    target = [
        [1, 1, 1, 1, 0, 0, 1, 1, 0, 1],
        [1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 1, 1, 0, 1, 1, 1, 0, 0, 1],
        [1, 1, 1, 0, 1, 1, 1, 1, 1, 1]
    ]

    matrix2 = [
        [1,1,1],
        [1,0,1],
        [1,1,1]
    ]

    target2 = [
        [1,1,1],
        [1,1,1],
        [1,1,1]
    ]

    assert problema_11(matrix) == target
    assert problema_11(matrix2) == target2


if __name__ == '__main__':
    run_test()


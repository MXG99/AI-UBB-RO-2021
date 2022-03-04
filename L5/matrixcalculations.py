def transpusa(x):
    return list(map(list, zip(*x)))


def getMinorant(x, i, j):
    return [row[:j] + row[j + 1:] for row in (x[:i] + x[i + 1:])]


def getDeterminant3by3(x):
    return (x[0][0] * x[1][1] * x[2][2]) + (x[1][0] * x[2][1] * x[0][2]) + (x[2][0] * x[0][1] * x[1][2]) - (
            x[0][2] * x[1][1] * x[2][0]) - (x[1][2] * x[2][1] * x[0][0]) - (x[2][2] * x[0][1] * x[1][0])


def getDeterminant2by2(x):
    return (x[0][0] * x[1][1]) - (x[0][1] * x[1][0])


def getMatrixInverse(x):
    det = getDeterminant3by3(x)
    adj = []
    for i in range(len(x)):
        adjRow = []
        for j in range(len(x)):
            minorant = getMinorant(x, i, j)
            adjRow.append(((-1) ** (i + j)) * getDeterminant2by2(minorant))
        adj.append(adjRow)
    adj = transpusa(adj)
    if det != 0:
        for i in range(len(adj)):
            for j in range(len(adj)):
                adj[i][j] = adj[i][j] / det
    else:
        raise Exception("Determinantul trebuie sa fie diferit de 0")
    return adj


def matrixMultiplication(a, b):
    c = []
    for i in range(len(a)):
        temp = []
        for j in range(len(b[0])):
            s = 0
            for k in range(len(a[0])):
                s += a[i][k] * b[k][j]
            temp.append(s)
        c.append(temp)
    return c

# def testDeterminant():
#     x = [
#         [3, 4, 0],
#         [6, 9, 8],
#         [6, 2, 0]
#     ]
#
# def testMatrixMultiplication():
#     a = [
#         [1, 3.3, 2.4],
#         [1, 3.1, 2.3],
#         [1, 2.9, 2.1],
#         [1, 2.3, 3.2]
#     ]
#     b = [
#         [1, 2.9, 2.5],
#         [1, 3, 3.2],
#         [1, 2.6, 2.1]
#     ]
#
#
# def testMatrxiInverse():
#     a = [
#         [3, 4, 0],
#         [6, 9, 8],
#         [6, 2, 0]
#     ]
#
#
# def run():
#     testMatrixMultiplication()
#     testDeterminant()
#     testMatrxiInverse()
#
#
#
# run()

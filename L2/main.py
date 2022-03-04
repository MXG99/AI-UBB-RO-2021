from greedy import Greedy

if __name__ == '__main__':
    matrix = []
    with open("data\\easy_01_tsp.txt") as f:
        cities = int(f.readline())
        for i in range(cities):
            matrix.append([int(x) for x in f.readline().split(",")])
        source = int(f.readline())
        destination = int(f.readline())

    g = Greedy(matrix, cities)

    path, sum = g.greedy_local_search(0, -1)
    f = open("data\\out.txt", "w")

    citiesString = str(cities) + "\n"
    pathString = str(path) + "\n"
    sumString = str(sum) + "\n"
    f.write(citiesString)
    f.write(pathString)
    f.write(sumString)

    path, sum = g.greedy_local_search(source - 1, destination - 1)
    numberOfCities = str(len(path)) + "\n"
    pathString = str(path) + "\n"
    sumString = str(sum) + "\n"
    f.write(numberOfCities)
    f.write(pathString)
    f.write(sumString)

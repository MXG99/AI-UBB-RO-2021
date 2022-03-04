import sys


class Greedy:
    def __init__(self, matrix, number_of_nodes):
        self.matrix = matrix
        self.number_of_nodes = number_of_nodes

    def greedy_local_search(self, source, destination):
        sum = 0
        starting = source + 1
        visited = [False for i in range(self.number_of_nodes)]

        minimum = sys.maxsize
        path = [-1 for i in range(self.number_of_nodes)]
        counter = 1
        path[0] = starting
        visited[0] = True
        i = 0
        j = 0
        while i < len(self.matrix) and j < len(self.matrix[0]):
            if counter >= len(self.matrix[i]) - 1:
                break
            if i == destination:
                break
            if j != i and visited[j] is False:
                if self.matrix[i][j] < minimum:
                    minimum = self.matrix[i][j]
                    position = j
                    path[counter] = position + 1
            j += 1
            if j == len(self.matrix[i]):
                sum += minimum
                minimum = sys.maxsize
                visited[path[counter] - 1] = True
                j = 0
                i = path[counter] - 1
                counter += 1

        i = path[counter - 1] - 1

        for j in range(len(self.matrix[i])):
            if i != j and self.matrix[i][j] < minimum and visited[j] is False:
                minimum = self.matrix[i][j]
                position = j
                visited[j] = True
                path[counter] = position + 1

        sum += minimum
        i = path[counter] - 1
        if destination == -1:
            sum += self.matrix[i][starting - 1]
        else:
            sum += self.matrix[i][destination]
            path[counter+1] = destination + 1
        return [x for x in path if x > 0], sum

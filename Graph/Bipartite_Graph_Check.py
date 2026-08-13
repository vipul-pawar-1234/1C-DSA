def isBipartite(graph):

    color = [-1] * len(graph)

    for start in range(len(graph)):

        if color[start] == -1:

            queue = []
            front = 0

            queue = queue + [start]
            color[start] = 0

            while front < len(queue):

                node = queue[front]
                front += 1

                for neighbour in graph[node]:

                    if color[neighbour] == -1:

                        color[neighbour] = 1 - color[node]

                        queue = queue + [neighbour]

                    elif color[neighbour] == color[node]:

                        return False

    return True


graph = [
    [1,3],
    [0,2],
    [1,3],
    [0,2]
]

print(isBipartite(graph))
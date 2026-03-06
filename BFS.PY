# BFS for 4 graphs

def bfs(graph, start):
    visited = []
    queue = [start]

    while queue:
        node = queue.pop(0)
        if node not in visited:
            print(node, end=" ")
            visited.append(node)

            for i in graph[node]:
                queue.append(i)
    print()
# Graph 1
g1 = {
    1:[2,7],
    2:[3,6],
    3:[4,5],
    4:[],
    5:[],
    6:[],
    7:[8,10],
    8:[9],
    9:[],
    10:[]
}

# Graph 2
g2 = {
    1:[2,3],
    2:[4,5],
    3:[],
    4:[2,5],
    5:[2,4] 
}

# Graph 3
g3 = {
    1:[2,3],
    2:[5,6],
    3:[7,4],
    4:[8],
    5:[],
    6:[],
    7:[8],
    8:[]
}

# Graph 4
g4 = {
    0:[1],
    1:[3],
    2:[1],
    3:[2,4],
    4:[5],
    5:[7],
    6:[4],
    7:[6]
}

print("BFS Graph 1:")
bfs(g1,1)

print("BFS Graph 2:")
bfs(g2,1)

print("BFS Graph 3:")
bfs(g3,1)

print("BFS Graph 4:")
bfs(g4,0)

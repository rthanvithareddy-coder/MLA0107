# DFS for 4 graphs

def dfs(graph, start):
    visited = []
    stack = [start]

    while stack:
        node = stack.pop()

        if node not in visited:
            print(node, end=" ")
            visited.append(node)

            for i in reversed(graph[node]):
                stack.append(i)
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

print("DFS Graph 1:")
dfs(g1,1)

print("DFS Graph 2:")
dfs(g2,1)

print("DFS Graph 3:")
dfs(g3,1)

print("DFS Graph 4:")
dfs(g4,0)

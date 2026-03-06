# Uniform Cost Search

def ucs(graph, start, goal):

    queue = [(0, start, [start])]
    visited = []

    while queue:

        queue.sort()
        cost, node, path = queue.pop(0)

        if node == goal:
            print("Path:", " -> ".join(path))
            print("Cost:", cost)
            print()
            return

        if node not in visited:
            visited.append(node)

            for neighbour, weight in graph[node]:
                queue.append((cost + weight, neighbour, path + [neighbour]))


# -------- Graph 1 --------
g1 = {
'S':[('A',1),('G',12)],
'A':[('B',3),('C',1)],
'B':[('D',3)],
'C':[('D',1),('G',2)],
'D':[('G',3)],
'G':[]
}

# -------- Graph 2 --------
g2 = {
'A':[('B',2),('C',3),('D',4)],
'B':[('E',1),('F',3)],
'C':[('G',4)],
'D':[('H',2),('I',1)],
'E':[('J',8),('K',4)],
'F':[],
'G':[('L',3)],
'H':[('M',3)],
'I':[],
'J':[],
'K':[],
'L':[],
'M':[]
}

# -------- Graph 3 --------
g3 = {
'V1':[('V2',9),('V3',4)],
'V2':[('V3',2),('V4',7),('V5',3)],
'V3':[('V4',1),('V5',6)],
'V4':[('V5',4),('V6',8)],
'V5':[('V6',2)],
'V6':[]
}

# -------- Graph 4 --------
g4 = {
'S':[('A',3),('B',2),('C',7)],
'A':[('D',3),('E',8),('G',15)],
'B':[('G',20)],
'C':[('G',6)],
'D':[],
'E':[],
'G':[]
}


print("Graph 1 UCS Result")
ucs(g1,'S','G')

print("Graph 2 UCS Result")
ucs(g2,'A','M')

print("Graph 3 UCS Result")
ucs(g3,'V1','V6')

print("Graph 4 UCS Result")
ucs(g4,'S','G')

# Prim's Algorithm in Python

INF = float('inf')
# number of vertices in graph
N = 5

#creating graph by adjacency matrix method
g = [[0, 19, 5, 0, 0],
     [19, 0, 5, 9, 2],
     [5, 5, 0, 1, 6],
     [0, 9, 1, 0, 1],
     [0, 2, 6, 1, 0]]

selected_node = [0, 0, 0, 0, 0]

no_edge = 0

selected_node[0] = True

# printing for edge and weight
print("Edge : Weight\n")
while (no_edge < N - 1):
    
    minimum = INF
    a = 0
    b = 0
    for i in range(N):
        if selected_node[i]:
            for j in range(N):
                if ((not selected_node[j]) and g[i][j]):  
                    # not in selected and there is an edge from i->j
                    if minimum > g[i][j]:
                        minimum = g[i][j]
                        a = i
                        b = j
    print(str(a) + "-" + str(b) + ":" + str(g[a][b]))
    selected_node[b] = True
    no_edge += 1
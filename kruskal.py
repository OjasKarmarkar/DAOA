n = int(input("Enter no of vertices : "))
g = [[0]*(n) for _ in range(0,n)]  # adjacency matrix
ne = 1  # used to check if all vertices are included or not
parent = [False for _ in range(0,n)]
final_cost = 0
a, u, v = 0, 0, 0


def find(i):

    while(parent[i]):
        i = parent[i]
    return i


def uni(i, j):

    if(i != j):
        # path from (i->j or u->v is added )
        parent[j] = i
        return True

    return False


# Step 1 :  Take Input as Adjacency Matrix

for i in range(n):
    for j in range(n):
        if i != j:
            weight = int(input(f"Enter cost of Edge {i} to {j} :  "))
            if weight==0:
                g[i][j] = float('inf')
            else:
                g[i][j] = weight
        else:
            g[i][j] = float('inf')

print(g)

# Step 2 :  Sort and Start Adding least weight edges

while ne < n:
    min_w = float('inf')

    for i in range(n):
        for j in range(n):

            if g[i][j] < min_w:
                 # find out min cost and edge (u->v) for every iteration
                min_w = g[i][j]
                a = u = i
                b = v = j
    #Why use find???
    u=find(u)
    v=find(v)
    if(uni(u,v)):
        print(f"Edge from {a}->{b} has min value of  : {min_w}"),
        final_cost += min_w
        ne+=1
    g[a][b]=g[b][a]=float('inf') # Make selected edges as infinity again

print(parent)

denom = [int(item) for item in input("Enter Denominations : ").split()]
goal = int(input("Enter Sum to achieve : "))
x= len(denom)+1
y = goal+1
solution = []

matrix = [[0 for _ in range(y)] for _ in range(y)]


def CC():
    for j in range(1, y):
        for i in range(1, x):
            if i == j or i == 1:
                matrix[i][j] = 1 + matrix[1][j-denom[i-1]]
            elif j < denom[i-1]:
                matrix[i][j] = matrix[i-1][j]
            else:
                matrix[i][j] = min(matrix[i-1][j], 1 + matrix[i][j-denom[i-1]])


def display_matrix():
    for i in range(x):
        for j in range(y):
            print(matrix[i][j], end=" ")
        print("")


def trace():
    i, j = x-1, y-1
    while j > 0:
        if matrix[i][j] == matrix[i-1][j]:
            i -= 1
        else:
            j -= denom[i-1]
            solution.append(denom[i-1])


def display_solution():
    print(solution)


CC()
display_matrix()
trace()
display_solution()

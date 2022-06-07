n = int(input("Enter size of board (n*n) : "))

def solveNQueen(n):
    col = set()
    posDiag = set() # row + column
    negDiag = set() # row - column

    soln = []
    board = [["-"] * n for i in range(n)]

    def backTrack(r):
        if r == n :
            copy = ["".join(row) for row in board]
            # Solution Found
            soln.append(copy)
            return

        for c in range(n):

            if c in col or (r+c) in posDiag or (r-c) in negDiag:
                #Bounding Fn
                continue
            else:
                #Place 
                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                board[r][c] = "Q"
                
                #Explore all DFS options
                backTrack(r+1)
                
                #Go Back One Step
                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c] = "-"

    backTrack(0)
    return soln


print(solveNQueen(n))
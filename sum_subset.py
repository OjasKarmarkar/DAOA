final_sum = int(input("Enter the sum : "))
subset = [int(item) for item in input("Enter The numbers (Subsubset) : ").split()]


state = []
soln = []


def solve(s,  idx) :
        # return false if s value exceed sum
        if (s > final_sum) :
            return

        # check if stack has the right subsubsets of numbers
        if (s == final_sum) :
            print(state)
            return

        i = idx
        while (i < len(subset)) :

            state.append(subset[i])       
            solve(s + subset[i], i + 1)
            state.pop()
            i += 1


solve(0, 0)
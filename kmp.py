# Time Complexity - O (n+m) , n = for traversing text  , m = for traversing pattern
# Knuth - Morris - Pratt Algo
pattern = input("Enter pattern to search : ")
text_problem = input("Enter text to search In : ")



def compute_lps(pattern):
    lps = [0] * len(pattern)

    prefi = 0
    for i in range(1, len(pattern)):

        while prefi and pattern[i] != pattern[prefi]:
            prefi = lps[prefi - 1]

        if pattern[i] == pattern[prefi]:
            prefi+=1
            lps[i] = prefi

    return lps

def kmp(pattern , text):
    lps = compute_lps(pattern)
    patterni=0
    match_indices = []

    for i , ch in enumerate(text):

        while patterni and pattern[patterni]!=ch:
            patterni = lps[patterni - 1]

        if pattern[patterni] == ch:
            if patterni == len(pattern) - 1:
                match_indices.append(i - patterni)
                patterni = lps[patterni]
            else:
                patterni+=1

    return match_indices



print(kmp(pattern , text_problem))
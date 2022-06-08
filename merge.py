arr = [44 ,33 ,11, 55, 77 ,90 ,40, 60 ,99 ,22 ,88]

def merge(l , r):
    l_ix = 0
    r_ix = 0
    res = []

    while l_ix < len(l) and r_ix < len(r):

        if l[l_ix]<r[r_ix]:
            res.append(l[l_ix])
            l_ix+=1
        else:
            res.append(r[r_ix])
            r_ix+=1
    
    res.extend(l[l_ix:])
    res.extend(r[r_ix:])
    return res


def msort(arr):

    if len(arr)<=1:
        return sorted(arr)

    mid = len(arr)//2
    l = msort(arr[:mid])
    r = msort(arr[mid:])
    
    return merge(l,r)

print(msort(arr))
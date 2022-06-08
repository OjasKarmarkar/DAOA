l=[
    [44 ,33 ,11, 55, 77 ,90 ,40, 60 ,99 ,22 ,88],
    [17 ,9 ,22, 31, 7 ,12, 10, 21, 13, 29, 18, 20, 11],
    [100, 76, 80, 9, 111, 50]
]

def swap(l,a,b):
    temp=l[a]
    l[a]=l[b]
    l[b]=temp

def qsort(l):

    if len(l)<2:
        return l

    p=1
    q=len(l)-1
    pivot=l[0]

    loop_on=True
    while (loop_on):
            while p < len(l) and l[p] < pivot:
                p += 1
            while l[q] > pivot and q > 0:
                q -= 1

    
            if p < q:
                swap(l,p,q)
            else:
                swap(l,0,q)
                loop_on = False
    
    return (qsort(l[:q]) + [pivot] + qsort(l[q+1:]))

for item in l:
    print(qsort(item))



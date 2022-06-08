arr = [15 , 12 , 4 , 19 , 55 , 100 , 66]

def qsort(l):
    if len(l)<2:
        return sorted(l)
    
    pivot = l[0]
    p=l[1]
    q=len(l)-1

    loop_on = True

    while(loop_on):
        while p <len(l) and l[p]<pivot:
            p +=1

        while l[q]>pivot and q >0:
            q -=1

        if q<p:
            l[pivot] , l[q] = l[q] , l[pivot]
            loop_on = False
            #overlap 
        
        else:
            l[p] , l[q] = l[q] , l[p]
    
    return (qsort(l[:q]) + [pivot] + l[q+1:])

print(qsort(arr))



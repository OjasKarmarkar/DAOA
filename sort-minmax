def min_max(arr, low, high):
    global minm,maxm
    if low == high: # one element
        minm = maxm = arr[0]

    elif high == low+1: # two elements
        if arr[low] < arr[high]:
            minm, maxm = arr[low], arr[high]
        else:
            minm, maxm = arr[high], arr[low]
    
    else:
        mid = (low + high) // 2
        min_max(arr,0,mid)
        minL, maxL = minm, maxm # stire min max of left sub arr
        min_max(arr,mid+1,high)
        minR, maxR = minm, maxm # stire min max of right sub arr

        if (minL < minR):
            minm = minL
        else:
            minm = minR

        if (maxL > maxR):
            maxm = maxL
        else:
            maxm = maxR

minm, maxm = 0, 0 
arr = [3,2,1,6,4,2,5,9,8,7]
low = 0
high = len(arr)-1
min_max(arr, 0, high)
print(f"Miminum: {minm}, Maximum: {maxm}")

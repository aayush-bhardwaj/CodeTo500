def mergeSort(A):
    n = len(A)
    left = []
    right = []
    mid = n/2
    if(n < 2):
        return
    else:
        # import pdb;pdb.set_trace()
        for x in range(0,mid):
            left.append(A[x])
        for y in range(mid,n):
            right.append(A[y])
    mergeSort(left)
    mergeSort(right)
    merge(left, right, A)
    return A

def merge(left, right, A):
    ln = len(left)
    rn = len(right)
    l = 0
    r = 0
    k = 0
    # import pdb;pdb.set_trace()
    while(l<ln and r<rn):
        if(left[l] < right[r]):
            A[k] = left[l]
            k += 1
            l += 1
        else:
            A[k] = right[r]
            k += 1
            r += 1

    while(l < ln):
        A[k] = left[l]
        k += 1
        l += 1

    while(r < rn):
        A[k] = right[r]
        k += 1
        r += 1

A = [2,4,1,6,8,5,3,7]
output = mergeSort(A)
print output

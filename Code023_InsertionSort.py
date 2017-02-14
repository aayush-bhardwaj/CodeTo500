def insertionSort(A):
    for x in range(1,len(A)):
        # import pdb;pdb.set_trace()
        hole = x
        item = A[hole]
        value = hole-1
        while(value >= 0):
            if(A[value] > item):
                A[value + 1] = A[value]
            else:
                A[value + 1] = item
                break
            if(value == 0):
                A[value]=item
                break
            else:
                value -= 1
    return A

A= [3,24,5,32,98,1,234,43,98,12,11,16]
sortedList = insertionSort(A)
print sortedList

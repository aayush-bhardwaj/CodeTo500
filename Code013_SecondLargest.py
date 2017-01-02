#DAY07_24DEC2016_Code013.py

#NOTES

'''
Max element in a string
max(list)

arr.sort() does not return a list , rather sorts the array in place.
but,
sorted(arr) returns a new list
'''

#QUES

'''

'''

#SOLUTION


if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    arr1 = list(set(arr))
    arr1.sort(reverse=True)
    if(len(arr1) == 1):
        print arr1[0]
    else:
        print arr1[1]

#DAY07_24DEC2016_Code011.py

#NOTES

'''
hash() -- ??
map() -- ??
'''

#QUES

'''
Input Format

The first line contains an integer, , denoting the number of elements in the tuple. 
The second line contains  space-separated integers describing the elements in tuple .

Output Format

Print the result of hash(t).
'''

#SOLUTION


if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    print hash(tuple(integer_list))

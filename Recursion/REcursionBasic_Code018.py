def recursion(num):
    if(num==0):
        return
    else:
        print num
        recursion(num-1)

recursion(5)
'''
output:
5
4
3
2
1
'''

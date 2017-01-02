#DAY07_24DEC2016_Code010.py

#NOTES

'''
List functions 
1. insert()
2. remove()
3. print()
4. sort()
5. pop()
6.remove()
'''

#QUES

'''
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.

Input Format

The first line contains an integer, , denoting the number of commands. 
Each line  of the  subsequent lines contains one of the commands described above.

Constraints

The elements added to the list must be integers.
Output Format

For each command of type print, print the list on a new line.

Sample Input

12
insert 0 5
insert 1 10
insert 0 6
print 
remove 6
append 9
append 1
sort 
print
pop
reverse
print
Sample Output

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
'''

#SOLUTION


if __name__ == '__main__':
    N = int(raw_input())
    a=[]
    for x in range(0,N):
    	#import pdb;pdb.set_trace()
    	cmd = raw_input().split(" ")
    	one = cmd[0]
    	if(one == "insert"):
			index = int(cmd[1])
			integer = int(cmd[2])
			a.insert(index,integer)
    	elif(one == "print"):
			print(a)
    	elif(one == "remove"):
            a.remove(int(cmd[1]))
        elif(one == "append"):
            a.append(int(cmd[1]))
        elif(one == "sort"):
            a.sort()
        elif(one == "pop"):
            a.pop()
        elif(one == "reverse"):
            a.reverse()

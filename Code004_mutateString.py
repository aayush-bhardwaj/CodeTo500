#DAY04_21DEC2016_Code004.py

#NOTES

'''
1. Lists are mutable
2. Strings are immutable
3. tuples are immutable
4. string = "aayush"
	string[0] = 'a'
	string[1] = 'a'
	string[2] = 'y'

5. string[4] = 'k'
	TypeError: 'str' object does not support item assignment

6. slice a string
	string[2:] = 'yush'
	string[:2] = 'aa'
'''

#QUES

'''
Task 
Read a given string, change the character at a given index and then print the modified string.

Input Format 
The first line contains a string, . 
The next line contains an integer , denoting the index location and a character  separated by a space.

URL = https://www.hackerrank.com/challenges/python-mutations?h_r=next-challenge&h_v=zen
'''

#SOLUTION

def mutate_string(string, position, character):
    string1 = list(string)
    string1[position] = character
    string2 = ("").join(string1)
    return string2

if __name__ == '__main__':
    s = raw_input()
    p,c = raw_input().split()
    result = mutate_string(s,int(p),c)
    print result
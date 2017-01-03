from __future__ import division
#DAY07_24DEC2016_Code015.py

#NOTES

'''
Using __future__ we can import the features of higher python versions 
without upgrading our python .
'''

#QUES

'''

'''

#SOLUTION
def division(a,b):
	#Using __future__ I am using divsion as in Python 3.x
	print a/b #7/3 = 2.3333
	print a//b #7/3 = 2


if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())
    result = division(a,b)
    print result
#DAY04_21DEC2016_Code008.py

#NOTES

'''
How to reverse a string

string = '123'
- reverse = string[::-1]
- reverse = ('').join(reversed(string))

reversed() returns a reversed object
'''

#QUES

'''
Find if a string is a pallindrome
'''

#SOLUTION
def pallindrome(s):
	if(s == s[::-1]):
		return True
	else:
		return False

if __name__ == '__main__':
    s = raw_input()
    result = pallindrome(s)
    print result
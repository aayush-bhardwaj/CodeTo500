#DAY04_21DEC2016_Code001.py
'''
NOTES :

1. help(str.istitle())  - The terminal help opens up
2. istitle() - Check if a string is camel case
3. upper() - convert  to upper case
4. lower() - convert to lower case
5. isupper() - check if a string is in uppercase
6. islower() - check if a string is in lowercase
7. split a string into an array
	word = "aayush bhardwaj"
	list = [y for y in word.split(" ")]
	list = ["aayush","bhardwaj"]
8. split a string into a character array
	word = "aayush"
	list = list(word)
	list = ['a','a','y','u','s','h']
'''
#QUES
'''
You are given a string . Your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
eg.

aayush BHARDWAJ
AAYUSH bhardwaj
URL : https://www.hackerrank.com/challenges/swap-case
'''

def swap_case(s):
    l = list(s)
    res = ""
    for item in l:
        if(item.isupper() == True):
            res += item.lower()
        elif(item.islower() == True):
            res += item.upper()
        else:
            res += item
    return res

if __name__ == '__main__':
    s = raw_input()
    result = swap_case(s)
    print result
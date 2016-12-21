#DAY04_21DEC2016_Code002.py

#NOTES

'''
1. Split
	line = "Code To 500"
	list = line.split(" ")
	list = ["Code","To","500"]

2. Join
	string = ("-").join(list)
	string = "Code-To-500"
'''

#QUES

'''
You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.


'''

#SOLUTION

def split_and_join(line):
    # writ your code here
    input = line.split(" ")
    output = "-".join(input)
    return output

if __name__ == '__main__':
    s = raw_input()
    result = split_and_join(s)
    print result
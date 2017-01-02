#DAY04_21DEC2016_Code005.py

#NOTES

'''
1. String traversal happens from left -> right

'''

#QUES

'''
In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. 
'''

#SOLUTION

def count_substring(string, sub_string):
    ss_len = len(sub_string)
    count = 0
    for x in range(0,len(string)):
        s2 = string[x:(x+ss_len)]
        if(s2==sub_string):
            count += 1
    return count
    
if __name__ == '__main__':
    string = raw_input().strip()
    sub_string = raw_input().strip()    
    count = count_substring(string, sub_string)
    print count
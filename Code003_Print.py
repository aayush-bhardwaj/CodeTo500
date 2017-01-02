#DAY04_21DEC2016_Code003.py

#NOTES

'''

'''

#QUES

'''
You are given the firstname and lastname of a person on two different lines. Your task is to read them and print the following:

Hello firstname lastname! You just delved into python.
'''

#SOLUTION

def print_full_name(a, b):
    res =  "Hello %s %s! You just delved into python."%(a,b)
    return res
    
if __name__ == '__main__':
    s = raw_input()
    t = raw_input()
    result = print_full_name(s,t)
    print result
#DAY04_21DEC2016_Code006.py

#NOTES

#Good Question 

'''
Python built in String validation functions

1. string.isalnum() - is it alphanumeric ?
2. string.isalpha() - is it alphabetical ?
3. string.isdigit() - is it numeric ?
'''

#QUES

'''
In the first line, print True if  has any alphanumeric characters. Otherwise, print False. 
In the second line, print True if  has any alphabetical characters. Otherwise, print False. 
In the third line, print True if  has any digits. Otherwise, print False. 
In the fourth line, print True if  has any lowercase characters. Otherwise, print False. 
In the fifth line, print True if  has any uppercase characters. Otherwise, print False.
'''

#SOLUTION

if __name__ == '__main__':
    s = raw_input()
    alnum = False
    alpha = False
    digit = False
    lower = False
    upper = False
    
    
    if(s == ""):
        print False
        print False
        print False
        print False
        print False
    else:
        for x in range(0,len(s)):      
            if(s[x].isdigit()):
                if(digit == False):
                    digit = True

            if(s[x].isalpha()):
                if(alpha == False):
                    alpha = True

            if(s[x].isupper()):
                if(upper == False):
                    upper = True

            if(s[x].islower()):
                if(lower == False):
                    lower = True    
                    
    if((alpha == True) or (digit == True)):
        alnum = True
        
    print alnum
    print alpha
    print digit
    print lower
    print upper
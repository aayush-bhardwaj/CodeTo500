#DAY07_24DEC2016_Code009.py

#NOTES

'''
Anagrams

 --> from collections import Counter
 	It return a dictionary with key and count as it's values
'''

#QUES

'''
Check for anagrams
'''

#SOLUTION

def anagram(str1,str2):
	from collections import Counter
	if(Counter(str1) == Counter(str2)):
		return True
	else:
		return False

if __name__ == '__main__':
    str1 = raw_input()
    str2 = raw_input()
    result = anagram(str1,str2)
    print result
#DAY07_24DEC2016_Code014.py

#NOTES

'''

'''

#QUES

'''

'''

#SOLUTION



classi = []
for x in range(int(raw_input())):
    stud = []
    name = raw_input()
    score = float(raw_input())
    stud.append(name)
    stud.append(score)
    classi.append(stud)
    
classi2 = list(set([x[1] for x in classi]))
classi2.sort()
num = classi2[1]
#classi3 = [x[0] for x in classi if x[1] is num]
classi3 = []
for x in classi:
    if(x[1] == num):
        classi3.append(x[0])
classi3.sort()
for x in range(len(classi3)):
	print classi3[x]
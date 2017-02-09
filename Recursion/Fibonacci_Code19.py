'''
def Fibonacci(num,A,B):
    if(num==0):
        return
    else:
        A=A
        B=B
        C=A+B
        print C
        A=B
        B=C
        Fibonacci(num-1,A,B)
A=0
B=1
print A
print B
Fibonacci(8,A,B)
'''
'''
#APPROACH-02

def Fibonacci(n):
    if(n<=1):
        return n
    else:
        return(Fibonacci(n-1) + Fibonacci(n-2))

for x in range(50):
    print Fibonacci(x)
'''
#APPROACH-03 Recursion and Momoization
T = []
def Fibonacci(n):
    if(n<=1):
        return n
    else:
        if (T[n] != -1):
            return T[n]
        else:
            T[n] = (Fibonacci(n-1) + Fibonacci(n-2))
            return T[n]
for y in range(55):
    T.append(-1)

for x in range(50):
    print Fibonacci(x)

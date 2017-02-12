def power(num, pow):
    if(pow == 0):
        return 1
    else:
        return(num * power(num, pow-1))

num = int(raw_input("Enter number"))
pow = int(raw_input("Enter power"))
C = int(raw_input("Enter modulus"))
output = power(num, pow)
print output

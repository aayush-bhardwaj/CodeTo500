#Approach - 01
def reverse(a):
    b=[]
    for x in range((len(a)-1),-1,-1):
        print a[x]
        b.append(a[x])
    return b

a=[1,2,3,4]
output = reverse(a)
print output

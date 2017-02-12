import sys


n,k,q = raw_input().strip().split(' ')
n,k,q = [int(n),int(k),int(q)]
a = map(int,raw_input().strip().split(' '))

for x in range(k):
    item = a[len(a)-1]
    a.pop(len(a)-1)
    a.insert(0, item)

for a0 in xrange(q):
    m = int(raw_input().strip())
    print a[m]

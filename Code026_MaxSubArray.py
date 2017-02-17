# Find max sub - array in a given array
#
# APPROACH - 01 : Brute Force Technique
# Time complexity = O(n^3) very bad
import sys
def maxSubArray(A):
    ans = -(sys.maxint)
    for i in range(1 ,len(A)+1):
        sum = 0
        for j in range(0,len(A)):
            sum = A[j]
            for k in range(1,i):
                if((j+k)<len(A)):
                    sum = sum + A[j+k]
            if(sum>ans):
                ans = sum
    return ans

A = [1,-2,3,5]
out = maxSubArray(A)
print out

# Now let's apply Divide and conquer
# APPROACH - 02

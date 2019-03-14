#encoding=utf-8
"""
The following iterative sequence is defined for the set of positive integers:

n -> n/2 (n is even)
n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
#Runs in 28.070503 seconds
import time

startTime = time.clock()
max = (0,0)

def getCollatzCount(n):
    count = 0
    while n!=1:
        if n%2==0:
            n = n/2
            count+=1
        else:
            n = 3*n + 1
            count+=1
    return count

for x in xrange(1, 1000000):
    currentCount = getCollatzCount(x)
    if currentCount > max[0]:
        max = (currentCount, x)

print max[1], time.clock() - startTime
#encoding=utf-8
"""
Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2. The first ten pentagonal numbers are:

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference, 70 − 22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are pentagonal and D = |Pk − Pj| is minimised; what is the value of D?
"""
#Runtime = 35.018393 seconds
import time
startTime = time.clock()
pentagonalDict = {}
pentagonalSet = set()

for x in xrange(1,10000):
    pentagonalDict[x]= x * ((3*x)-1) / 2
    pentagonalSet.add(x * ((3*x)-1) / 2)

currentMin = float('inf')

def totallyPentagonal(k,j):
   return k+j in pentagonalSet and k-j in pentagonalSet 

for x in xrange(1, 10000):
    for y in xrange(1,10000):
        if totallyPentagonal(pentagonalDict[x],pentagonalDict[y]):
            if abs(pentagonalDict[x] - pentagonalDict[y]) < currentMin:
                currentMin = abs(pentagonalDict[x] - pentagonalDict[y])

print currentMin, time.clock()-startTime
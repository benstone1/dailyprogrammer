#encoding=utf-8
"""
Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:

Triangle Tn=n(n+1)/2 1, 3, 6, 10, 15, ...
Pentagonal Pn=n(3n−1)/2 1, 5, 12, 22, 35, ...
Hexagonal Hn=n(2n−1) 1, 6, 15, 28, 45, ...
It can be verified that T285 = P165 = H143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal.

"""
#Runtime = 1.226477 seconds
import time

startTime = time.clock()
triangleNumbers = set()
pentagonalNumbers = set()
hexagonalNumbers = set()

for n in xrange(0,1000000):
    triangleNumbers.add(((n * (n+1 ) ) / 2))
    pentagonalNumbers.add((n * (3 * n - 1 ) ) /2 )
    hexagonalNumbers.add((n * (2 * n - 1)))

def isAllTypes(n):
    return n in triangleNumbers and n in pentagonalNumbers and n in hexagonalNumbers

for x in xrange(286, 1000000000):
    currentTriangleNum = x * (x+1) / 2
    if isAllTypes(currentTriangleNum):
        print currentTriangleNum, time.clock()-startTime
        break

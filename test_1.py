#!/usr/bin/python

'''
Write a program that prints the numbers from 1 to 100.
But for multiples of three print "Three" instead of the number and
for the multiples of five print "Five".
For numbers which are multiples of both three and five print "ThreeFive".
'''

def NumTest(N):
    for n in range(1,N+1):
        r = n % 3
        s = n % 5
        if r == 0 and s == 0:
            print ("ThreeFive")
        elif r == 0:
            print ("Three")
        elif s == 0:
            print ("Five")
        else:
            print (n)

if __name__ == '__main__':
    NumTest(100)

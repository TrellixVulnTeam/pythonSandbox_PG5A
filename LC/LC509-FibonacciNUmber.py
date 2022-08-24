"""
Dynamic Programming. 

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).

 

"""


class Solution:
    def fib(self, n: int, m=[]) -> int:
        if n == 0: 
            return 0
        if n == 1 or n == 2: 
            return 1
        m = [None] * (n+1)
        m[0] = 0
        m[1] = 1
        m[2] = 1
        for i in range(3, n+1):
            m[i] = m[i-1] + m[i-2]
        return m[n]
        


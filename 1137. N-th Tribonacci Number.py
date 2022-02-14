class Solution:
    def tribonacci(self, n: int) -> int:
        TN = 0
        TN1 = 1
        TN2 = 1
        TN3 = int()
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1

        for i in (range(3,n+1)):
            TN3 = TN + TN1 + TN2
            TN = TN1
            TN1 = TN2
            TN2 = TN3
        return TN3
        
        
'''

        The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

 

Example 1:

Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
Example 2:

Input: n = 25
Output: 1389537
'''

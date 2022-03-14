class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:

# This is not working....
#         n1 = n-1
#         n2 = n - n1
#         while True:
#             if '0' in str(n1):
#                 n1 = n1-1
#                 n2 = n2 + 1

#             elif '0' in str(n2):
#                 n2 = n2-1
#                 n1 = n1 + 1
#             else:

#                 break
#         # print(n1, n2)
#         return [n1, n2]
        n1 = n
        n2 = 0
# This is working.
        while True:
            if '0' not in str(n1) and '0' not in str(n2):
                print(n1,n2)
                return [n1,n2]
                break
            else:
                n1-=1
                n2+=1

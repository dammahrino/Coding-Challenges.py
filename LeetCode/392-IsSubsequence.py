# Problem Description
# https://leetcode.com/problems/is-subsequence/


# Input
# s = "abc", t = "ahbgdc"

# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         out = True
#         for letter in s:
#             print(t)
#             letterIndex = t.find(letter)
#             if letterIndex == -1:
#                 out = False
#                 break
#             else:
#                 t = t[letterIndex + 1 :]
#         return out

# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         it_create = iter(t)
#         return all(letter in it_create for letter in s)

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):return False
        if len(s) == 0:return True
        subsequence=0
        for i in range(0,len(t)):
            if subsequence <= len(s) -1:
                print(s[subsequence])
                if s[subsequence]==t[i]:

                    subsequence+=1
        return  subsequence == len(s) 

solution = Solution()
print(solution.isSubsequence("acb", "ahbgdc"))
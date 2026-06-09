class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = list(str(x))
        result = True
        for i in range(len(x)//2):
            if x[i] != x[-i-1]:
                result = False
        return result
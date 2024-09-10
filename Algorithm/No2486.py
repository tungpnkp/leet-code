# run time: 69%
# memory: 75%
class Solution:
    def nextPermutation(self, s: str, t: str) -> int:
        z=0
        for i in range(len(s)):
            if s[i] == t[z]:
                z+=1
            if z==len(t):
                return 0
        return len(t)-z


solution = Solution()
print(solution.nextPermutation('coaching', "coding"))
print(solution.nextPermutation('z', "abcde"))
print(solution.nextPermutation('abcde', "a"))

# run time: 64%
# memory: 90%
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) >= len(needle):
            j = 0
            i = 0
            while i < len(haystack):
                if needle[j] == haystack[i]:
                    if j == len(needle) - 1:
                        return i-j
                    else:
                        j += 1
                        i += 1
                else:
                    i = i - j + 1
                    j=0
        return -1

solution = Solution()
print(solution.strStr("mississippi", "issip"))
print(solution.strStr("leetcode", "leeto"))


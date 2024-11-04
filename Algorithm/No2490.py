# run time:
# memory:
class Solution:
    def action(self, s: str):
        arr = s.split()
        arr_len = len(arr)
        if arr_len > 1:
            for i in range(arr_len - 1):
                if arr[i][-1] != arr[i+1][0]:
                    return False
        return arr[0][0] == arr[arr_len - 1][-1]


solution = Solution()
print(solution.action('leetcode exercises sound delightful'))
print(solution.action('Leetcode is cool'))


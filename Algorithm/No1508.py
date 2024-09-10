# run time:
# memory:
class Solution:
    def action(self, nums: [int], n: int, left: int, right: int):
        arr = []
        i = 0
        while i < n:
            prefix = 0
            for j in range(i,n):
                prefix += nums[j]
                arr.append(prefix)
            i += 1
        arr.sort()
        return sum(arr[left-1:right]) % 1000000007


solution = Solution()
print(solution.action([1,2,3,4], 4, 1, 5))
# print(solution.action([4,1,5,9], [1,3,2,6]))
# print(solution.action([1]))


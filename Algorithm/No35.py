# run time: 86%
# memory: 50%
class Solution:
    def searchInsert(self, nums: [], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid
        return l

solution = Solution()
print(solution.searchInsert([1,3,5,6], 5))
print(solution.searchInsert([1,3,5,6], 7))
print(solution.searchInsert([1,3,5,6], 2))


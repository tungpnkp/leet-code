class Solution:
    def majorityElement(self, nums: []) -> int:
        count_dict = defaultdict(int)
        n = len(nums) / 2

        for element in nums:
            count_dict[element] += 1
            if count_dict[element] > n:
                return element

        return count_dict

solution = Solution()
print(solution.majorityElement([3,2,3]))


# toi uu
# return functools.reduce(lambda x, y: x ^ y, nums, 0)
# run time: 69%
# memory: 75%
class Solution:
    def action(self, nums: [], n:int):
        counter_nums = {}
        max_num = nums[-1]
        patches = 0
        for num in nums:
            if num in counter_nums:
                counter_nums[num] += num
            else:
                counter_nums[num] = num
        if 1 not in counter_nums:
            patches +=1
            counter_nums[1] = 1
        sum_temp = counter_nums[1]
        i = 2
        while sum_temp<n:
            if i not in counter_nums and i > sum_temp:
                patches += 1
                counter_nums[i] = i
            sum_temp += 0 if i not in counter_nums else counter_nums[i]
            if i >= max_num:
                i = sum_temp + 1
                max_num = i
            else:
                i +=1
        return patches

    def leet_code(self, nums: [], n:int):
        miss = 1
        i = 0
        added = 0
        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                miss += miss
                added += 1
        return added


solution = Solution()
print(solution.action([1,3], 6))
print(solution.action([1,5,10], 20))
print(solution.action([1,2,2], 5))
print(solution.action([1,2,31,33], 2147483647))

#code toi uu

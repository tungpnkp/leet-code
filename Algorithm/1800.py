# run time:
# memory:
class Solution:
    def action(self, nums: []):
        s=nums[0]
        m=0
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                s += nums[i]
            else:
                m = max(s,m)
                s = nums[i]
        return max(m,s)

solution = Solution()
print(solution.action([10,20,30,5,10,50]))
print(solution.action([10,20,30,40,50]))


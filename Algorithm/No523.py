# run time:
# memory:
class Solution:
    def action(self, nums: [], k: int):
        if len(nums) < 2:
            return False
        prefix_sum = 0
        prefix_mod = {0:1}
        check_tmp = False
        for num in nums:
            prefix_sum += num
            mod = prefix_sum % k
            if num%k != 0:
                if mod in prefix_mod:
                    return True
                else:
                    prefix_mod[mod] = 1
                check_tmp = False
            else:
                if check_tmp:
                    return True
                check_tmp = True
        return False

solution = Solution()
print(solution.action([23,2,4,6,7], 6)) #true
print(solution.action([23,2,6,4,7], 6)) #true
print(solution.action([23,2,6,4,7], 13)) #false
print(solution.action([5,0,0,0], 3))   #true
print(solution.action([23,2,4,6,6], 7)) #true
print(solution.action([23,6,9], 6)) #false
print(solution.action([1,2,12], 6)) #false


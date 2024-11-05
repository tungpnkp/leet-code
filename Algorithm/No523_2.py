# run time:
# memory:
class Solution:
    def action(self, nums: [], k: int):
        if len(nums) < 2 :
            return False
        check_not_first = False
        tmp_sum = 0
        mod_arr = {0:1}
        for num in nums:
            tmp_sum += num
            tmp_mod = tmp_sum % k
            if tmp_mod in mod_arr:
                if check_not_first:
                    return True
                check_not_first = True
                mod_arr[tmp_mod] += 1
            else:
                mod_arr[tmp_mod] = 1

        return False

solution = Solution()
print(solution.action([23,2,4,6,7], 6)) #true
print(solution.action([23,2,6,4,7], 6)) #true
print(solution.action([23,2,6,4,7], 13)) #false
print(solution.action([5,0,0,0], 3))   #true
print(solution.action([23,2,4,6,6], 7)) #true
print(solution.action([23,6,9], 6)) #false
print(solution.action([1,2,12], 6)) #false


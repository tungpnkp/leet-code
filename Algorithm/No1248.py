# run time: 69%
# memory: 75%
class Solution:
    def action(self, nums: [],  k: int):
        tmp = {}
        tmp_count = 1
        result = 0
        j=0
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                tmp[j] = tmp_count
                tmp_count = 1
                if j >= k:
                    result += tmp[j-k] * tmp[j]
                j += 1
            else:
                tmp_count += 1
        if tmp_count != 0 and j>=k:
            result += tmp[j-k] * tmp_count
        return result



    def leet_code(self, nums: [], k: int):
        tmp = {}
        result = 0
        count_odd = 0
        before_first_odd = 0
        after_last_odd = 0
        first_odd_idx = -1
        i = 0
        while i < len(nums):
            if nums[i] % 2 == 1:
                if count_odd == k:
                    result += (before_first_odd + 1) * (after_last_odd + 1)
                    before_first_odd = 0
                    after_last_odd = 0
                    count_odd = 0
                    i = first_odd_idx + 1
                    first_odd_idx = -1
                    continue
                if first_odd_idx == -1:
                    first_odd_idx = i
                count_odd += 1
            else:
                if count_odd == 0:
                    before_first_odd += 1
                elif count_odd == k:
                    after_last_odd += 1
            i += 1
        if count_odd == k:
            result += (before_first_odd + 1) * (after_last_odd + 1)
        return result


solution = Solution()
print(solution.action([2,4,6],  1))
print(solution.action([1,1,2,1,1],  3))
print(solution.action([2,2,2,1,2,2,1,2,2,2],  2))

# code toi uu

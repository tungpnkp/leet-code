# run time:
# memory:
# O(n)
class Solution:
    def action(self, customers: [], grumpy: [], minutes: int):
        dissatisfied_array = []
        result = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                result+= customers[i]
                dissatisfied_array.append(0)
            else:
                dissatisfied_array.append(customers[i])
        max_dissatisfied = sum(dissatisfied_array[0:minutes])
        pre_dissatisfied = max_dissatisfied
        for i in range(minutes,len(dissatisfied_array)):
            now_dissatified = pre_dissatisfied + dissatisfied_array[i] - dissatisfied_array[i-minutes]
            if now_dissatified > max_dissatisfied:
                max_dissatisfied = now_dissatified
            pre_dissatisfied = now_dissatified
        return result + max_dissatisfied




    def leet_code(self, nums: [], k: int):
        return 1


solution = Solution()
print(solution.action([1,0,1,2,1,1,7,5],  [0,1,0,1,0,1,0,1], 3))
print(solution.action([1],  [0], 1))

# code toi uu

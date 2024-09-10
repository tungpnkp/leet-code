class Solution:
    def plusOne(self, digits: []) -> []:
        number_str = ''.join(map(str, digits))
        result = int(number_str) + 1
        return [int(digit) for digit in str(result)]
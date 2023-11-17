# https://leetcode.com/problems/find-unique-binary-string/

import numpy

class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        bits = len(nums.__getitem__(0))
        numbers_for_bits = range(0, self.__convert_binary_to_number__('1' * bits) + 1)

        numbers = list()
        for binary in map(str, nums):
            numbers.append(self.__convert_binary_to_number__(binary))
        
        numbers = numpy.unique(numbers)
        numbers.sort()

        missing_number = None
        for i in numbers_for_bits:
            res = False
            for y in numbers:
                if y == i:
                    res = True
                    break
            if res is False:
                missing_number = i
                break

        # Could be a replacement for the above code, but, leetcode tells it doubles the runtime :O
        # missing_number = set(numbers_for_bits).difference(numbers).pop()

        if missing_number is not None:
            return self.__convert_number_to_binary__(missing_number).zfill(bits)

    def __convert_number_to_binary__(self, number) -> str:
        return bin(number).replace("0b", "")
    
    def __convert_binary_to_number__(self, binary) -> int:
        return int(binary, 2)

solution = Solution()

nums = list()
nums.append('11')
nums.append('01')
nums.append('10')
# nums.append('00')

print(solution.findDifferentBinaryString(nums))
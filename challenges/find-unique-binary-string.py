# https://leetcode.com/problems/find-unique-binary-string/

import numpy

class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        bits = len(nums.__getitem__(0))
        numbers_for_bits = range(1, self.__convert_binary_to_number__('1' * bits))

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

        if missing_number is not None:
            return self.__convert_number_to_binary__(missing_number)

    def __convert_number_to_binary__(self, number) -> int:
        return bin(number)[2:]
    
    def __convert_binary_to_number__(self, binary) -> int:
        return int(binary, 2)

solution = Solution()

nums = list()
nums.append('10')


print(solution.findDifferentBinaryString(nums))
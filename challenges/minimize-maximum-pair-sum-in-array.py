# https://leetcode.com/problems/minimize-maximum-pair-sum-in-array

class Solution:
    def minPairSum(self, nums: list[int]) -> int:
        nums.sort()

        i = 0
        j = len(nums) - 1

        groups = list()
        while i < j:
            groups.append(nums[i]+nums[j])
            i += 1
            j -= 1

        return max(groups)

solution = Solution()

nums = list()
nums.append(3)
nums.append(2)
nums.append(4)
nums.append(1)
nums.append(1)
nums.append(5)
nums.append(1)
nums.append(3)
nums.append(5)
nums.append(1)

print(solution.minPairSum(nums))
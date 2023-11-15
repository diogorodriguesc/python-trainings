# https://leetcode.com/problems/unique-length-3-palindromic-subsequences/

import numpy

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        letterIndexes = dict()
        for index, letter in enumerate(s):
            if not letterIndexes.get(letter):
                letterIndexes[letter] = list()
                letterIndexes[letter].append(index)
            else:
                letterIndexes[letter].append(index)

        palindromics = list()
        for letterA in letterIndexes.keys():
            if len(letterIndexes[letterA]) >= 3:
                palindromics.append("%s%s%s" % (letterA, letterA, letterA))
            
            for letterB in letterIndexes.keys():
                if letterA is not letterB and len(letterIndexes[letterA]) >=2 and len(letterIndexes[letterB]) >= 1:
                    palindromics.append("%s%s%s" % (letterA, letterB, letterA))

        print(palindromics)

        return len(numpy.unique(palindromics))

solution = Solution()

print(solution.countPalindromicSubsequence("bbcbaba"))
# https://leetcode.com/problems/unique-length-3-palindromic-subsequences/

import numpy

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        print("input %s" % (s))
    
        countLetters = dict()
        letterIndexes = dict()
        for index, letter in enumerate(s):
            countLetters[letter] = (countLetters[letter] if countLetters.get(letter) else 0) + 1
            if not letterIndexes.get(letter):
                letterIndexes[letter] = list()
                letterIndexes[letter].append(index)
            else:
                letterIndexes[letter].append(index)

        print(letterIndexes)

        palindromics = list()
        for indexX, letterA in enumerate(countLetters):
            if countLetters[letterA] >= 3:
                palindromics.append("%s%s%s" % (letterA, letterA, letterA))
            
            for indexY, letterB in enumerate(countLetters):
                print(letterB)
                print(letterIndexes[letterA][:1])
                print(letterIndexes[letterB][:1])
                print(letterIndexes[letterA][:1] > letterIndexes[letterB][:1])
                if letterA is not letterB and countLetters[letterA] >=2 and countLetters[letterB] >= 1:
                    palindromics.append("%s%s%s" % (letterA, letterB, letterA))

        print(countLetters)
        print(palindromics)

        return len(numpy.unique(palindromics))

solution = Solution()

print(solution.countPalindromicSubsequence("bbcbaba"))
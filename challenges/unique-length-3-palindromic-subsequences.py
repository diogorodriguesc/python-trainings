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
        for candidateBoundaryLetter in letterIndexes.keys():
            if len(letterIndexes[candidateBoundaryLetter]) >= 3:
                palindromics.append("%s%s%s" % (candidateBoundaryLetter, candidateBoundaryLetter, candidateBoundaryLetter))
            
            for candidateMiddleLetter in letterIndexes.keys():
                if candidateBoundaryLetter is not candidateMiddleLetter and len(letterIndexes[candidateBoundaryLetter]) >= 2 and len(letterIndexes[candidateMiddleLetter]) >= 1 and min(letterIndexes[candidateBoundaryLetter]) < max(letterIndexes[candidateMiddleLetter]) and max(letterIndexes[candidateBoundaryLetter]) > min(letterIndexes[candidateMiddleLetter]):
                    palindromics.append("%s%s%s" % (candidateBoundaryLetter, candidateMiddleLetter, candidateBoundaryLetter))

        print(palindromics)

        return len(numpy.unique(palindromics))

solution = Solution()

print(solution.countPalindromicSubsequence("bbcbaba")) # return 4 [OKAY!]
print(solution.countPalindromicSubsequence("tlpjzdmtwderpkpmgoyrcxttiheassztncqvnfjeyxxp")) # should return 161 accordingly with leetcode - returning 189 with this version.
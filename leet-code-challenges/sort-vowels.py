# https://leetcode.com/problems/sort-vowels-in-a-string/

class Solution:
    vowels = ["a","e","i","o","u"]

    def sortVowels(self, s: str) -> str:
        t: str = ""
        vowels_in_s: list = list()
        for letter in s:
            if letter.lower() in Solution.vowels:
                vowels_in_s.append(letter)

        sorted_vowels_in_s = sorted(vowels_in_s)

        iterator = 0;
        for letter in s:
            if letter.lower() in Solution.vowels:
                t = t + sorted_vowels_in_s[iterator]
                iterator = iterator + 1
            else: 
                t = t + letter

        return t

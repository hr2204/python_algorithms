# 438. Find All Anagrams in a String
# Difficulty: Easy
# Contributors: Stomach_ache
# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
#
# Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.
#
# The order of output does not matter.
#
# Example 1:
#
# Input:
# s: "cbaebabacd" p: "abc"
#
# Output:
# [0, 6]
#
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# Example 2:
#
# Input:
# s: "abab" p: "ab"
#
# Output:
# [0, 1, 2]
#
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
from collections import Counter


class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        count_p = Counter(p)
        res = []
        count_s = Counter(s[0:0+len(p)])
        if count_s == count_p:
            res.append(0)
        for i in range(1,len(s)-len(p)+1):
            count_s[s[i-1]] -= 1
            if count_s[s[i-1]] == 0:
                del count_s[s[i-1]]
            count_s[s[i+len(p)-1]] += 1
            if  count_p == count_s:
                res.append(i)
        return res


    # LTE version
    def findAnagrams_LTE(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []
        for i in range(len(s)):
            temp = sorted(s[i:i + len(p)])
            if temp == sorted(p):
                res.append(i)
        return res


if __name__ == '__main__':
    s = "cbaebabacd"
    p = "abc"
    print Solution().findAnagrams(s, p)

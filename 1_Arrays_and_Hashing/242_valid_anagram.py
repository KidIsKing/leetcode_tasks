"""https://leetcode.com/problems/valid-anagram/description/"""


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if t[::-1] == s:
            return True
        return False


def main():
    S = Solution()
    print(S.isAnagram(s="anagram", t="nagaram"))  # true
    print(S.isAnagram(s="anagram", t="nagaram"))  # true


if __name__ == "__main__":
    main()

"""https://leetcode.com/problems/valid-anagram/description/"""


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if sorted(s) == sorted(t):
            return True
        return False


def main():
    S = Solution()
    print(S.isAnagram(s="anagram", t="nagaram"))  # true
    print(S.isAnagram(s="rat", t="car"))  # false


if __name__ == "__main__":
    main()

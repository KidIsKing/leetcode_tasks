"""https://leetcode.com/problems/concatenation-of-array/"""


class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return nums*2


def main():
    S = Solution()
    print(S.getConcatenation([1, 2, 1]))  # [1, 2, 1, 1, 2, 1]
    print(S.getConcatenation([1, 3, 2, 1]))  # [1, 3, 2, 1, 1, 3, 2, 1]


if __name__ == "__main__":
    main()

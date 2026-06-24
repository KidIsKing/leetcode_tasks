"""https://leetcode.com/problems/contains-duplicate/submissions/2044688392/"""


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # O(n^2) - выход за временные рамки при тестировании
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False

        if len(set(nums)) < len(nums):
            return True
        return False


def main():
    S = Solution()
    print(S.containsDuplicate([1, 2, 3, 1]))  # true
    print(S.containsDuplicate([1, 2, 3, 4]))  # false
    print(S.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  # true


if __name__ == "__main__":
    main()

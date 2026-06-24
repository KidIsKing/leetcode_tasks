"""https://leetcode.com/problems/contains-duplicate-ii/"""


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # Быстарая проверка на наличие дубликата
        if len(set(nums)) >= len(nums):
            return False

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if i != j and nums[i] == nums[j] and abs(i - j) <= k:
                    return True
        return False


def main():
    S = Solution()
    print(S.containsNearbyDuplicate(nums=[1, 2, 3, 1], k=3))  # true
    print(S.containsNearbyDuplicate(nums=[1, 0, 1, 1], k=1))  # true
    print(S.containsNearbyDuplicate(nums=[1, 2, 3, 1, 2, 3], k=2))  # false


if __name__ == "__main__":
    main()

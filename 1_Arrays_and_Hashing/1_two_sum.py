class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
                    break
        return None


def main():
    S = Solution()
    print(S.twoSum(nums=[2, 7, 11, 15], target=9))  # [0,1]
    print(S.twoSum(nums=[3, 2, 4], target=6))  # [1,2]
    print(S.twoSum(nums=[3, 3], target=6))  # [0,1]


if __name__ == "__main__":
    main()

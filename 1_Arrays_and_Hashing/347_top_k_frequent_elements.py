"""https://leetcode.com/problems/top-k-frequent-elements/description/"""


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        result = []
        nums_set = set(sorted(nums))
        nums_counts = []
        # Записываем пары элементов: элемент и его количество в исходном массиве
        for num in nums_set:
            nums_counts.append([nums.count(num), num])
        nums_counts = sorted(nums_counts, reverse=True)
        # Смотря на количество k, выбираем нужное количество чисел в отсортированном списке
        for i in range(k):
            result.append(nums_counts[i][1])  # 1 - индекс элементов, которые повторяются
        return result


def main():
    S = Solution()
    print(S.topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2))  # [1,2]
    print(S.topKFrequent(nums=[1], k=1))  # [1,2]
    print(S.topKFrequent(nums=[1, 2, 1, 2, 1, 2, 3, 1, 3, 2], k=2))  # [1,2]


if __name__ == "__main__":
    main()

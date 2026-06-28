"""https://leetcode.com/problems/group-anagrams/description/"""


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = {}
        for s in strs:
            key = "".join(sorted(s))
            result[key] = result.get(key, []) + [s]

        return list(result.values())


def main():
    S = Solution()
    print(S.groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))  # [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    print(S.groupAnagrams(strs=[""]))  # [[""]]
    print(S.groupAnagrams(strs=["a"]))  # [["a"]]


if __name__ == "__main__":
    main()

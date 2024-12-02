class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        dup = []
        non_unique = False
        for num in nums:
            if num not in dup:
                dup.append(num)
            else:
                non_unique = True
        return non_unique



Y = Solution()
Y.hasDuplicate([1,2,2])

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        indices = {}  # val -> index

        for i, n in enumerate(nums):
            indices[n] = i

        for i, n in enumerate(nums):
            diff = target - n
            if diff in indices and indices[diff] != i:
                return [i, indices[diff]]
            
Y = Solution()
Y.twoSum([3,4,5,6], 7)

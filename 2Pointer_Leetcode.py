class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        total_nums = nums1+nums2
        total_nums = sorted(total_nums)
        test = len(total_nums)

        if (test % 2) != 0:
            #odd
            X = len(total_nums)/2
            X = X - 0.5
            X = int(X)
            solution = total_nums[X]
        else:
            X = len(total_nums)/2
            X = int(X)
            solution = (total_nums[X-1] + total_nums[X])/2
        print(solution)
        return solution





nums1 = [1,3,6]
nums2 = [2,4,5]

x = Solution()  
x.findMedianSortedArrays(nums1,nums2)
         
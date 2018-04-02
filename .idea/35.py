class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            result = nums.index(target)
            return result
        else :
            nums.append(target)
            nums.sort()
            result=nums.index(target)
            return result
if __name__ == "__main__":
    print Solution().searchInsert([1,3],2)

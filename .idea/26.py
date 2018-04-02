class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result=0
        if len(nums)==0 :
            return 0
        for i in range(len(nums)-2) :
            if nums[i+1]==None :
                break
            if nums[i]==nums[i+1] :
                del nums[i]
        return nums
if __name__ == "__main__":
    print Solution().removeDuplicates([1,1,3])
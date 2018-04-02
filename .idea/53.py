class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum=['']
        result=0
        num=len(nums)
        for i in range(num) :
            for j in range(num-i) :
                k=j
                for k in range(j+i) :
                    sum.append(nums[k])
        result=max(sum)
if __name__ == "__main__":
    print Solution().maxSubArray([1,3,2])
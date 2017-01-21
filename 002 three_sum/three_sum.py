class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        length=len(nums)
        res=[]
        for i in range(length):
            if i!=0 and nums[i] == nums[i-1]: continue
            target = -nums[i]
            l = i+1
            r = length-1
            
            while l<r :
                if nums[l]+nums[r]==target:
                    res.append((nums[i],nums[l],nums[r]))
                    while l<r and nums[l] == nums[l+1]: l+=1
                    while l<r and nums[r] == nums[r-1]: r-=1
                    l+=1 
                    r-=1
                elif nums[l]+nums[r] > target: r-=1
                else: l+=1
        return res
                
if __name__=='__main__':
        a = Solution()          
        nums = [-3,-5,-2,3,6,9,-1,7,4,2]
        print (a.threeSum(nums))
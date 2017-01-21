class Solution(object):
    def twoSum(self,nums,target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if (nums[j]==target - nums[i]):
                    return (i,j)
        return (0,0)

    def twoSum_hash(self,nums,target):
        dict={}
        n = len(nums)
        i = 0
        for number in nums:
            dict[number]=i
            i+=1
            
        for j in range(n): 
            complement = target - nums[j]
            if complement in dict:
                key = dict.get(complement)
                if key != j:
                    break
        return (j,key)
    
        
if __name__=='__main__':
   
    a = Solution()   
    nums = [3,2,4]
    target = 6
#    (i,j)= a.twoSum(nums, target)
    (i,j)= a.twoSum_hash(nums, target)
    print(i,j)
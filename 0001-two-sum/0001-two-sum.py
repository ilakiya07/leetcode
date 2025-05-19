class Solution:
    def twoSum(self, nums, target):
        num_len=len(nums)
        for i in range(num_len):
            for j in range(i+1 ,num_len):
              if((nums[i]+nums[j])==target):
                return[i,j]
                return
                
              
        print("no match found")

nums=[2,7,11,15]    

obj=Solution()
result=obj.twoSum(nums,10)
print("index are",result)


        
        
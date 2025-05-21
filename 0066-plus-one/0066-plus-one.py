class Solution():
    def plusOne(self, digits):
        c=""
        d=0
        list=[]
        for i in range(len(digits)):
            c+=str(digits[i])
        d=int(c)
        d+=1
        
        

        for i in str(d):
            list.append(int(i))
            
        return list
        
        
            
        

digits=[1,2,3]
obj=Solution()
res=obj.plusOne(digits)
print(res)

        






   









   











       
        
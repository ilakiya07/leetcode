class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        

        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        maxi=max(d.values())
        total=0
        for i in d.values():
            if i==maxi:
                total+=maxi
        return total
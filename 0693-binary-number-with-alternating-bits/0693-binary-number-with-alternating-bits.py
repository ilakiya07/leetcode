class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        prev=n%2#1
        n=n//2#2

        while n>0:
            current=n%2
            if prev==current:
                return False
            prev=current
            n=n//2
        return True

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        r = 0
        result = 0
        while result<=n:
            result = 3**r
            r+=1
            if result==n:
                return True
        return False
        

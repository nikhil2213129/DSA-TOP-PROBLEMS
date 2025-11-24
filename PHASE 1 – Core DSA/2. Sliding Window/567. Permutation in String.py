class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        l=len(s1) #getting the length of both the strings
        n=len(s2)
        if l>n: #if second one is already greater
            return False
        m1=[0]*26 #making two maps to store frequency of every letter
        m2=[0]*26
        for i in range(l): #traversing the first string
            m1[ord(s1[i])-97]+=1
            m2[ord(s2[i])-97]+=1 #also updating the 2nd string map
        if m1==m2: #if the both maps equal i.e have same letters
            return True
        for i in range(l,n): #check for all using sliding window
            m2[ord(s2[i])-97]+=1
            m2[ord(s2[i-l])-97]-=1
            if m1==m2:
                return True # true if found a window = Permutation 
        return False #if no string was a permutation

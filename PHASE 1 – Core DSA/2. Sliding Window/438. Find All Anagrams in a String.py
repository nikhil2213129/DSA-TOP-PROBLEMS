from collections import Counter

class Solution(object):
    def findAnagrams(self, s, p):
        res = []
        len_p = len(p)
        len_s = len(s)
        
        if len_s < len_p:
            return res
        
        p_count = Counter(p)
        window_count = Counter(s[:len_p-1])
        
        for i in range(len_p - 1, len_s):
            window_count[s[i]] += 1  # include rightmost char in the window
            
            if window_count == p_count:
                res.append(i - len_p + 1)
            
            left_char = s[i - len_p + 1]
            window_count[left_char] -= 1 
            if window_count[left_char] == 0:
                del window_count[left_char] 
        return res

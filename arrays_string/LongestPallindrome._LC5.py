# TOPIC: Two pointer, DP

class Solution(object):
    def longestPalindrome(self, s): # 2 pointer
        out = ''
        for i in range(len(s)):
            l, r = i, i
            # odd length
            while (l >= 0 and r < len(s) and s[l] == s[r]):
                if (r - l + 1) > len(out):
                    out =  s[l:r+1]
                l -= 1
                r += 1

            l , r = i, i + 1
            # Even length
            while (l >= 0 and r < len(s) and s[l] == s[r]):
                if (r - l + 1) > len(out):
                    out = s[l:r+1]
                l -= 1
                r += 1
        
        return out

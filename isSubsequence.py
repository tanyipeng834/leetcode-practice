class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_pointer =0
        t_pointer =0
        # Have two pointer for the word

        while(s_pointer<len(s) and t_pointer<len(t)):
            if t[t_pointer]==s[s_pointer]:
                s_pointer +=1
            t_pointer +=1
        if s_pointer != len(s):
            return False
        else:
            return True

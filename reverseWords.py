class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        str_list = s.split()
        rev_list = str_list[::-1]
        for i in range(len(rev_list)):

            rev_list[i] = rev_list[i].strip()
        print(rev_list)

        new_str = " ".join(rev_list)
        return new_str
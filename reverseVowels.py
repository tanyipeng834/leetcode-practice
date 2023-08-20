class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = "aeiouAEIOU"
        stack =[]
        newStr =""
       
        for i in range(len(s)):
            if s[i] in vowels:
                stack.append(s[i])
        for i in range(len(s)):
            if s[i] in vowels:
                newStr+=stack.pop()
            else:
                newStr+=s[i]       
        return newStr
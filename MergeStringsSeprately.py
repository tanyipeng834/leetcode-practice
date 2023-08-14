class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        newstr =""
        i =0
        j =0
        count =0
        while(i<len(word1) and  j<len(word2)):
            if count%2 ==0:
                newstr+= word1[i]
                i+=1
            else:
                newstr+= word2[j]
                j+=1
            if (i == len(word1)):
                while(j<len(word2)):
                    newstr+=word2[j]
                    j+=1
            elif (j==len(word2)):
                while(i<len(word1)):
                    newstr+=word1[i]
                    i+=1
            count +=1
        return newstr

            

            
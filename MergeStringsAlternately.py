class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        if len(word1) < len(word2):
            shorter_word = word1
            longer_word = word2
        else:
            shorter_word = word2
            longer_word = word1

        merged_str = ""
        for i in range(len(shorter_word)):
            merged_str += word1[i]
            merged_str += word2[i]

        merged_str += longer_word[len(shorter_word):]

        return merged_str
class Solution:
    
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dict_occurence = dict()
        set_occurence = set()
        for nums in arr:
            if nums not in dict_occurence:
                dict_occurence[nums]=1
            else:
                dict_occurence[nums]+=1
        for value in dict_occurence.values():
            set_occurence.add(value)
        if len(set_occurence) == len(dict_occurence):
            return True
        else:
            return False
        
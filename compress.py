class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        count = 1  # Start count at 1, as there is at least one occurrence of the first character
        result_index = 0  # Index for the result string
        # Take care of the edge case of the first character not being processed
        for i in range(1, len(chars)):
            if chars[i] == chars[i-1]:
                # put the index as before 
                count +=1
            # Take the scenario where it is not the same as before
            else:
                # Take care of the charater first
                chars[result_index] = chars[i-1]
                result_index +=1
                
                if count >1:
                    for digit in str(count):
                        chars[result_index] = digit
                        result_index+=1

                count =1
        # Now take care of the last group
        chars[result_index] = chars[-1]
        result_index +=1
        if count >1:
            for digit in str(count):
                chars[result_index]= digit
                result_index +=1
        return result_index
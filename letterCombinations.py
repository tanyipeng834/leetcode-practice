class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Space Complexity would be O(N) recurision directly propotional to the n elements
        # Time complexity would be (4^n)
        combinations = []
        phone_number = { "2" : "abc",
         "3" : "def",
         "4":"ghi",
         "5" : "jkl",
         "6" : "mno",
         "7" :"pqrs",
         "8" : "tuv",
         "9" :"wxyz",
        }
        def backtrack(current_number,digits):
            if digits =="":
                if current_number !="":
                    combinations.append(current_number)
                return
            else:
                digit = digits[0]
                letters = phone_number[digit]
                for letter in letters:
                   
                    backtrack(current_number + letter,digits[1:])
                    
        backtrack("",digits)
        return combinations
                


          

       










        
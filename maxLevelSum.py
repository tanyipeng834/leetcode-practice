from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        number_of_elements =1
        queue = deque()
        queue.append(root)
        current_sum = 0
        max_sum = root.val
        max_level =1
        next_level =0
        current_level =1
        while number_of_elements>0:
            current = queue.popleft()
            current_sum += current.val
            number_of_elements -=1
            if current.left:
                queue.append(current.left)
                next_level+=1
            if current.right:
                queue.append(current.right)
                next_level +=1
            # End the current level , then we would set to the next level
            if number_of_elements ==0:
                number_of_elements = next_level
                
                
                next_level =0
                if current_sum >max_sum:
                    max_level = current_level
                    max_sum = current_sum
                current_sum =0
                current_level +=1
        return max_level



class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # (2,8) , (10,16)
        # Sort this by the starting time
        intersections =0
        sorted_point_list = sorted(points, key=lambda x:x[0])
        stack = []
        stack.append(sorted_point_list[0])
        for i in range(1,len(sorted_point_list)):
            # Check if there is any intersection with the stack and the new element
            intersect_time =self.check_intersect(stack[-1],sorted_point_list[i])
            if(intersect_time):
                print(intersect_time)
                stack.pop()
                stack.append(intersect_time)
            else:
                stack.append(sorted_point_list[i])
        return len(stack)

            
    # timing_1 would take a smaller value than timing_2
    def check_intersect(self,timing_1,timing_2):
        # Check if the start time is smaller than the end time
        if timing_1[1]>=timing_2[0]:
            return [timing_2[0],min(timing_1[1],timing_2[1])]

        
        else:
            return None




        
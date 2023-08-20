lass Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current= head
        # Using a stack to reverse the linked list
        stack =[]
        while current is not None and  current.next is not None:
            
            stack.append(current)
            current = current.next

        new_head = current
        new_current = new_head
       
        while len(stack)>0:
            
            next_pointer= stack.pop()
            print(new_current)
            print(next_pointer)
            
            new_current.next= next_pointer
            new_current.next.next = None
            new_current = new_current.next
            
       
            
        
        
        return new_head
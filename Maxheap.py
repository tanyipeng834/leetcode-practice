class MaxHeap:


    def __init__(self):
        self.heap=[]
    # K would be the index of the element
    def swim(self,k):
        while k>0 and self.heap[(k-1)//2] < self.heap[k]:
            # Exhcange values with the parent
            self.heap[(k-1)//2],self.heap[k] = self.heap[k],self.heap[(k-1)//2]
            # Swim Towards the root
            k =(k-1)//2
    def sink(self,k,n):
        # Check if there is a left child to sink in 
        while 2*k +1<n:
            # This is the left child
            # The left child would be 2*k +1
            # The right child would be 2* k+2
            j = 2*k +1 
            if j+1<n and self.heap[j] < self.heap[j+1]:
                j+=1
            if self.heap[k] >= self.heap[j]:
                break
            self.heap[k], self.heap[j] = self.heap[j] , self.heap[k]
            # Update k to be the greater child
            k = j
    def insert(self,value):
        self.heap.append(value)
        self.swim((len(self.heap)-1))
    
    def delete_max(self):
        if not self.heap:
            return None
        # The head of the 
        max_value = self.heap[0]
        # Replace the head of the heap with the last element
        self.heap[0] = self.heap[-1]
        # Remove the last element
        self.heap.pop()
        self.sink(0,len(self.heap))
        return max_value
    def heap_sort(self):
        n = len(self.heap)
        # Build the max heap by targeting the non leaf nodes
        # Sink the parent with the children nodes
        for i in range(n//2-1,-1,-1):
            self.sink(i,n)

        # Delete the maximum element
        # sorted array 
        sorted_array =[]
        for i in range(n):
            max_value = self.delete_max()
            sorted_array.insert(0,max_value)
        return sorted_array

        
# Example usage:
max_heap = MaxHeap()
max_heap.insert(10)
max_heap.insert(5)
max_heap.insert(20)
max_heap.insert(15)

sorted_array = max_heap.heap_sort()
print("Sorted array:", sorted_array)









"""
Heap Data Structure Implementation (Min Heap and Max Heap)
"""

class Heap:
    def __init__(self, heap_type="min"):
        self.heap = []
        self.heap_type = heap_type  # "min" or "max"
        self.history = []
    
    def _parent(self, index):
        """Get parent index"""
        return (index - 1) // 2
    
    def _left_child(self, index):
        """Get left child index"""
        return 2 * index + 1
    
    def _right_child(self, index):
        """Get right child index"""
        return 2 * index + 2
    
    def _compare(self, a, b):
        """Compare two values based on heap type"""
        if self.heap_type == "min":
            return a < b
        else:
            return a > b
    
    def _heapify_up(self, index):
        """Maintain heap property upward"""
        while index > 0:
            parent_index = self._parent(index)
            if not self._compare(self.heap[index], self.heap[parent_index]):
                break
            
            # Swap with parent
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index
    
    def _heapify_down(self, index):
        """Maintain heap property downward"""
        while True:
            smallest_or_largest = index
            left = self._left_child(index)
            right = self._right_child(index)
            
            # Compare with left child
            if (left < len(self.heap) and 
                self._compare(self.heap[left], self.heap[smallest_or_largest])):
                smallest_or_largest = left
            
            # Compare with right child
            if (right < len(self.heap) and 
                self._compare(self.heap[right], self.heap[smallest_or_largest])):
                smallest_or_largest = right
            
            # If no change needed, break
            if smallest_or_largest == index:
                break
            
            # Swap and continue
            self.heap[index], self.heap[smallest_or_largest] = self.heap[smallest_or_largest], self.heap[index]
            index = smallest_or_largest
    
    def insert(self, value):
        """Insert a value into the heap"""
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)
        self.history.append(f"Inserted {value} into {self.heap_type} heap")
        return True, f"Successfully inserted {value}"
    
    def extract(self):
        """Extract the root element (min or max)"""
        if not self.heap:
            return None, f"{self.heap_type.title()} heap is empty"
        
        if len(self.heap) == 1:
            root = self.heap.pop()
            self.history.append(f"Extracted {root} from {self.heap_type} heap")
            return root, f"Extracted {root}"
        
        # Store root and replace with last element
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        
        self.history.append(f"Extracted {root} from {self.heap_type} heap")
        return root, f"Extracted {root}"
    
    def peek(self):
        """Peek at the root element without removing it"""
        if not self.heap:
            return None, f"{self.heap_type.title()} heap is empty"
        
        root = self.heap[0]
        self.history.append(f"Peeked at root: {root}")
        return root, f"Root element is {root}"
    
    def delete(self, value):
        """Delete a specific value from the heap"""
        try:
            index = self.heap.index(value)
        except ValueError:
            return False, f"Value {value} not found in heap"
        
        # Replace with last element
        last_element = self.heap.pop()
        
        if index < len(self.heap):
            self.heap[index] = last_element
            
            # Heapify both up and down to maintain heap property
            parent_index = self._parent(index)
            if (index > 0 and 
                self._compare(self.heap[index], self.heap[parent_index])):
                self._heapify_up(index)
            else:
                self._heapify_down(index)
        
        self.history.append(f"Deleted {value} from {self.heap_type} heap")
        return True, f"Successfully deleted {value}"
    
    def build_heap(self, array):
        """Build heap from an array"""
        self.heap = array.copy()
        
        # Start from last non-leaf node and heapify down
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self._heapify_down(i)
        
        self.history.append(f"Built {self.heap_type} heap from array: {array}")
        return True, f"Successfully built heap from array"
    
    def heap_sort(self):
        """Perform heap sort and return sorted array"""
        if not self.heap:
            return [], "Heap is empty"
        
        original_heap = self.heap.copy()
        sorted_array = []
        
        while self.heap:
            root, _ = self.extract()
            sorted_array.append(root)
        
        # Restore original heap
        self.heap = original_heap
        
        # For min heap, reverse to get ascending order
        if self.heap_type == "min":
            sorted_array.reverse()
        
        self.history.append(f"Performed heap sort: {sorted_array}")
        return sorted_array, f"Heap sort completed: {sorted_array}"
    
    def get_heap_array(self):
        """Get heap as array for visualization"""
        return self.heap.copy()
    
    def get_tree_structure(self):
        """Get heap as tree structure for visualization"""
        if not self.heap:
            return None
        
        return self._build_tree_dict(0)
    
    def _build_tree_dict(self, index):
        """Helper method to build tree dictionary"""
        if index >= len(self.heap):
            return None
        
        left_index = self._left_child(index)
        right_index = self._right_child(index)
        
        return {
            'data': self.heap[index],
            'index': index,
            'left': self._build_tree_dict(left_index) if left_index < len(self.heap) else None,
            'right': self._build_tree_dict(right_index) if right_index < len(self.heap) else None
        }
    
    def size(self):
        """Get heap size"""
        return len(self.heap)
    
    def is_empty(self):
        """Check if heap is empty"""
        return len(self.heap) == 0
    
    def clear(self):
        """Clear the heap"""
        self.heap.clear()
        self.history.append(f"{self.heap_type.title()} heap cleared")
    
    def get_history(self):
        """Return operation history"""
        return self.history.copy()
    
    def clear_history(self):
        """Clear operation history"""
        self.history.clear()
    
    def __str__(self):
        return f"{self.heap_type.title()} Heap: {self.heap}"

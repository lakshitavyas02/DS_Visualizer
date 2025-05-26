"""
Stack Data Structure Implementation
"""

class Stack:
    def __init__(self, max_size=10):
        self.items = []
        self.max_size = max_size
        self.history = []  # For step-by-step visualization
    
    def push(self, item):
        """Add an item to the top of the stack"""
        if len(self.items) >= self.max_size:
            return False, "Stack Overflow! Maximum size reached."
        
        self.items.append(item)
        self.history.append(f"Pushed {item} onto stack")
        return True, f"Successfully pushed {item}"
    
    def pop(self):
        """Remove and return the top item from the stack"""
        if self.is_empty():
            return None, "Stack Underflow! Stack is empty."
        
        item = self.items.pop()
        self.history.append(f"Popped {item} from stack")
        return item, f"Successfully popped {item}"
    
    def peek(self):
        """Return the top item without removing it"""
        if self.is_empty():
            return None, "Stack is empty"
        
        top_item = self.items[-1]
        self.history.append(f"Peeked at top element: {top_item}")
        return top_item, f"Top element is {top_item}"
    
    def is_empty(self):
        """Check if the stack is empty"""
        return len(self.items) == 0
    
    def is_full(self):
        """Check if the stack is full"""
        return len(self.items) >= self.max_size
    
    def size(self):
        """Return the current size of the stack"""
        return len(self.items)
    
    def clear(self):
        """Clear all items from the stack"""
        self.items.clear()
        self.history.append("Stack cleared")
    
    def get_items(self):
        """Return a copy of the stack items"""
        return self.items.copy()
    
    def get_history(self):
        """Return the operation history"""
        return self.history.copy()
    
    def clear_history(self):
        """Clear the operation history"""
        self.history.clear()
    
    def __str__(self):
        if self.is_empty():
            return "Stack: []"
        return f"Stack: {self.items} (top: {self.items[-1]})"
    
    def __repr__(self):
        return self.__str__()

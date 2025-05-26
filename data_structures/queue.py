"""
Queue Data Structure Implementation
"""

class Queue:
    def __init__(self, max_size=10):
        self.items = []
        self.max_size = max_size
        self.history = []  # For step-by-step visualization
    
    def enqueue(self, item):
        """Add an item to the rear of the queue"""
        if len(self.items) >= self.max_size:
            return False, "Queue Overflow! Maximum size reached."
        
        self.items.append(item)
        self.history.append(f"Enqueued {item} to queue")
        return True, f"Successfully enqueued {item}"
    
    def dequeue(self):
        """Remove and return the front item from the queue"""
        if self.is_empty():
            return None, "Queue Underflow! Queue is empty."
        
        item = self.items.pop(0)
        self.history.append(f"Dequeued {item} from queue")
        return item, f"Successfully dequeued {item}"
    
    def front(self):
        """Return the front item without removing it"""
        if self.is_empty():
            return None, "Queue is empty"
        
        front_item = self.items[0]
        self.history.append(f"Viewed front element: {front_item}")
        return front_item, f"Front element is {front_item}"
    
    def rear(self):
        """Return the rear item without removing it"""
        if self.is_empty():
            return None, "Queue is empty"
        
        rear_item = self.items[-1]
        self.history.append(f"Viewed rear element: {rear_item}")
        return rear_item, f"Rear element is {rear_item}"
    
    def is_empty(self):
        """Check if the queue is empty"""
        return len(self.items) == 0
    
    def is_full(self):
        """Check if the queue is full"""
        return len(self.items) >= self.max_size
    
    def size(self):
        """Return the current size of the queue"""
        return len(self.items)
    
    def clear(self):
        """Clear all items from the queue"""
        self.items.clear()
        self.history.append("Queue cleared")
    
    def get_items(self):
        """Return a copy of the queue items"""
        return self.items.copy()
    
    def get_history(self):
        """Return the operation history"""
        return self.history.copy()
    
    def clear_history(self):
        """Clear the operation history"""
        self.history.clear()
    
    def __str__(self):
        if self.is_empty():
            return "Queue: []"
        return f"Queue: {self.items} (front: {self.items[0]}, rear: {self.items[-1]})"
    
    def __repr__(self):
        return self.__str__()

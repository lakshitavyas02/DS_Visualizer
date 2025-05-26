"""
Linked List Data Structure Implementation
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None  # For doubly linked list

class LinkedList:
    def __init__(self, doubly=False):
        self.head = None
        self.tail = None  # For doubly linked list
        self.doubly = doubly
        self.size = 0
        self.history = []
    
    def insert_at_beginning(self, data):
        """Insert a node at the beginning of the list"""
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            if self.doubly:
                self.tail = new_node
        else:
            new_node.next = self.head
            if self.doubly:
                self.head.prev = new_node
            self.head = new_node
        
        self.size += 1
        self.history.append(f"Inserted {data} at beginning")
        return True, f"Successfully inserted {data} at beginning"
    
    def insert_at_end(self, data):
        """Insert a node at the end of the list"""
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            if self.doubly:
                self.tail = new_node
        else:
            if self.doubly and self.tail:
                self.tail.next = new_node
                new_node.prev = self.tail
                self.tail = new_node
            else:
                current = self.head
                while current.next:
                    current = current.next
                current.next = new_node
                if self.doubly:
                    new_node.prev = current
                    self.tail = new_node
        
        self.size += 1
        self.history.append(f"Inserted {data} at end")
        return True, f"Successfully inserted {data} at end"
    
    def insert_at_position(self, data, position):
        """Insert a node at a specific position"""
        if position < 0 or position > self.size:
            return False, "Invalid position"
        
        if position == 0:
            return self.insert_at_beginning(data)
        
        if position == self.size:
            return self.insert_at_end(data)
        
        new_node = Node(data)
        current = self.head
        
        for i in range(position - 1):
            current = current.next
        
        new_node.next = current.next
        current.next = new_node
        
        if self.doubly:
            new_node.prev = current
            if new_node.next:
                new_node.next.prev = new_node
        
        self.size += 1
        self.history.append(f"Inserted {data} at position {position}")
        return True, f"Successfully inserted {data} at position {position}"
    
    def delete(self, data):
        """Delete the first occurrence of data"""
        if self.head is None:
            return False, "List is empty"
        
        # If head node contains the data
        if self.head.data == data:
            self.head = self.head.next
            if self.doubly and self.head:
                self.head.prev = None
            elif self.doubly:
                self.tail = None
            self.size -= 1
            self.history.append(f"Deleted {data}")
            return True, f"Successfully deleted {data}"
        
        current = self.head
        while current.next and current.next.data != data:
            current = current.next
        
        if current.next:
            node_to_delete = current.next
            current.next = node_to_delete.next
            
            if self.doubly:
                if node_to_delete.next:
                    node_to_delete.next.prev = current
                else:
                    self.tail = current
            
            self.size -= 1
            self.history.append(f"Deleted {data}")
            return True, f"Successfully deleted {data}"
        
        return False, f"Data {data} not found in list"
    
    def search(self, data):
        """Search for data in the list"""
        current = self.head
        position = 0
        
        while current:
            if current.data == data:
                self.history.append(f"Found {data} at position {position}")
                return position, f"Found {data} at position {position}"
            current = current.next
            position += 1
        
        return -1, f"Data {data} not found in list"
    
    def get_list(self):
        """Return list as array for visualization"""
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result
    
    def clear(self):
        """Clear the entire list"""
        self.head = None
        self.tail = None
        self.size = 0
        self.history.append("List cleared")
    
    def get_history(self):
        """Return the operation history"""
        return self.history.copy()
    
    def clear_history(self):
        """Clear the operation history"""
        self.history.clear()
    
    def __str__(self):
        if self.head is None:
            return "LinkedList: []"
        
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next
        
        arrow = " <-> " if self.doubly else " -> "
        return f"LinkedList: {arrow.join(result)}"

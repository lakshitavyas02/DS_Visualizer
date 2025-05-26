"""
Hash Table Data Structure Implementation
"""

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(self.size)]  # Using chaining for collision resolution
        self.history = []
        self.count = 0
    
    def _hash(self, key):
        """Simple hash function using modulo"""
        if isinstance(key, str):
            return sum(ord(char) for char in key) % self.size
        return hash(key) % self.size
    
    def insert(self, key, value):
        """Insert a key-value pair into the hash table"""
        index = self._hash(key)
        bucket = self.table[index]
        
        # Check if key already exists
        for i, (k, v) in enumerate(bucket):
            if k == key:
                old_value = bucket[i][1]
                bucket[i] = (key, value)
                self.history.append(f"Updated {key}: {old_value} -> {value} at index {index}")
                return True, f"Updated {key} with new value {value}"
        
        # Add new key-value pair
        bucket.append((key, value))
        self.count += 1
        self.history.append(f"Inserted {key}: {value} at index {index}")
        return True, f"Successfully inserted {key}: {value}"
    
    def get(self, key):
        """Get value by key"""
        index = self._hash(key)
        bucket = self.table[index]
        
        for k, v in bucket:
            if k == key:
                self.history.append(f"Found {key}: {v} at index {index}")
                return v, f"Found {key}: {v}"
        
        self.history.append(f"Key {key} not found")
        return None, f"Key {key} not found"
    
    def delete(self, key):
        """Delete a key-value pair"""
        index = self._hash(key)
        bucket = self.table[index]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                deleted_item = bucket.pop(i)
                self.count -= 1
                self.history.append(f"Deleted {key}: {v} from index {index}")
                return True, f"Successfully deleted {key}: {v}"
        
        return False, f"Key {key} not found for deletion"
    
    def contains(self, key):
        """Check if key exists in hash table"""
        index = self._hash(key)
        bucket = self.table[index]
        
        for k, v in bucket:
            if k == key:
                return True, f"Key {key} exists in hash table"
        
        return False, f"Key {key} does not exist in hash table"
    
    def get_all_items(self):
        """Get all key-value pairs"""
        items = []
        for bucket in self.table:
            items.extend(bucket)
        return items
    
    def get_table_state(self):
        """Get current state of the hash table for visualization"""
        return [bucket.copy() for bucket in self.table]
    
    def get_load_factor(self):
        """Calculate load factor"""
        return self.count / self.size
    
    def get_collision_count(self):
        """Count number of collisions (buckets with more than one item)"""
        collisions = 0
        for bucket in self.table:
            if len(bucket) > 1:
                collisions += len(bucket) - 1
        return collisions
    
    def clear(self):
        """Clear all items from hash table"""
        self.table = [[] for _ in range(self.size)]
        self.count = 0
        self.history.append("Hash table cleared")
    
    def get_history(self):
        """Return operation history"""
        return self.history.copy()
    
    def clear_history(self):
        """Clear operation history"""
        self.history.clear()
    
    def is_empty(self):
        """Check if hash table is empty"""
        return self.count == 0
    
    def __str__(self):
        result = "HashTable:\n"
        for i, bucket in enumerate(self.table):
            result += f"  [{i}]: {bucket}\n"
        return result

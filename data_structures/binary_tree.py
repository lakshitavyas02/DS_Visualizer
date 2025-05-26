"""
Binary Tree Data Structure Implementation
"""

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
        self.history = []
        self.traversal_result = []
    
    def insert(self, data):
        """Insert a node into the binary search tree"""
        if self.root is None:
            self.root = TreeNode(data)
            self.history.append(f"Inserted {data} as root")
            return True, f"Successfully inserted {data} as root"
        
        result = self._insert_recursive(self.root, data)
        if result:
            self.history.append(f"Inserted {data}")
            return True, f"Successfully inserted {data}"
        else:
            return False, f"Value {data} already exists in tree"
    
    def _insert_recursive(self, node, data):
        """Helper method for recursive insertion"""
        if data < node.data:
            if node.left is None:
                node.left = TreeNode(data)
                return True
            else:
                return self._insert_recursive(node.left, data)
        elif data > node.data:
            if node.right is None:
                node.right = TreeNode(data)
                return True
            else:
                return self._insert_recursive(node.right, data)
        else:
            return False  # Duplicate value
    
    def search(self, data):
        """Search for a value in the tree"""
        result = self._search_recursive(self.root, data)
        if result:
            self.history.append(f"Found {data} in tree")
            return True, f"Found {data} in tree"
        else:
            self.history.append(f"Value {data} not found")
            return False, f"Value {data} not found in tree"
    
    def _search_recursive(self, node, data):
        """Helper method for recursive search"""
        if node is None:
            return False
        
        if data == node.data:
            return True
        elif data < node.data:
            return self._search_recursive(node.left, data)
        else:
            return self._search_recursive(node.right, data)
    
    def delete(self, data):
        """Delete a node from the tree"""
        if self.root is None:
            return False, "Tree is empty"
        
        self.root, deleted = self._delete_recursive(self.root, data)
        if deleted:
            self.history.append(f"Deleted {data}")
            return True, f"Successfully deleted {data}"
        else:
            return False, f"Value {data} not found in tree"
    
    def _delete_recursive(self, node, data):
        """Helper method for recursive deletion"""
        if node is None:
            return node, False
        
        if data < node.data:
            node.left, deleted = self._delete_recursive(node.left, data)
            return node, deleted
        elif data > node.data:
            node.right, deleted = self._delete_recursive(node.right, data)
            return node, deleted
        else:
            # Node to be deleted found
            if node.left is None:
                return node.right, True
            elif node.right is None:
                return node.left, True
            else:
                # Node with two children
                min_node = self._find_min(node.right)
                node.data = min_node.data
                node.right, _ = self._delete_recursive(node.right, min_node.data)
                return node, True
    
    def _find_min(self, node):
        """Find the minimum value node in a subtree"""
        while node.left is not None:
            node = node.left
        return node
    
    def inorder_traversal(self):
        """Perform inorder traversal (Left, Root, Right)"""
        self.traversal_result = []
        self._inorder_recursive(self.root)
        result = self.traversal_result.copy()
        self.history.append(f"Inorder traversal: {result}")
        return result, f"Inorder traversal completed: {result}"
    
    def _inorder_recursive(self, node):
        """Helper method for inorder traversal"""
        if node is not None:
            self._inorder_recursive(node.left)
            self.traversal_result.append(node.data)
            self._inorder_recursive(node.right)
    
    def preorder_traversal(self):
        """Perform preorder traversal (Root, Left, Right)"""
        self.traversal_result = []
        self._preorder_recursive(self.root)
        result = self.traversal_result.copy()
        self.history.append(f"Preorder traversal: {result}")
        return result, f"Preorder traversal completed: {result}"
    
    def _preorder_recursive(self, node):
        """Helper method for preorder traversal"""
        if node is not None:
            self.traversal_result.append(node.data)
            self._preorder_recursive(node.left)
            self._preorder_recursive(node.right)
    
    def postorder_traversal(self):
        """Perform postorder traversal (Left, Right, Root)"""
        self.traversal_result = []
        self._postorder_recursive(self.root)
        result = self.traversal_result.copy()
        self.history.append(f"Postorder traversal: {result}")
        return result, f"Postorder traversal completed: {result}"
    
    def _postorder_recursive(self, node):
        """Helper method for postorder traversal"""
        if node is not None:
            self._postorder_recursive(node.left)
            self._postorder_recursive(node.right)
            self.traversal_result.append(node.data)
    
    def get_tree_structure(self):
        """Get tree structure for visualization"""
        if self.root is None:
            return {}
        
        return self._build_tree_dict(self.root)
    
    def _build_tree_dict(self, node):
        """Helper method to build tree dictionary for visualization"""
        if node is None:
            return None
        
        return {
            'data': node.data,
            'left': self._build_tree_dict(node.left),
            'right': self._build_tree_dict(node.right)
        }
    
    def clear(self):
        """Clear the entire tree"""
        self.root = None
        self.history.append("Tree cleared")
    
    def get_history(self):
        """Return the operation history"""
        return self.history.copy()
    
    def clear_history(self):
        """Clear the operation history"""
        self.history.clear()
    
    def is_empty(self):
        """Check if tree is empty"""
        return self.root is None

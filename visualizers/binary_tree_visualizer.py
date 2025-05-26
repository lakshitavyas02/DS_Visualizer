"""
Binary Tree Visualizer using Streamlit and Matplotlib
"""

import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from data_structures.binary_tree import BinaryTree
from utils.pseudocode import BINARY_TREE_PSEUDOCODE
import time
import math

class BinaryTreeVisualizer:
    def __init__(self):
        if 'binary_tree' not in st.session_state:
            st.session_state.binary_tree = BinaryTree()
        self.tree = st.session_state.binary_tree
    
    def render(self):
        st.title("🌳 Binary Tree Visualizer")
        st.markdown("**Binary Search Tree** - Each node has at most two children, left < parent < right")
        
        # Create two columns for controls and visualization
        col1, col2 = st.columns([1, 2])
        
        with col1:
            self._render_controls()
        
        with col2:
            self._render_visualization()
        
        # Display operation history and traversals
        self._render_history_and_traversals()
    
    def _render_controls(self):
        st.subheader("🎮 Controls")
        
        # Insert operation
        st.markdown("**Insert Operation**")
        insert_value = st.text_input("Value to insert:", key="insert_input")
        
        col_insert, col_clear = st.columns(2)
        with col_insert:
            if st.button("🌱 Insert"):
                if insert_value:
                    try:
                        value = int(insert_value)
                        success, message = self.tree.insert(value)
                        if success:
                            st.success(message)
                            time.sleep(0.5)
                            st.rerun()
                        else:
                            st.error(message)
                    except ValueError:
                        st.error("Please enter a valid integer")
                else:
                    st.warning("Please enter a value to insert")
        
        with col_clear:
            if st.button("🗑️ Clear Tree"):
                self.tree.clear()
                st.rerun()
        
        # Delete operation
        st.markdown("**Delete Operation**")
        delete_value = st.text_input("Value to delete:", key="delete_input")
        if st.button("🗑️ Delete", disabled=self.tree.is_empty()):
            if delete_value:
                try:
                    value = int(delete_value)
                    success, message = self.tree.delete(value)
                    if success:
                        st.success(message)
                        time.sleep(0.5)
                        st.rerun()
                    else:
                        st.error(message)
                except ValueError:
                    st.error("Please enter a valid integer")
            else:
                st.warning("Please enter a value to delete")
        
        # Search operation
        st.markdown("**Search Operation**")
        search_value = st.text_input("Value to search:", key="search_input")
        if st.button("🔍 Search"):
            if search_value:
                try:
                    value = int(search_value)
                    found, message = self.tree.search(value)
                    if found:
                        st.success(message)
                    else:
                        st.warning(message)
                except ValueError:
                    st.error("Please enter a valid integer")
            else:
                st.warning("Please enter a value to search")
        
        # Traversal operations
        st.markdown("**Traversal Operations**")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("📖 Inorder", disabled=self.tree.is_empty()):
                result, message = self.tree.inorder_traversal()
                st.info(f"Inorder: {result}")
        
        with col2:
            if st.button("📖 Preorder", disabled=self.tree.is_empty()):
                result, message = self.tree.preorder_traversal()
                st.info(f"Preorder: {result}")
        
        with col3:
            if st.button("📖 Postorder", disabled=self.tree.is_empty()):
                result, message = self.tree.postorder_traversal()
                st.info(f"Postorder: {result}")
        
        # Tree information
        st.markdown("**Tree Info**")
        st.write(f"Empty: {self.tree.is_empty()}")
        if not self.tree.is_empty():
            inorder_result, _ = self.tree.inorder_traversal()
            st.write(f"Nodes: {len(inorder_result)}")
    
    def _render_visualization(self):
        st.subheader("📊 Binary Tree Visualization")
        
        if self.tree.is_empty():
            st.info("Tree is empty. Add some nodes to see the visualization!")
            return
        
        # Get tree structure
        tree_structure = self.tree.get_tree_structure()
        
        # Create matplotlib figure
        fig, ax = plt.subplots(figsize=(12, 8))
        
        # Calculate tree dimensions
        inorder_result, _ = self.tree.inorder_traversal()
        tree_height = self._calculate_height(tree_structure)
        
        # Draw the tree
        self._draw_tree_recursive(ax, tree_structure, 6, 7, 3, 0)
        
        # Set axis properties
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 8)
        ax.set_aspect('equal')
        ax.axis('off')
        ax.set_title('Binary Search Tree Structure', fontsize=16, fontweight='bold')
        
        # Display the plot
        st.pyplot(fig)
        plt.close()
    
    def _calculate_height(self, node):
        """Calculate the height of the tree"""
        if node is None:
            return 0
        
        left_height = self._calculate_height(node.get('left'))
        right_height = self._calculate_height(node.get('right'))
        
        return 1 + max(left_height, right_height)
    
    def _draw_tree_recursive(self, ax, node, x, y, x_offset, level):
        """Recursively draw the tree nodes and edges"""
        if node is None:
            return
        
        # Draw the node
        circle = patches.Circle((x, y), 0.3, linewidth=2, edgecolor='black', facecolor='lightblue')
        ax.add_patch(circle)
        
        # Add the data text
        ax.text(x, y, str(node['data']), ha='center', va='center', 
                fontsize=12, fontweight='bold')
        
        # Calculate positions for children
        child_x_offset = x_offset / 1.5 if x_offset > 0.5 else 0.5
        child_y = y - 1.2
        
        # Draw left child
        if node.get('left'):
            left_x = x - child_x_offset
            # Draw edge
            ax.plot([x, left_x], [y - 0.3, child_y + 0.3], 'k-', linewidth=2)
            # Recursively draw left subtree
            self._draw_tree_recursive(ax, node['left'], left_x, child_y, child_x_offset, level + 1)
        
        # Draw right child
        if node.get('right'):
            right_x = x + child_x_offset
            # Draw edge
            ax.plot([x, right_x], [y - 0.3, child_y + 0.3], 'k-', linewidth=2)
            # Recursively draw right subtree
            self._draw_tree_recursive(ax, node['right'], right_x, child_y, child_x_offset, level + 1)
    
    def _render_history_and_traversals(self):
        st.subheader("📝 Operation History & Traversals")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Recent Operations**")
            history = self.tree.get_history()
            if history:
                for i, operation in enumerate(reversed(history[-8:])):  # Show last 8 operations
                    st.text(f"{len(history)-i}: {operation}")
            else:
                st.text("No operations performed yet")
            
            if st.button("Clear History"):
                self.tree.clear_history()
                st.rerun()
        
        with col2:
            st.markdown("**Current Traversals**")
            if not self.tree.is_empty():
                inorder, _ = self.tree.inorder_traversal()
                preorder, _ = self.tree.preorder_traversal()
                postorder, _ = self.tree.postorder_traversal()
                
                st.text(f"Inorder:   {inorder}")
                st.text(f"Preorder:  {preorder}")
                st.text(f"Postorder: {postorder}")
            else:
                st.text("Tree is empty")
    
    def render_with_pseudocode(self):
        """Render the visualizer with pseudocode sections"""
        self.render()
        
        # Pseudocode section
        st.markdown("---")
        st.subheader("📚 Algorithm Pseudocode")
        
        # Tabs for different operations
        tab1, tab2, tab3, tab4 = st.tabs(["Insert", "Inorder", "Preorder", "Postorder"])
        
        with tab1:
            st.code(BINARY_TREE_PSEUDOCODE["insert"], language="text")
        
        with tab2:
            st.code(BINARY_TREE_PSEUDOCODE["inorder"], language="text")
        
        with tab3:
            st.code(BINARY_TREE_PSEUDOCODE["preorder"], language="text")
        
        with tab4:
            st.code(BINARY_TREE_PSEUDOCODE["postorder"], language="text")

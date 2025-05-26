"""
Heap Visualizer using Streamlit and Matplotlib
"""

import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from data_structures.heap import Heap
import time
import math

class HeapVisualizer:
    def __init__(self):
        if 'heap' not in st.session_state:
            st.session_state.heap = Heap()
        self.heap = st.session_state.heap
    
    def render(self):
        st.title("🏔️ Heap Visualizer")
        st.markdown("**Complete Binary Tree** - Min Heap (smallest at root) or Max Heap (largest at root)")
        
        # Heap type selection
        heap_type = st.selectbox("Heap Type:", ["min", "max"])
        if heap_type != self.heap.heap_type:
            # Convert existing heap to new type
            old_array = self.heap.get_heap_array()
            self.heap = Heap(heap_type)
            st.session_state.heap = self.heap
            if old_array:
                self.heap.build_heap(old_array)
        
        # Create two columns for controls and visualization
        col1, col2 = st.columns([1, 2])
        
        with col1:
            self._render_controls()
        
        with col2:
            self._render_visualization()
        
        # Display operation history and array representation
        self._render_history_and_array()
    
    def _render_controls(self):
        st.subheader("🎮 Controls")
        
        # Insert operation
        st.markdown("**Insert Operation**")
        insert_value = st.text_input("Value to insert:", key="insert_input")
        
        col_insert, col_clear = st.columns(2)
        with col_insert:
            if st.button("⬆️ Insert"):
                if insert_value:
                    try:
                        value = int(insert_value)
                        success, message = self.heap.insert(value)
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
            if st.button("🗑️ Clear Heap"):
                self.heap.clear()
                st.rerun()
        
        # Extract operation
        st.markdown("**Extract Operation**")
        if st.button("⬇️ Extract Root", disabled=self.heap.is_empty()):
            root, message = self.heap.extract()
            if root is not None:
                st.success(message)
                time.sleep(0.5)
                st.rerun()
            else:
                st.error(message)
        
        # Peek operation
        st.markdown("**Peek Operation**")
        if st.button("👁️ Peek Root", disabled=self.heap.is_empty()):
            root, message = self.heap.peek()
            if root is not None:
                st.info(message)
            else:
                st.warning(message)
        
        # Delete specific value
        st.markdown("**Delete Specific Value**")
        delete_value = st.text_input("Value to delete:", key="delete_input")
        if st.button("🗑️ Delete Value", disabled=self.heap.is_empty()):
            if delete_value:
                try:
                    value = int(delete_value)
                    success, message = self.heap.delete(value)
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
        
        # Build heap from array
        st.markdown("**Build Heap from Array**")
        array_input = st.text_input("Enter numbers (comma-separated):", key="array_input")
        if st.button("🏗️ Build Heap"):
            if array_input:
                try:
                    array = [int(x.strip()) for x in array_input.split(',')]
                    success, message = self.heap.build_heap(array)
                    if success:
                        st.success(message)
                        time.sleep(0.5)
                        st.rerun()
                    else:
                        st.error(message)
                except ValueError:
                    st.error("Please enter valid integers separated by commas")
            else:
                st.warning("Please enter an array of numbers")
        
        # Heap sort
        st.markdown("**Heap Sort**")
        if st.button("🔄 Heap Sort", disabled=self.heap.is_empty()):
            sorted_array, message = self.heap.heap_sort()
            st.success(message)
        
        # Heap information
        st.markdown("**Heap Info**")
        st.write(f"Type: {self.heap.heap_type.title()} Heap")
        st.write(f"Size: {self.heap.size()}")
        st.write(f"Empty: {self.heap.is_empty()}")
    
    def _render_visualization(self):
        st.subheader("📊 Heap Visualization")
        
        if self.heap.is_empty():
            st.info("Heap is empty. Add some elements to see the visualization!")
            return
        
        # Get heap structure
        tree_structure = self.heap.get_tree_structure()
        heap_array = self.heap.get_heap_array()
        
        # Create matplotlib figure
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
        
        # Tree visualization
        self._draw_heap_tree(ax1, tree_structure, heap_array)
        
        # Array visualization
        self._draw_heap_array(ax2, heap_array)
        
        # Display the plot
        st.pyplot(fig)
        plt.close()
    
    def _draw_heap_tree(self, ax, tree_structure, heap_array):
        """Draw heap as a tree"""
        if not tree_structure:
            return
        
        # Calculate tree dimensions
        height = math.floor(math.log2(len(heap_array))) + 1
        width = 2 ** (height - 1)
        
        # Draw the tree
        self._draw_heap_node_recursive(ax, tree_structure, 6, 8, 3, 0, height)
        
        # Set axis properties for tree
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 9)
        ax.set_aspect('equal')
        ax.axis('off')
        ax.set_title(f'{self.heap.heap_type.title()} Heap - Tree View', fontsize=14, fontweight='bold')
    
    def _draw_heap_node_recursive(self, ax, node, x, y, x_offset, level, max_height):
        """Recursively draw heap nodes"""
        if node is None:
            return
        
        # Determine node color based on heap type and position
        if node['index'] == 0:
            node_color = '#FF6B6B'  # Root - red
        elif level == 1:
            node_color = '#4ECDC4'  # Level 1 - teal
        else:
            node_color = '#95E1D3'  # Other levels - light teal
        
        # Draw the node
        circle = patches.Circle((x, y), 0.4, linewidth=2, edgecolor='black', facecolor=node_color)
        ax.add_patch(circle)
        
        # Add the data text
        ax.text(x, y, str(node['data']), ha='center', va='center', 
                fontsize=12, fontweight='bold', color='white')
        
        # Add index label
        ax.text(x, y - 0.7, f'[{node["index"]}]', ha='center', va='center', 
                fontsize=8, color='gray')
        
        # Calculate positions for children
        child_x_offset = x_offset / 1.8 if x_offset > 0.8 else 0.8
        child_y = y - 1.5
        
        # Draw left child
        if node.get('left'):
            left_x = x - child_x_offset
            # Draw edge
            ax.plot([x, left_x], [y - 0.4, child_y + 0.4], 'k-', linewidth=2)
            # Recursively draw left subtree
            self._draw_heap_node_recursive(ax, node['left'], left_x, child_y, child_x_offset, level + 1, max_height)
        
        # Draw right child
        if node.get('right'):
            right_x = x + child_x_offset
            # Draw edge
            ax.plot([x, right_x], [y - 0.4, child_y + 0.4], 'k-', linewidth=2)
            # Recursively draw right subtree
            self._draw_heap_node_recursive(ax, node['right'], right_x, child_y, child_x_offset, level + 1, max_height)
    
    def _draw_heap_array(self, ax, heap_array):
        """Draw heap as an array"""
        if not heap_array:
            return
        
        # Array visualization parameters
        box_width = 0.8
        box_height = 0.6
        start_x = 1
        start_y = 1
        
        # Draw array boxes
        for i, value in enumerate(heap_array):
            x_pos = start_x + i * box_width
            
            # Determine box color based on level in tree
            level = math.floor(math.log2(i + 1))
            if i == 0:
                box_color = '#FF6B6B'  # Root
            elif level == 1:
                box_color = '#4ECDC4'  # Level 1
            else:
                box_color = '#95E1D3'  # Other levels
            
            # Draw rectangle
            rect = patches.Rectangle(
                (x_pos, start_y), box_width, box_height,
                linewidth=2, edgecolor='black', facecolor=box_color
            )
            ax.add_patch(rect)
            
            # Add value text
            ax.text(
                x_pos + box_width/2, start_y + box_height/2,
                str(value), ha='center', va='center',
                fontsize=12, fontweight='bold', color='white'
            )
            
            # Add index label
            ax.text(
                x_pos + box_width/2, start_y - 0.2,
                f'[{i}]', ha='center', va='center',
                fontsize=10, color='gray'
            )
            
            # Add parent-child relationship arrows for non-root elements
            if i > 0:
                parent_index = (i - 1) // 2
                parent_x = start_x + parent_index * box_width + box_width/2
                child_x = x_pos + box_width/2
                
                # Draw arrow from parent to child
                ax.annotate(
                    '', xy=(child_x, start_y + box_height + 0.1),
                    xytext=(parent_x, start_y + box_height + 0.3),
                    arrowprops=dict(arrowstyle='->', color='blue', lw=1, alpha=0.6)
                )
        
        # Set axis properties for array
        ax.set_xlim(0, start_x + len(heap_array) * box_width + 1)
        ax.set_ylim(0, 3)
        ax.set_aspect('equal')
        ax.axis('off')
        ax.set_title('Heap - Array Representation', fontsize=14, fontweight='bold')
        
        # Add heap property explanation
        heap_property = "Parent ≤ Children" if self.heap.heap_type == "min" else "Parent ≥ Children"
        ax.text(start_x, 2.5, f'Heap Property: {heap_property}', 
               fontsize=12, fontweight='bold', color='darkblue')
    
    def _render_history_and_array(self):
        st.subheader("📝 Operation History & Array View")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Recent Operations**")
            history = self.heap.get_history()
            if history:
                for i, operation in enumerate(reversed(history[-8:])):
                    st.text(f"{len(history)-i}: {operation}")
            else:
                st.text("No operations performed yet")
            
            if st.button("Clear History"):
                self.heap.clear_history()
                st.rerun()
        
        with col2:
            st.markdown("**Current Array**")
            heap_array = self.heap.get_heap_array()
            if heap_array:
                st.text(f"Array: {heap_array}")
                
                # Show parent-child relationships
                st.markdown("**Parent-Child Relationships:**")
                for i in range(len(heap_array)):
                    left_child = 2 * i + 1
                    right_child = 2 * i + 2
                    
                    children = []
                    if left_child < len(heap_array):
                        children.append(f"L:{heap_array[left_child]}")
                    if right_child < len(heap_array):
                        children.append(f"R:{heap_array[right_child]}")
                    
                    if children:
                        st.text(f"  [{i}]{heap_array[i]} → {', '.join(children)}")
            else:
                st.text("Heap is empty")
    
    def render_with_pseudocode(self):
        """Render the visualizer with pseudocode sections"""
        self.render()
        
        # Pseudocode section
        st.markdown("---")
        st.subheader("📚 Heap Algorithms")
        
        # Tabs for different operations
        tab1, tab2, tab3, tab4 = st.tabs(["Insert", "Extract", "Heapify Up", "Heapify Down"])
        
        with tab1:
            st.code("""
ALGORITHM Insert(heap, value)
BEGIN
    1. ADD value to end of heap array
    2. index = length(heap) - 1
    3. HeapifyUp(heap, index)
END

ALGORITHM HeapifyUp(heap, index)
BEGIN
    1. WHILE index > 0 DO
        parent_index = (index - 1) / 2
        IF heap[index] compared_to heap[parent_index] THEN
            SWAP heap[index] and heap[parent_index]
            index = parent_index
        ELSE
            BREAK
END
            """, language="text")
        
        with tab2:
            st.code("""
ALGORITHM Extract(heap)
BEGIN
    1. IF heap is empty THEN
        RETURN null
    2. root = heap[0]
    3. heap[0] = heap[last_index]
    4. REMOVE last element
    5. HeapifyDown(heap, 0)
    6. RETURN root
END
            """, language="text")
        
        with tab3:
            st.code("""
ALGORITHM HeapifyUp(heap, index)
BEGIN
    1. WHILE index > 0 DO
        parent_index = (index - 1) / 2
        IF heap[index] satisfies_heap_property_with heap[parent_index] THEN
            SWAP heap[index] and heap[parent_index]
            index = parent_index
        ELSE
            BREAK
END
            """, language="text")
        
        with tab4:
            st.code("""
ALGORITHM HeapifyDown(heap, index)
BEGIN
    1. WHILE TRUE DO
        target = index
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        
        IF left_child < heap_size AND heap[left_child] better_than heap[target] THEN
            target = left_child
        
        IF right_child < heap_size AND heap[right_child] better_than heap[target] THEN
            target = right_child
        
        IF target == index THEN
            BREAK
        
        SWAP heap[index] and heap[target]
        index = target
END
            """, language="text")

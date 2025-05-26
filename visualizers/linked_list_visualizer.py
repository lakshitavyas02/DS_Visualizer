"""
Linked List Visualizer using Streamlit and Matplotlib
"""

import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from data_structures.linked_list import LinkedList
from utils.pseudocode import LINKED_LIST_PSEUDOCODE
import time

class LinkedListVisualizer:
    def __init__(self):
        if 'linked_list' not in st.session_state:
            st.session_state.linked_list = LinkedList()
        if 'doubly_linked_list' not in st.session_state:
            st.session_state.doubly_linked_list = LinkedList(doubly=True)
        
        # Choose between singly and doubly linked list
        self.list_type = st.selectbox("List Type:", ["Singly Linked List", "Doubly Linked List"])
        
        if self.list_type == "Singly Linked List":
            self.linked_list = st.session_state.linked_list
        else:
            self.linked_list = st.session_state.doubly_linked_list
    
    def render(self):
        st.title("🔗 Linked List Visualizer")
        st.markdown(f"**{self.list_type}** - Dynamic data structure with nodes containing data and pointers")
        
        # Create two columns for controls and visualization
        col1, col2 = st.columns([1, 2])
        
        with col1:
            self._render_controls()
        
        with col2:
            self._render_visualization()
        
        # Display operation history
        self._render_history()
    
    def _render_controls(self):
        st.subheader("🎮 Controls")
        
        # Insert operations
        st.markdown("**Insert Operations**")
        insert_value = st.text_input("Value to insert:", key="insert_input")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("⬅️ Insert at Beginning"):
                if insert_value:
                    success, message = self.linked_list.insert_at_beginning(insert_value)
                    if success:
                        st.success(message)
                        time.sleep(0.5)
                        st.rerun()
                else:
                    st.warning("Please enter a value")
        
        with col2:
            if st.button("➡️ Insert at End"):
                if insert_value:
                    success, message = self.linked_list.insert_at_end(insert_value)
                    if success:
                        st.success(message)
                        time.sleep(0.5)
                        st.rerun()
                else:
                    st.warning("Please enter a value")
        
        with col3:
            position = st.number_input("Position:", min_value=0, max_value=self.linked_list.size, value=0)
            if st.button("📍 Insert at Position"):
                if insert_value:
                    success, message = self.linked_list.insert_at_position(insert_value, position)
                    if success:
                        st.success(message)
                        time.sleep(0.5)
                        st.rerun()
                    else:
                        st.error(message)
                else:
                    st.warning("Please enter a value")
        
        # Delete operation
        st.markdown("**Delete Operation**")
        delete_value = st.text_input("Value to delete:", key="delete_input")
        
        col_delete, col_clear = st.columns(2)
        with col_delete:
            if st.button("🗑️ Delete", disabled=self.linked_list.size == 0):
                if delete_value:
                    success, message = self.linked_list.delete(delete_value)
                    if success:
                        st.success(message)
                        time.sleep(0.5)
                        st.rerun()
                    else:
                        st.error(message)
                else:
                    st.warning("Please enter a value to delete")
        
        with col_clear:
            if st.button("🗑️ Clear All"):
                self.linked_list.clear()
                st.rerun()
        
        # Search operation
        st.markdown("**Search Operation**")
        search_value = st.text_input("Value to search:", key="search_input")
        if st.button("🔍 Search"):
            if search_value:
                position, message = self.linked_list.search(search_value)
                if position >= 0:
                    st.success(message)
                else:
                    st.warning(message)
            else:
                st.warning("Please enter a value to search")
        
        # List information
        st.markdown("**List Info**")
        st.write(f"Size: {self.linked_list.size}")
        st.write(f"Empty: {self.linked_list.size == 0}")
        st.write(f"Type: {self.list_type}")
    
    def _render_visualization(self):
        st.subheader("📊 Linked List Visualization")
        
        # Get list data
        items = self.linked_list.get_list()
        
        if not items:
            st.info("List is empty. Add some elements to see the visualization!")
            return
        
        # Create matplotlib figure
        fig, ax = plt.subplots(figsize=(max(12, len(items) * 2), 6))
        
        # Visualization parameters
        node_width = 1.5
        node_height = 0.8
        arrow_length = 0.5
        start_x = 1
        start_y = 3
        
        # Draw nodes and arrows
        for i, item in enumerate(items):
            x_pos = start_x + i * (node_width + arrow_length + 0.5)
            
            # Draw node rectangle
            node_color = '#4CAF50' if i == 0 else '#81C784'  # Head node in different color
            rect = patches.Rectangle(
                (x_pos, start_y), node_width, node_height,
                linewidth=2, edgecolor='black', facecolor=node_color
            )
            ax.add_patch(rect)
            
            # Add data text
            ax.text(
                x_pos + node_width/2, start_y + node_height/2,
                str(item), ha='center', va='center',
                fontsize=12, fontweight='bold', color='white'
            )
            
            # Add position label
            ax.text(
                x_pos + node_width/2, start_y - 0.3,
                f'pos {i}', ha='center', va='center',
                fontsize=10, color='gray'
            )
            
            # Draw arrow to next node (except for last node)
            if i < len(items) - 1:
                arrow_start_x = x_pos + node_width
                arrow_end_x = arrow_start_x + arrow_length + 0.5
                arrow_y = start_y + node_height/2
                
                # Forward arrow
                ax.annotate(
                    '', xy=(arrow_end_x, arrow_y),
                    xytext=(arrow_start_x, arrow_y),
                    arrowprops=dict(arrowstyle='->', color='blue', lw=2)
                )
                
                # For doubly linked list, add backward arrow
                if self.linked_list.doubly:
                    ax.annotate(
                        '', xy=(arrow_start_x, arrow_y - 0.2),
                        xytext=(arrow_end_x, arrow_y - 0.2),
                        arrowprops=dict(arrowstyle='->', color='red', lw=2)
                    )
            else:
                # Draw NULL pointer for last node
                null_x = x_pos + node_width
                ax.text(
                    null_x + 0.3, start_y + node_height/2,
                    'NULL', ha='center', va='center',
                    fontsize=10, color='red', fontweight='bold'
                )
        
        # Add HEAD indicator
        if items:
            head_x = start_x + node_width/2
            ax.annotate(
                'HEAD', xy=(head_x, start_y + node_height),
                xytext=(head_x, start_y + node_height + 0.8),
                arrowprops=dict(arrowstyle='->', color='green', lw=2),
                fontsize=12, fontweight='bold', color='green', ha='center'
            )
        
        # For doubly linked list, add TAIL indicator
        if items and self.linked_list.doubly:
            tail_x = start_x + (len(items) - 1) * (node_width + arrow_length + 0.5) + node_width/2
            ax.annotate(
                'TAIL', xy=(tail_x, start_y),
                xytext=(tail_x, start_y - 0.8),
                arrowprops=dict(arrowstyle='->', color='purple', lw=2),
                fontsize=12, fontweight='bold', color='purple', ha='center'
            )
        
        # Set axis properties
        total_width = len(items) * (node_width + arrow_length + 0.5) + 2
        ax.set_xlim(0, max(total_width, 8))
        ax.set_ylim(1, 6)
        ax.set_aspect('equal')
        ax.axis('off')
        ax.set_title(f'{self.list_type} Structure', fontsize=16, fontweight='bold')
        
        # Add legend for doubly linked list
        if self.linked_list.doubly and len(items) > 1:
            ax.text(
                0.5, 5.5, 'Blue arrows: next pointers\nRed arrows: prev pointers',
                fontsize=10, bbox=dict(boxstyle="round,pad=0.3", facecolor="lightgray")
            )
        
        # Display the plot
        st.pyplot(fig)
        plt.close()
    
    def _render_history(self):
        st.subheader("📝 Operation History")
        
        col1, col2 = st.columns(2)
        
        with col1:
            history = self.linked_list.get_history()
            if history:
                for i, operation in enumerate(reversed(history[-10:])):  # Show last 10 operations
                    st.text(f"{len(history)-i}: {operation}")
            else:
                st.text("No operations performed yet")
        
        with col2:
            if st.button("Clear History"):
                self.linked_list.clear_history()
                st.rerun()
    
    def render_with_pseudocode(self):
        """Render the visualizer with pseudocode sections"""
        self.render()
        
        # Pseudocode section
        st.markdown("---")
        st.subheader("📚 Algorithm Pseudocode")
        
        # Tabs for different operations
        tab1, tab2, tab3 = st.tabs(["Insert at Beginning", "Insert at End", "Delete"])
        
        with tab1:
            st.code(LINKED_LIST_PSEUDOCODE["insert_beginning"], language="text")
        
        with tab2:
            st.code(LINKED_LIST_PSEUDOCODE["insert_end"], language="text")
        
        with tab3:
            st.code(LINKED_LIST_PSEUDOCODE["delete"], language="text")

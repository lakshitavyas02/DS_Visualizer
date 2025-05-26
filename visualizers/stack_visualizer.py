"""
Stack Visualizer using Streamlit and Matplotlib
"""

import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from data_structures.stack import Stack
from utils.pseudocode import STACK_PSEUDOCODE
import time

class StackVisualizer:
    def __init__(self):
        if 'stack' not in st.session_state:
            st.session_state.stack = Stack()
        self.stack = st.session_state.stack
    
    def render(self):
        st.title("🥞 Stack Visualizer")
        st.markdown("**LIFO (Last In, First Out)** - Elements are added and removed from the top")
        
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
        
        # Stack size configuration
        max_size = st.slider("Max Stack Size", 3, 15, self.stack.max_size)
        if max_size != self.stack.max_size:
            self.stack.max_size = max_size
        
        # Push operation
        st.markdown("**Push Operation**")
        push_value = st.text_input("Value to push:", key="push_input")
        
        col_push, col_clear = st.columns(2)
        with col_push:
            if st.button("🔼 Push", disabled=self.stack.is_full()):
                if push_value:
                    success, message = self.stack.push(push_value)
                    if success:
                        st.success(message)
                        time.sleep(0.5)  # Simple animation delay
                        st.rerun()
                    else:
                        st.error(message)
                else:
                    st.warning("Please enter a value to push")
        
        with col_clear:
            if st.button("🗑️ Clear"):
                self.stack.clear()
                st.rerun()
        
        # Pop operation
        st.markdown("**Pop Operation**")
        if st.button("🔽 Pop", disabled=self.stack.is_empty()):
            item, message = self.stack.pop()
            if item is not None:
                st.success(message)
                time.sleep(0.5)  # Simple animation delay
                st.rerun()
            else:
                st.error(message)
        
        # Peek operation
        st.markdown("**Peek Operation**")
        if st.button("👁️ Peek", disabled=self.stack.is_empty()):
            item, message = self.stack.peek()
            if item is not None:
                st.info(message)
            else:
                st.warning(message)
        
        # Stack information
        st.markdown("**Stack Info**")
        st.write(f"Size: {self.stack.size()}/{self.stack.max_size}")
        st.write(f"Empty: {self.stack.is_empty()}")
        st.write(f"Full: {self.stack.is_full()}")
    
    def _render_visualization(self):
        st.subheader("📊 Stack Visualization")
        
        # Create matplotlib figure
        fig, ax = plt.subplots(figsize=(8, 10))
        
        # Stack visualization parameters
        box_width = 2
        box_height = 0.8
        start_x = 1
        start_y = 1
        
        # Draw stack boxes
        items = self.stack.get_items()
        
        # Draw empty boxes for maximum capacity
        for i in range(self.stack.max_size):
            y_pos = start_y + i * box_height
            
            # Determine box color and content
            if i < len(items):
                # Filled box
                box_color = '#4CAF50' if i == len(items) - 1 else '#81C784'
                text_color = 'white'
                content = str(items[i])
            else:
                # Empty box
                box_color = '#E0E0E0'
                text_color = 'gray'
                content = ''
            
            # Draw rectangle
            rect = patches.Rectangle(
                (start_x, y_pos), box_width, box_height,
                linewidth=2, edgecolor='black', facecolor=box_color
            )
            ax.add_patch(rect)
            
            # Add text
            ax.text(
                start_x + box_width/2, y_pos + box_height/2,
                content, ha='center', va='center',
                fontsize=12, fontweight='bold', color=text_color
            )
            
            # Add index label
            ax.text(
                start_x - 0.3, y_pos + box_height/2,
                f'[{i}]', ha='center', va='center',
                fontsize=10, color='gray'
            )
        
        # Add "TOP" indicator
        if not self.stack.is_empty():
            top_y = start_y + (len(items) - 1) * box_height + box_height/2
            ax.annotate(
                'TOP', xy=(start_x + box_width + 0.1, top_y),
                xytext=(start_x + box_width + 0.8, top_y),
                arrowprops=dict(arrowstyle='->', color='red', lw=2),
                fontsize=12, fontweight='bold', color='red'
            )
        
        # Set axis properties
        ax.set_xlim(0, 4)
        ax.set_ylim(0, start_y + self.stack.max_size * box_height + 1)
        ax.set_aspect('equal')
        ax.axis('off')
        ax.set_title('Stack Structure', fontsize=16, fontweight='bold')
        
        # Display the plot
        st.pyplot(fig)
        plt.close()
    
    def _render_history(self):
        st.subheader("📝 Operation History")
        
        col1, col2 = st.columns(2)
        
        with col1:
            history = self.stack.get_history()
            if history:
                for i, operation in enumerate(reversed(history[-10:])):  # Show last 10 operations
                    st.text(f"{len(history)-i}: {operation}")
            else:
                st.text("No operations performed yet")
        
        with col2:
            if st.button("Clear History"):
                self.stack.clear_history()
                st.rerun()
    
    def _render_pseudocode(self, operation):
        """Render pseudocode for the given operation"""
        if operation in STACK_PSEUDOCODE:
            st.subheader(f"📋 Pseudocode - {operation.title()}")
            st.code(STACK_PSEUDOCODE[operation], language="text")
    
    def render_with_pseudocode(self):
        """Render the visualizer with pseudocode sections"""
        self.render()
        
        # Pseudocode section
        st.markdown("---")
        st.subheader("📚 Algorithm Pseudocode")
        
        # Tabs for different operations
        tab1, tab2, tab3 = st.tabs(["Push", "Pop", "Peek"])
        
        with tab1:
            st.code(STACK_PSEUDOCODE["push"], language="text")
        
        with tab2:
            st.code(STACK_PSEUDOCODE["pop"], language="text")
        
        with tab3:
            st.code(STACK_PSEUDOCODE["peek"], language="text")

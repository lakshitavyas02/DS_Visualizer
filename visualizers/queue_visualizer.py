"""
Queue Visualizer using Streamlit and Matplotlib
"""

import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from data_structures.queue import Queue
from utils.pseudocode import QUEUE_PSEUDOCODE
import time

class QueueVisualizer:
    def __init__(self):
        if 'queue' not in st.session_state:
            st.session_state.queue = Queue()
        self.queue = st.session_state.queue
    
    def render(self):
        st.title("🚶‍♂️ Queue Visualizer")
        st.markdown("**FIFO (First In, First Out)** - Elements are added at rear and removed from front")
        
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
        
        # Queue size configuration
        max_size = st.slider("Max Queue Size", 3, 15, self.queue.max_size)
        if max_size != self.queue.max_size:
            self.queue.max_size = max_size
        
        # Enqueue operation
        st.markdown("**Enqueue Operation**")
        enqueue_value = st.text_input("Value to enqueue:", key="enqueue_input")
        
        col_enqueue, col_clear = st.columns(2)
        with col_enqueue:
            if st.button("➡️ Enqueue", disabled=self.queue.is_full()):
                if enqueue_value:
                    success, message = self.queue.enqueue(enqueue_value)
                    if success:
                        st.success(message)
                        time.sleep(0.5)  # Simple animation delay
                        st.rerun()
                    else:
                        st.error(message)
                else:
                    st.warning("Please enter a value to enqueue")
        
        with col_clear:
            if st.button("🗑️ Clear"):
                self.queue.clear()
                st.rerun()
        
        # Dequeue operation
        st.markdown("**Dequeue Operation**")
        if st.button("⬅️ Dequeue", disabled=self.queue.is_empty()):
            item, message = self.queue.dequeue()
            if item is not None:
                st.success(message)
                time.sleep(0.5)  # Simple animation delay
                st.rerun()
            else:
                st.error(message)
        
        # Front and Rear operations
        col_front, col_rear = st.columns(2)
        with col_front:
            st.markdown("**Front**")
            if st.button("👁️ Front", disabled=self.queue.is_empty()):
                item, message = self.queue.front()
                if item is not None:
                    st.info(message)
                else:
                    st.warning(message)
        
        with col_rear:
            st.markdown("**Rear**")
            if st.button("👁️ Rear", disabled=self.queue.is_empty()):
                item, message = self.queue.rear()
                if item is not None:
                    st.info(message)
                else:
                    st.warning(message)
        
        # Queue information
        st.markdown("**Queue Info**")
        st.write(f"Size: {self.queue.size()}/{self.queue.max_size}")
        st.write(f"Empty: {self.queue.is_empty()}")
        st.write(f"Full: {self.queue.is_full()}")
    
    def _render_visualization(self):
        st.subheader("📊 Queue Visualization")
        
        # Create matplotlib figure
        fig, ax = plt.subplots(figsize=(12, 6))
        
        # Queue visualization parameters
        box_width = 1.5
        box_height = 1
        start_x = 1
        start_y = 2
        
        # Draw queue boxes
        items = self.queue.get_items()
        
        # Draw boxes for maximum capacity
        for i in range(self.queue.max_size):
            x_pos = start_x + i * box_width
            
            # Determine box color and content
            if i < len(items):
                # Filled box
                if i == 0:
                    box_color = '#FF5722'  # Front - Red/Orange
                elif i == len(items) - 1:
                    box_color = '#4CAF50'  # Rear - Green
                else:
                    box_color = '#81C784'  # Middle - Light Green
                text_color = 'white'
                content = str(items[i])
            else:
                # Empty box
                box_color = '#E0E0E0'
                text_color = 'gray'
                content = ''
            
            # Draw rectangle
            rect = patches.Rectangle(
                (x_pos, start_y), box_width, box_height,
                linewidth=2, edgecolor='black', facecolor=box_color
            )
            ax.add_patch(rect)
            
            # Add text
            ax.text(
                x_pos + box_width/2, start_y + box_height/2,
                content, ha='center', va='center',
                fontsize=12, fontweight='bold', color=text_color
            )
            
            # Add index label
            ax.text(
                x_pos + box_width/2, start_y - 0.3,
                f'[{i}]', ha='center', va='center',
                fontsize=10, color='gray'
            )
        
        # Add "FRONT" and "REAR" indicators
        if not self.queue.is_empty():
            # Front indicator
            front_x = start_x + box_width/2
            ax.annotate(
                'FRONT', xy=(front_x, start_y),
                xytext=(front_x, start_y - 0.8),
                arrowprops=dict(arrowstyle='->', color='red', lw=2),
                fontsize=12, fontweight='bold', color='red', ha='center'
            )
            
            # Rear indicator
            rear_x = start_x + (len(items) - 1) * box_width + box_width/2
            ax.annotate(
                'REAR', xy=(rear_x, start_y + box_height),
                xytext=(rear_x, start_y + box_height + 0.8),
                arrowprops=dict(arrowstyle='->', color='green', lw=2),
                fontsize=12, fontweight='bold', color='green', ha='center'
            )
        
        # Add direction arrows
        if len(items) > 1:
            # Enqueue direction (right arrow)
            ax.annotate(
                '', xy=(start_x + self.queue.max_size * box_width + 0.5, start_y + box_height/2),
                xytext=(start_x + self.queue.max_size * box_width + 0.2, start_y + box_height/2),
                arrowprops=dict(arrowstyle='->', color='blue', lw=3)
            )
            ax.text(
                start_x + self.queue.max_size * box_width + 0.7, start_y + box_height/2,
                'Enqueue', rotation=90, ha='center', va='center',
                fontsize=10, color='blue', fontweight='bold'
            )
            
            # Dequeue direction (left arrow)
            ax.annotate(
                '', xy=(start_x - 0.5, start_y + box_height/2),
                xytext=(start_x - 0.2, start_y + box_height/2),
                arrowprops=dict(arrowstyle='->', color='orange', lw=3)
            )
            ax.text(
                start_x - 0.7, start_y + box_height/2,
                'Dequeue', rotation=90, ha='center', va='center',
                fontsize=10, color='orange', fontweight='bold'
            )
        
        # Set axis properties
        ax.set_xlim(0, start_x + self.queue.max_size * box_width + 1)
        ax.set_ylim(0, 5)
        ax.set_aspect('equal')
        ax.axis('off')
        ax.set_title('Queue Structure', fontsize=16, fontweight='bold')
        
        # Display the plot
        st.pyplot(fig)
        plt.close()
    
    def _render_history(self):
        st.subheader("📝 Operation History")
        
        col1, col2 = st.columns(2)
        
        with col1:
            history = self.queue.get_history()
            if history:
                for i, operation in enumerate(reversed(history[-10:])):  # Show last 10 operations
                    st.text(f"{len(history)-i}: {operation}")
            else:
                st.text("No operations performed yet")
        
        with col2:
            if st.button("Clear History"):
                self.queue.clear_history()
                st.rerun()
    
    def render_with_pseudocode(self):
        """Render the visualizer with pseudocode sections"""
        self.render()
        
        # Pseudocode section
        st.markdown("---")
        st.subheader("📚 Algorithm Pseudocode")
        
        # Tabs for different operations
        tab1, tab2 = st.tabs(["Enqueue", "Dequeue"])
        
        with tab1:
            st.code(QUEUE_PSEUDOCODE["enqueue"], language="text")
        
        with tab2:
            st.code(QUEUE_PSEUDOCODE["dequeue"], language="text")

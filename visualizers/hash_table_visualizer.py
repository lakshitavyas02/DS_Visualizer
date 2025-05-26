"""
Hash Table Visualizer using Streamlit and Matplotlib
"""

import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from data_structures.hash_table import HashTable
import time

class HashTableVisualizer:
    def __init__(self):
        if 'hash_table' not in st.session_state:
            st.session_state.hash_table = HashTable()
        self.hash_table = st.session_state.hash_table
    
    def render(self):
        st.title("🗂️ Hash Table Visualizer")
        st.markdown("**Key-Value Storage** - Fast insertion, deletion, and lookup using hash functions")
        
        # Create two columns for controls and visualization
        col1, col2 = st.columns([1, 2])
        
        with col1:
            self._render_controls()
        
        with col2:
            self._render_visualization()
        
        # Display operation history and statistics
        self._render_history_and_stats()
    
    def _render_controls(self):
        st.subheader("🎮 Controls")
        
        # Hash table size configuration
        new_size = st.slider("Hash Table Size", 5, 20, self.hash_table.size)
        if new_size != self.hash_table.size:
            # Create new hash table with new size
            old_items = self.hash_table.get_all_items()
            self.hash_table = HashTable(new_size)
            st.session_state.hash_table = self.hash_table
            # Re-insert all items
            for key, value in old_items:
                self.hash_table.insert(key, value)
        
        # Insert operation
        st.markdown("**Insert/Update Operation**")
        col_key, col_value = st.columns(2)
        with col_key:
            key_input = st.text_input("Key:", key="key_input")
        with col_value:
            value_input = st.text_input("Value:", key="value_input")
        
        col_insert, col_clear = st.columns(2)
        with col_insert:
            if st.button("📝 Insert/Update"):
                if key_input and value_input:
                    success, message = self.hash_table.insert(key_input, value_input)
                    if success:
                        st.success(message)
                        time.sleep(0.5)
                        st.rerun()
                    else:
                        st.error(message)
                else:
                    st.warning("Please enter both key and value")
        
        with col_clear:
            if st.button("🗑️ Clear All"):
                self.hash_table.clear()
                st.rerun()
        
        # Get operation
        st.markdown("**Get Operation**")
        get_key = st.text_input("Key to get:", key="get_input")
        if st.button("🔍 Get Value"):
            if get_key:
                value, message = self.hash_table.get(get_key)
                if value is not None:
                    st.success(message)
                else:
                    st.warning(message)
            else:
                st.warning("Please enter a key to search")
        
        # Delete operation
        st.markdown("**Delete Operation**")
        delete_key = st.text_input("Key to delete:", key="delete_input")
        if st.button("🗑️ Delete", disabled=self.hash_table.is_empty()):
            if delete_key:
                success, message = self.hash_table.delete(delete_key)
                if success:
                    st.success(message)
                    time.sleep(0.5)
                    st.rerun()
                else:
                    st.error(message)
            else:
                st.warning("Please enter a key to delete")
        
        # Contains operation
        st.markdown("**Contains Operation**")
        contains_key = st.text_input("Key to check:", key="contains_input")
        if st.button("❓ Contains"):
            if contains_key:
                exists, message = self.hash_table.contains(contains_key)
                if exists:
                    st.success(message)
                else:
                    st.info(message)
            else:
                st.warning("Please enter a key to check")
    
    def _render_visualization(self):
        st.subheader("📊 Hash Table Visualization")
        
        # Create matplotlib figure
        fig, ax = plt.subplots(figsize=(12, 8))
        
        # Visualization parameters
        bucket_width = 8
        bucket_height = 0.8
        start_x = 1
        start_y = 1
        
        table_state = self.hash_table.get_table_state()
        
        # Draw hash table buckets
        for i, bucket in enumerate(table_state):
            y_pos = start_y + i * (bucket_height + 0.2)
            
            # Draw index label
            ax.text(start_x - 0.5, y_pos + bucket_height/2, f'[{i}]', 
                   ha='center', va='center', fontsize=12, fontweight='bold')
            
            # Draw bucket container
            bucket_rect = patches.Rectangle(
                (start_x, y_pos), bucket_width, bucket_height,
                linewidth=2, edgecolor='black', facecolor='lightgray', alpha=0.3
            )
            ax.add_patch(bucket_rect)
            
            # Draw items in bucket
            if bucket:
                item_width = bucket_width / len(bucket)
                for j, (key, value) in enumerate(bucket):
                    item_x = start_x + j * item_width
                    
                    # Color based on collision
                    item_color = '#FF6B6B' if len(bucket) > 1 else '#4ECDC4'
                    
                    # Draw item rectangle
                    item_rect = patches.Rectangle(
                        (item_x, y_pos), item_width, bucket_height,
                        linewidth=1, edgecolor='black', facecolor=item_color
                    )
                    ax.add_patch(item_rect)
                    
                    # Add key:value text
                    ax.text(item_x + item_width/2, y_pos + bucket_height/2,
                           f'{key}:{value}', ha='center', va='center',
                           fontsize=8, fontweight='bold', color='white')
            else:
                # Empty bucket
                ax.text(start_x + bucket_width/2, y_pos + bucket_height/2,
                       'Empty', ha='center', va='center',
                       fontsize=10, color='gray', style='italic')
        
        # Add hash function visualization
        if hasattr(self, '_last_operation_key'):
            key = self._last_operation_key
            hash_value = self.hash_table._hash(key)
            
            # Draw arrow pointing to the hashed bucket
            arrow_y = start_y + hash_value * (bucket_height + 0.2) + bucket_height/2
            ax.annotate(
                f'hash("{key}") = {hash_value}',
                xy=(start_x + bucket_width + 0.1, arrow_y),
                xytext=(start_x + bucket_width + 2, arrow_y),
                arrowprops=dict(arrowstyle='->', color='red', lw=2),
                fontsize=10, fontweight='bold', color='red'
            )
        
        # Set axis properties
        ax.set_xlim(0, start_x + bucket_width + 4)
        ax.set_ylim(0, start_y + len(table_state) * (bucket_height + 0.2) + 1)
        ax.set_aspect('equal')
        ax.axis('off')
        ax.set_title('Hash Table Structure', fontsize=16, fontweight='bold')
        
        # Add legend
        legend_y = start_y + len(table_state) * (bucket_height + 0.2) + 0.5
        
        # Single item legend
        single_rect = patches.Rectangle((start_x, legend_y), 0.5, 0.3, 
                                       facecolor='#4ECDC4', edgecolor='black')
        ax.add_patch(single_rect)
        ax.text(start_x + 0.7, legend_y + 0.15, 'Single Item', 
               va='center', fontsize=10)
        
        # Collision legend
        collision_rect = patches.Rectangle((start_x + 3, legend_y), 0.5, 0.3, 
                                          facecolor='#FF6B6B', edgecolor='black')
        ax.add_patch(collision_rect)
        ax.text(start_x + 3.7, legend_y + 0.15, 'Collision (Chaining)', 
               va='center', fontsize=10)
        
        # Display the plot
        st.pyplot(fig)
        plt.close()
    
    def _render_history_and_stats(self):
        st.subheader("📝 Operation History & Statistics")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Recent Operations**")
            history = self.hash_table.get_history()
            if history:
                for i, operation in enumerate(reversed(history[-8:])):
                    st.text(f"{len(history)-i}: {operation}")
            else:
                st.text("No operations performed yet")
            
            if st.button("Clear History"):
                self.hash_table.clear_history()
                st.rerun()
        
        with col2:
            st.markdown("**Statistics**")
            st.write(f"**Size:** {self.hash_table.size}")
            st.write(f"**Items:** {self.hash_table.count}")
            st.write(f"**Load Factor:** {self.hash_table.get_load_factor():.2f}")
            st.write(f"**Collisions:** {self.hash_table.get_collision_count()}")
            st.write(f"**Empty:** {self.hash_table.is_empty()}")
            
            # Show all items
            st.markdown("**All Items:**")
            all_items = self.hash_table.get_all_items()
            if all_items:
                for key, value in all_items:
                    st.text(f"  {key}: {value}")
            else:
                st.text("  No items")
    
    def render_with_pseudocode(self):
        """Render the visualizer with pseudocode sections"""
        self.render()
        
        # Pseudocode section
        st.markdown("---")
        st.subheader("📚 Hash Table Algorithms")
        
        # Tabs for different operations
        tab1, tab2, tab3, tab4 = st.tabs(["Hash Function", "Insert", "Search", "Delete"])
        
        with tab1:
            st.code("""
ALGORITHM Hash(key, table_size)
BEGIN
    1. IF key is string THEN
        hash_value = 0
        FOR each character in key DO
            hash_value = hash_value + ASCII(character)
        RETURN hash_value MOD table_size
    2. ELSE
        RETURN hash(key) MOD table_size
END
            """, language="text")
        
        with tab2:
            st.code("""
ALGORITHM Insert(hash_table, key, value)
BEGIN
    1. index = Hash(key, table_size)
    2. bucket = hash_table[index]
    3. FOR each (k, v) in bucket DO
        IF k == key THEN
            UPDATE (k, v) to (key, value)
            RETURN "Updated"
    4. APPEND (key, value) to bucket
    5. RETURN "Inserted"
END
            """, language="text")
        
        with tab3:
            st.code("""
ALGORITHM Search(hash_table, key)
BEGIN
    1. index = Hash(key, table_size)
    2. bucket = hash_table[index]
    3. FOR each (k, v) in bucket DO
        IF k == key THEN
            RETURN v
    4. RETURN "Not Found"
END
            """, language="text")
        
        with tab4:
            st.code("""
ALGORITHM Delete(hash_table, key)
BEGIN
    1. index = Hash(key, table_size)
    2. bucket = hash_table[index]
    3. FOR i = 0 to length(bucket) - 1 DO
        IF bucket[i].key == key THEN
            REMOVE bucket[i]
            RETURN "Deleted"
    4. RETURN "Not Found"
END
            """, language="text")

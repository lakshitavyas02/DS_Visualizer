"""
Interactive Data Structure Visualizer
Built with Streamlit for educational purposes
"""

import streamlit as st
from visualizers.stack_visualizer import StackVisualizer
from visualizers.queue_visualizer import QueueVisualizer
from visualizers.linked_list_visualizer import LinkedListVisualizer
from visualizers.binary_tree_visualizer import BinaryTreeVisualizer
from visualizers.hash_table_visualizer import HashTableVisualizer
from visualizers.heap_visualizer import HeapVisualizer
from visualizers.graph_visualizer import GraphVisualizer

# Page configuration
st.set_page_config(
    page_title="Data Structure Visualizer",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .sidebar .sidebar-content {
        background-color: #f0f2f6;
    }
    .stButton > button {
        width: 100%;
        border-radius: 10px;
        border: 2px solid #1f77b4;
        background-color: #1f77b4;
        color: white;
        font-weight: bold;
    }
    .stButton > button:hover {
        background-color: #0d5aa7;
        border-color: #0d5aa7;
    }
    .info-box {
        background-color: #1f77b4;
        color: #ffffff;
        padding: 1.5rem;
        border-radius: 15px;
        border: 2px solid #3498db;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin: 1rem 0;
    }
    .info-box h3 {
        color: #ffffff;
        margin-top: 0;
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Sidebar navigation
    st.sidebar.title("🧠 Data Structure Visualizer")
    st.sidebar.markdown("---")

    # Navigation menu
    page = st.sidebar.selectbox(
        "Choose a Data Structure:",
        ["Home", "Stack", "Queue", "Linked List", "Binary Tree", "Hash Table", "Heap", "Graph"]
    )

    # Display selected page
    if page == "Home":
        show_home_page()
    elif page == "Stack":
        stack_visualizer = StackVisualizer()
        stack_visualizer.render_with_pseudocode()
    elif page == "Queue":
        queue_visualizer = QueueVisualizer()
        queue_visualizer.render_with_pseudocode()
    elif page == "Linked List":
        linked_list_visualizer = LinkedListVisualizer()
        linked_list_visualizer.render_with_pseudocode()
    elif page == "Binary Tree":
        binary_tree_visualizer = BinaryTreeVisualizer()
        binary_tree_visualizer.render_with_pseudocode()
    elif page == "Hash Table":
        hash_table_visualizer = HashTableVisualizer()
        hash_table_visualizer.render_with_pseudocode()
    elif page == "Heap":
        heap_visualizer = HeapVisualizer()
        heap_visualizer.render_with_pseudocode()
    elif page == "Graph":
        graph_visualizer = GraphVisualizer()
        graph_visualizer.render_with_pseudocode()

    # Sidebar information
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 📚 About")
    st.sidebar.info(
        "This interactive visualizer helps you understand fundamental data structures "
        "through real-time visual feedback and step-by-step execution."
    )

    st.sidebar.markdown("### 🎯 Features")
    st.sidebar.markdown("""
    - **Interactive Controls**: Perform operations with buttons and inputs
    - **Real-time Visualization**: See changes instantly
    - **Step-by-step Execution**: Understand each operation
    - **Pseudocode Display**: Learn the algorithms
    - **Operation History**: Track your actions
    """)

    st.sidebar.markdown("### 🛠️ Tech Stack")
    st.sidebar.markdown("""
    - **Python 3**
    - **Streamlit** (UI Framework)
    - **Matplotlib** (Visualization)
    - **Custom Data Structures**
    """)

def show_home_page():
    """Display the home page with overview and instructions"""

    # Main title
    st.markdown('<h1 class="main-header">🧠 Interactive Data Structure Visualizer</h1>',
                unsafe_allow_html=True)

    # Introduction
    st.markdown("""
    <div class="info-box">
        <h3>Welcome to the Interactive Data Structure Visualizer!</h3>
        <p>This educational tool helps you understand and experiment with core data structures
        through real-time visual feedback. Perfect for students, educators, and anyone preparing
        for technical interviews.</p>
    </div>
    """, unsafe_allow_html=True)

    # Features overview
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📚 Supported Data Structures")

        st.markdown("**🥞 Stack (LIFO)**")
        st.write("- Push and Pop operations")
        st.write("- Peek functionality")
        st.write("- Visual stack representation")

        st.markdown("**🚶‍♂️ Queue (FIFO)**")
        st.write("- Enqueue and Dequeue operations")
        st.write("- Front and Rear access")
        st.write("- Circular queue visualization")

        st.markdown("**🔗 Linked List**")
        st.write("- Singly and Doubly linked lists")
        st.write("- Insert, Delete, Search operations")
        st.write("- Dynamic node visualization")

        st.markdown("**🌳 Binary Tree**")
        st.write("- Binary Search Tree operations")
        st.write("- Insert, Delete, Search")
        st.write("- Inorder, Preorder, Postorder traversals")

        st.markdown("**🗂️ Hash Table**")
        st.write("- Key-Value storage with hashing")
        st.write("- Insert, Get, Delete operations")
        st.write("- Collision handling with chaining")

        st.markdown("**🏔️ Heap**")
        st.write("- Min Heap and Max Heap")
        st.write("- Insert, Extract, Heapify operations")
        st.write("- Priority queue implementation")

        st.markdown("**🕸️ Graph**")
        st.write("- Directed and Undirected graphs")
        st.write("- Add vertices and edges")
        st.write("- BFS, DFS traversals and path finding")

    with col2:
        st.subheader("🎮 How to Use")

        st.markdown("**1. Choose a Data Structure**")
        st.write("Use the sidebar to select the data structure you want to explore.")

        st.markdown("**2. Perform Operations**")
        st.write("Use the interactive controls to add, remove, or search for elements.")

        st.markdown("**3. Watch the Visualization**")
        st.write("See real-time updates as you perform operations on the data structure.")

        st.markdown("**4. Learn the Algorithms**")
        st.write("Study the pseudocode to understand how each operation works.")

        st.markdown("**5. Track Your Progress**")
        st.write("View operation history to see what you've done.")

    # Quick start section
    st.markdown("---")
    st.subheader("🚀 Quick Start")

    # First row of buttons
    quick_col1, quick_col2, quick_col3, quick_col4 = st.columns(4)

    with quick_col1:
        if st.button("🥞 Explore Stack"):
            st.session_state.page = "Stack"
            st.rerun()

    with quick_col2:
        if st.button("🚶‍♂️ Explore Queue"):
            st.session_state.page = "Queue"
            st.rerun()

    with quick_col3:
        if st.button("🔗 Explore Linked List"):
            st.session_state.page = "Linked List"
            st.rerun()

    with quick_col4:
        if st.button("🌳 Explore Binary Tree"):
            st.session_state.page = "Binary Tree"
            st.rerun()

    # Second row of buttons
    quick_col5, quick_col6, quick_col7, quick_col8 = st.columns(4)

    with quick_col5:
        if st.button("🗂️ Explore Hash Table"):
            st.session_state.page = "Hash Table"
            st.rerun()

    with quick_col6:
        if st.button("🏔️ Explore Heap"):
            st.session_state.page = "Heap"
            st.rerun()

    with quick_col7:
        if st.button("🕸️ Explore Graph"):
            st.session_state.page = "Graph"
            st.rerun()

    with quick_col8:
        st.write("")  # Empty column for spacing

    # Educational benefits
    st.markdown("---")
    st.subheader("🎓 Educational Benefits")

    benefit_col1, benefit_col2, benefit_col3 = st.columns(3)

    with benefit_col1:
        st.markdown("""
        **🧠 Visual Learning**
        - See how data structures work in real-time
        - Understand memory layout and pointers
        - Grasp abstract concepts through visualization
        """)

    with benefit_col2:
        st.markdown("""
        **💡 Interactive Experience**
        - Hands-on learning approach
        - Immediate feedback on operations
        - Experiment with different scenarios
        """)

    with benefit_col3:
        st.markdown("""
        **📖 Algorithm Understanding**
        - Study pseudocode for each operation
        - Learn time and space complexity
        - Prepare for technical interviews
        """)

    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666; padding: 2rem;">
        <p>Built with ❤️ using Streamlit | Perfect for Computer Science Education</p>
        <p>Start exploring by selecting a data structure from the sidebar!</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()

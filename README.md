# 🧠 Interactive Data Structure Visualizer

An educational tool built entirely in Python using Streamlit that enables users to understand and experiment with core data structures through real-time visual feedback.

## 🌟 Features

### 📚 Supported Data Structures

- **🥞 Stack (LIFO)** - Last In, First Out operations
- **🚶‍♂️ Queue (FIFO)** - First In, First Out operations
- **🔗 Linked List** - Singly and Doubly linked lists
- **🌳 Binary Tree** - Binary Search Tree with traversals
- **🗂️ Hash Table** - Key-Value storage with collision handling
- **🏔️ Heap** - Min/Max Heap with priority queue operations
- **🕸️ Graph** - Directed/Undirected graphs with traversals

### 🎮 Interactive Controls

- Perform operations like push, pop, enqueue, dequeue, insert, delete, traverse
- Input values dynamically and see changes instantly
- Real-time visual updates with every operation

### 🔁 Step-by-Step Execution

- Simple animations using Python's time.sleep()
- Visual updates rendered on every operation
- Clear understanding of data structure behavior

### 🧠 Educational Aid

- Displays matching pseudocode alongside each operation
- Helps learners grasp both logic and implementation flow
- Operation history tracking for learning progress

### 🖥️ No Frontend Code Needed

- Entirely built in Python with Streamlit widgets
- Buttons, sliders, and expandable code sections
- Clean, intuitive user interface

## 🛠️ Tech Stack

- **Python 3.8+**
- **Streamlit** - Web app framework
- **Matplotlib** - Visualization and plotting
- **Custom Python Classes** - Data structure implementations

## 🚀 Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation Steps

1. **Clone or download the project**

   ```bash
   git clone <repository-url>
   cd VISUALIZER
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**

   ```bash
   streamlit run main.py
   ```

4. **Open in browser**
   - The app will automatically open in your default browser
   - If not, navigate to `http://localhost:8501`

## 📖 Usage Guide

### Getting Started

1. **Launch the application** using `streamlit run main.py`
2. **Choose a data structure** from the sidebar navigation
3. **Perform operations** using the interactive controls
4. **Watch the visualization** update in real-time
5. **Study the pseudocode** to understand algorithms
6. **Track your progress** through operation history

### Data Structure Operations

#### 🥞 Stack Operations

- **Push**: Add element to top of stack
- **Pop**: Remove element from top of stack
- **Peek**: View top element without removing
- **Clear**: Empty the entire stack

#### 🚶‍♂️ Queue Operations

- **Enqueue**: Add element to rear of queue
- **Dequeue**: Remove element from front of queue
- **Front**: View front element without removing
- **Rear**: View rear element without removing
- **Clear**: Empty the entire queue

#### 🔗 Linked List Operations

- **Insert at Beginning**: Add node at the start
- **Insert at End**: Add node at the end
- **Insert at Position**: Add node at specific position
- **Delete**: Remove node with specific value
- **Search**: Find position of a value
- **Clear**: Remove all nodes

#### 🌳 Binary Tree Operations

- **Insert**: Add node maintaining BST property
- **Delete**: Remove node from tree
- **Search**: Find if value exists in tree
- **Traversals**: Inorder, Preorder, Postorder
- **Clear**: Remove all nodes

#### 🗂️ Hash Table Operations

- **Insert/Update**: Add or update key-value pairs
- **Get**: Retrieve value by key
- **Delete**: Remove key-value pair
- **Contains**: Check if key exists
- **Clear**: Remove all entries

#### 🏔️ Heap Operations

- **Insert**: Add element maintaining heap property
- **Extract**: Remove root element (min/max)
- **Peek**: View root without removing
- **Delete**: Remove specific value
- **Build Heap**: Create heap from array
- **Heap Sort**: Sort elements using heap

#### 🕸️ Graph Operations

- **Add Vertex**: Add new node to graph
- **Add Edge**: Connect two vertices
- **Remove Vertex/Edge**: Delete nodes or connections
- **BFS/DFS**: Breadth-first and depth-first traversals
- **Path Finding**: Check if path exists between vertices
- **Clear**: Remove entire graph

## 📁 Project Structure

```
VISUALIZER/
├── main.py                          # Main Streamlit application
├── requirements.txt                 # Python dependencies
├── README.md                       # Project documentation
├── data_structures/                # Data structure implementations
│   ├── stack.py                    # Stack class
│   ├── queue.py                    # Queue class
│   ├── linked_list.py              # Linked List classes
│   ├── binary_tree.py              # Binary Tree class
│   ├── hash_table.py               # Hash Table class
│   ├── heap.py                     # Heap class
│   └── graph.py                    # Graph class
├── visualizers/                    # Visualization components
│   ├── stack_visualizer.py         # Stack visualization
│   ├── queue_visualizer.py         # Queue visualization
│   ├── linked_list_visualizer.py   # Linked List visualization
│   ├── binary_tree_visualizer.py   # Binary Tree visualization
│   ├── hash_table_visualizer.py    # Hash Table visualization
│   ├── heap_visualizer.py          # Heap visualization
│   └── graph_visualizer.py         # Graph visualization
└── utils/                          # Utility modules
    └── pseudocode.py               # Algorithm pseudocode definitions
```

## 🎯 Use Cases

### 👨‍🎓 For Students

- Learn fundamental data structures visually
- Understand algorithm implementations
- Practice for computer science courses
- Prepare for coding interviews

### 👩‍🏫 For Educators

- Teaching aid for data structure concepts
- Interactive classroom demonstrations
- Visual explanation of abstract concepts
- Engaging learning experience

### 💼 For Interview Preparation

- Practice common data structure operations
- Understand time and space complexity
- Review algorithm implementations
- Build confidence with visual feedback

## 🔧 Customization

### Adding New Data Structures

1. Create implementation in `data_structures/`
2. Add pseudocode to `utils/pseudocode.py`
3. Create visualizer in `visualizers/`
4. Update main navigation in `main.py`

### Modifying Visualizations

- Edit matplotlib plotting code in visualizer files
- Adjust colors, sizes, and layouts
- Add new animation effects
- Customize user interface elements

## 🤝 Contributing

Contributions are welcome! Please feel free to:

- Report bugs and issues
- Suggest new features
- Submit pull requests
- Improve documentation

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- Built with Streamlit for the amazing web app framework
- Matplotlib for powerful visualization capabilities
- Python community for excellent libraries and tools

---

**Start exploring data structures today!** 🚀

Select a data structure from the sidebar and begin your interactive learning journey!

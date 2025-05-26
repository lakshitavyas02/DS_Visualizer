"""
Graph Visualizer using Streamlit and Matplotlib
"""

import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from data_structures.graph import Graph
import time
import math
import random

class GraphVisualizer:
    def __init__(self):
        if 'graph' not in st.session_state:
            st.session_state.graph = Graph()
        self.graph = st.session_state.graph
    
    def render(self):
        st.title("🕸️ Graph Visualizer")
        st.markdown("**Network of Vertices and Edges** - Directed or Undirected connections between nodes")
        
        # Graph type selection
        graph_type = st.selectbox("Graph Type:", ["Undirected", "Directed"])
        directed = graph_type == "Directed"
        
        if directed != self.graph.directed:
            # Create new graph with new type, preserving vertices
            old_vertices = list(self.graph.vertices)
            old_edges = []
            for vertex in self.graph.vertices:
                for neighbor, weight in self.graph.adjacency_list[vertex]:
                    if not self.graph.directed or vertex < neighbor:  # Avoid duplicates
                        old_edges.append((vertex, neighbor, weight))
            
            self.graph = Graph(directed)
            st.session_state.graph = self.graph
            
            # Re-add vertices and edges
            for vertex in old_vertices:
                self.graph.add_vertex(vertex)
            for v1, v2, weight in old_edges:
                self.graph.add_edge(v1, v2, weight)
        
        # Create two columns for controls and visualization
        col1, col2 = st.columns([1, 2])
        
        with col1:
            self._render_controls()
        
        with col2:
            self._render_visualization()
        
        # Display operation history and graph info
        self._render_history_and_info()
    
    def _render_controls(self):
        st.subheader("🎮 Controls")
        
        # Add vertex
        st.markdown("**Add Vertex**")
        vertex_input = st.text_input("Vertex name:", key="vertex_input")
        
        col_add_vertex, col_clear = st.columns(2)
        with col_add_vertex:
            if st.button("➕ Add Vertex"):
                if vertex_input:
                    success, message = self.graph.add_vertex(vertex_input)
                    if success:
                        st.success(message)
                        time.sleep(0.5)
                        st.rerun()
                    else:
                        st.warning(message)
                else:
                    st.warning("Please enter a vertex name")
        
        with col_clear:
            if st.button("🗑️ Clear Graph"):
                self.graph.clear()
                st.rerun()
        
        # Add edge
        st.markdown("**Add Edge**")
        vertices_list = list(self.graph.vertices)
        
        if len(vertices_list) >= 2:
            col_from, col_to = st.columns(2)
            with col_from:
                from_vertex = st.selectbox("From:", vertices_list, key="from_vertex")
            with col_to:
                to_vertex = st.selectbox("To:", vertices_list, key="to_vertex")
            
            weight = st.number_input("Weight:", value=1, min_value=1, max_value=100)
            
            if st.button("🔗 Add Edge"):
                if from_vertex and to_vertex:
                    success, message = self.graph.add_edge(from_vertex, to_vertex, weight)
                    if success:
                        st.success(message)
                        time.sleep(0.5)
                        st.rerun()
                    else:
                        st.error(message)
        else:
            st.info("Add at least 2 vertices to create edges")
        
        # Remove operations
        if vertices_list:
            st.markdown("**Remove Operations**")
            
            # Remove vertex
            remove_vertex = st.selectbox("Remove vertex:", vertices_list, key="remove_vertex")
            if st.button("🗑️ Remove Vertex"):
                success, message = self.graph.remove_vertex(remove_vertex)
                if success:
                    st.success(message)
                    time.sleep(0.5)
                    st.rerun()
                else:
                    st.error(message)
            
            # Remove edge
            if len(vertices_list) >= 2:
                col_from_rem, col_to_rem = st.columns(2)
                with col_from_rem:
                    from_vertex_rem = st.selectbox("From:", vertices_list, key="from_vertex_rem")
                with col_to_rem:
                    to_vertex_rem = st.selectbox("To:", vertices_list, key="to_vertex_rem")
                
                if st.button("🔗❌ Remove Edge"):
                    success, message = self.graph.remove_edge(from_vertex_rem, to_vertex_rem)
                    if success:
                        st.success(message)
                        time.sleep(0.5)
                        st.rerun()
                    else:
                        st.error(message)
        
        # Traversal operations
        if vertices_list:
            st.markdown("**Graph Traversal**")
            start_vertex = st.selectbox("Start vertex:", vertices_list, key="start_vertex")
            
            col_bfs, col_dfs = st.columns(2)
            with col_bfs:
                if st.button("🔍 BFS"):
                    result, message = self.graph.bfs(start_vertex)
                    st.info(f"BFS: {result}")
            
            with col_dfs:
                if st.button("🔍 DFS"):
                    result, message = self.graph.dfs(start_vertex)
                    st.info(f"DFS: {result}")
            
            # Path finding
            st.markdown("**Path Finding**")
            col_path_from, col_path_to = st.columns(2)
            with col_path_from:
                path_from = st.selectbox("From:", vertices_list, key="path_from")
            with col_path_to:
                path_to = st.selectbox("To:", vertices_list, key="path_to")
            
            if st.button("🛤️ Find Path"):
                exists, message = self.graph.has_path(path_from, path_to)
                if exists:
                    st.success(message)
                else:
                    st.warning(message)
    
    def _render_visualization(self):
        st.subheader("📊 Graph Visualization")
        
        if self.graph.is_empty():
            st.info("Graph is empty. Add some vertices and edges to see the visualization!")
            return
        
        # Get graph data
        graph_data = self.graph.get_graph_data()
        vertices = graph_data['vertices']
        edges = graph_data['edges']
        
        # Create matplotlib figure
        fig, ax = plt.subplots(figsize=(12, 8))
        
        # Generate positions for vertices (circular layout)
        positions = self._generate_positions(vertices)
        
        # Draw edges first (so they appear behind vertices)
        self._draw_edges(ax, edges, positions, graph_data['directed'])
        
        # Draw vertices
        self._draw_vertices(ax, vertices, positions)
        
        # Set axis properties
        ax.set_xlim(-1.5, 1.5)
        ax.set_ylim(-1.5, 1.5)
        ax.set_aspect('equal')
        ax.axis('off')
        
        graph_type = "Directed" if graph_data['directed'] else "Undirected"
        ax.set_title(f'{graph_type} Graph Visualization', fontsize=16, fontweight='bold')
        
        # Display the plot
        st.pyplot(fig)
        plt.close()
    
    def _generate_positions(self, vertices):
        """Generate positions for vertices in a circular layout"""
        positions = {}
        n = len(vertices)
        
        if n == 1:
            positions[vertices[0]] = (0, 0)
        else:
            for i, vertex in enumerate(vertices):
                angle = 2 * math.pi * i / n
                x = math.cos(angle)
                y = math.sin(angle)
                positions[vertex] = (x, y)
        
        return positions
    
    def _draw_vertices(self, ax, vertices, positions):
        """Draw graph vertices"""
        for vertex in vertices:
            x, y = positions[vertex]
            
            # Draw vertex circle
            circle = patches.Circle((x, y), 0.15, linewidth=2, 
                                   edgecolor='black', facecolor='lightblue')
            ax.add_patch(circle)
            
            # Add vertex label
            ax.text(x, y, str(vertex), ha='center', va='center', 
                   fontsize=12, fontweight='bold')
    
    def _draw_edges(self, ax, edges, positions, directed):
        """Draw graph edges"""
        for vertex1, vertex2, weight in edges:
            x1, y1 = positions[vertex1]
            x2, y2 = positions[vertex2]
            
            # Calculate edge endpoints (adjust for vertex radius)
            dx = x2 - x1
            dy = y2 - y1
            length = math.sqrt(dx*dx + dy*dy)
            
            if length > 0:
                # Normalize direction vector
                dx_norm = dx / length
                dy_norm = dy / length
                
                # Adjust start and end points
                start_x = x1 + 0.15 * dx_norm
                start_y = y1 + 0.15 * dy_norm
                end_x = x2 - 0.15 * dx_norm
                end_y = y2 - 0.15 * dy_norm
                
                # Draw edge
                if directed:
                    # Draw arrow for directed graph
                    ax.annotate('', xy=(end_x, end_y), xytext=(start_x, start_y),
                               arrowprops=dict(arrowstyle='->', color='darkblue', lw=2))
                else:
                    # Draw line for undirected graph
                    ax.plot([start_x, end_x], [start_y, end_y], 'darkblue', linewidth=2)
                
                # Add weight label
                mid_x = (start_x + end_x) / 2
                mid_y = (start_y + end_y) / 2
                
                # Offset label slightly to avoid overlap with edge
                offset_x = -0.1 * dy_norm if abs(dy_norm) > 0.1 else 0.1
                offset_y = 0.1 * dx_norm if abs(dx_norm) > 0.1 else 0.1
                
                ax.text(mid_x + offset_x, mid_y + offset_y, str(weight), 
                       ha='center', va='center', fontsize=10, 
                       bbox=dict(boxstyle="round,pad=0.2", facecolor="white", alpha=0.8))
    
    def _render_history_and_info(self):
        st.subheader("📝 Operation History & Graph Info")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Recent Operations**")
            history = self.graph.get_history()
            if history:
                for i, operation in enumerate(reversed(history[-8:])):
                    st.text(f"{len(history)-i}: {operation}")
            else:
                st.text("No operations performed yet")
            
            if st.button("Clear History"):
                self.graph.clear_history()
                st.rerun()
        
        with col2:
            st.markdown("**Graph Information**")
            st.write(f"**Type:** {'Directed' if self.graph.directed else 'Undirected'}")
            st.write(f"**Vertices:** {self.graph.vertex_count()}")
            st.write(f"**Edges:** {self.graph.edge_count()}")
            st.write(f"**Empty:** {self.graph.is_empty()}")
            
            # Show adjacency list
            st.markdown("**Adjacency List:**")
            if not self.graph.is_empty():
                for vertex in sorted(self.graph.vertices):
                    neighbors = [f"{neighbor}({weight})" for neighbor, weight in self.graph.adjacency_list[vertex]]
                    neighbors_str = ", ".join(neighbors) if neighbors else "[]"
                    st.text(f"  {vertex}: {neighbors_str}")
            else:
                st.text("  Graph is empty")
            
            # Show adjacency matrix
            if not self.graph.is_empty() and self.graph.vertex_count() <= 6:
                st.markdown("**Adjacency Matrix:**")
                matrix, vertices_list = self.graph.get_adjacency_matrix()
                
                # Create header
                header = "    " + " ".join(f"{v:>3}" for v in vertices_list)
                st.text(header)
                
                # Create matrix rows
                for i, vertex in enumerate(vertices_list):
                    row = f"{vertex:>3} " + " ".join(f"{matrix[i][j]:>3}" for j in range(len(vertices_list)))
                    st.text(row)
    
    def render_with_pseudocode(self):
        """Render the visualizer with pseudocode sections"""
        self.render()
        
        # Pseudocode section
        st.markdown("---")
        st.subheader("📚 Graph Algorithms")
        
        # Tabs for different operations
        tab1, tab2, tab3, tab4 = st.tabs(["Add Edge", "BFS", "DFS", "Path Finding"])
        
        with tab1:
            st.code("""
ALGORITHM AddEdge(graph, vertex1, vertex2, weight)
BEGIN
    1. ADD vertex1 to graph if not exists
    2. ADD vertex2 to graph if not exists
    3. ADD (vertex2, weight) to adjacency_list[vertex1]
    4. IF graph is undirected THEN
        ADD (vertex1, weight) to adjacency_list[vertex2]
END
            """, language="text")
        
        with tab2:
            st.code("""
ALGORITHM BFS(graph, start_vertex)
BEGIN
    1. CREATE empty queue
    2. CREATE empty visited set
    3. ENQUEUE start_vertex to queue
    4. WHILE queue is not empty DO
        vertex = DEQUEUE from queue
        IF vertex not in visited THEN
            ADD vertex to visited
            PRINT vertex
            FOR each neighbor of vertex DO
                IF neighbor not in visited THEN
                    ENQUEUE neighbor to queue
END
            """, language="text")
        
        with tab3:
            st.code("""
ALGORITHM DFS(graph, start_vertex)
BEGIN
    1. CREATE empty visited set
    2. DFS_Recursive(start_vertex, visited)
END

ALGORITHM DFS_Recursive(vertex, visited)
BEGIN
    1. ADD vertex to visited
    2. PRINT vertex
    3. FOR each neighbor of vertex DO
        IF neighbor not in visited THEN
            DFS_Recursive(neighbor, visited)
END
            """, language="text")
        
        with tab4:
            st.code("""
ALGORITHM HasPath(graph, start, end)
BEGIN
    1. CREATE empty queue
    2. CREATE empty visited set
    3. ENQUEUE start to queue
    4. WHILE queue is not empty DO
        vertex = DEQUEUE from queue
        IF vertex == end THEN
            RETURN true
        IF vertex not in visited THEN
            ADD vertex to visited
            FOR each neighbor of vertex DO
                IF neighbor not in visited THEN
                    ENQUEUE neighbor to queue
    5. RETURN false
END
            """, language="text")

"""
Graph Data Structure Implementation (Adjacency List)
"""

from collections import deque, defaultdict

class Graph:
    def __init__(self, directed=False):
        self.adjacency_list = defaultdict(list)
        self.directed = directed
        self.history = []
        self.vertices = set()
    
    def add_vertex(self, vertex):
        """Add a vertex to the graph"""
        if vertex not in self.vertices:
            self.vertices.add(vertex)
            self.adjacency_list[vertex] = []
            self.history.append(f"Added vertex {vertex}")
            return True, f"Successfully added vertex {vertex}"
        else:
            return False, f"Vertex {vertex} already exists"
    
    def add_edge(self, vertex1, vertex2, weight=1):
        """Add an edge between two vertices"""
        # Add vertices if they don't exist
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        
        # Check if edge already exists
        for neighbor, w in self.adjacency_list[vertex1]:
            if neighbor == vertex2:
                return False, f"Edge {vertex1} -> {vertex2} already exists"
        
        # Add edge
        self.adjacency_list[vertex1].append((vertex2, weight))
        
        # For undirected graph, add reverse edge
        if not self.directed:
            self.adjacency_list[vertex2].append((vertex1, weight))
        
        edge_type = "directed" if self.directed else "undirected"
        self.history.append(f"Added {edge_type} edge {vertex1} -> {vertex2} (weight: {weight})")
        return True, f"Successfully added edge {vertex1} -> {vertex2}"
    
    def remove_vertex(self, vertex):
        """Remove a vertex and all its edges"""
        if vertex not in self.vertices:
            return False, f"Vertex {vertex} does not exist"
        
        # Remove all edges to this vertex
        for v in self.vertices:
            self.adjacency_list[v] = [(neighbor, weight) for neighbor, weight in self.adjacency_list[v] 
                                     if neighbor != vertex]
        
        # Remove the vertex itself
        del self.adjacency_list[vertex]
        self.vertices.remove(vertex)
        
        self.history.append(f"Removed vertex {vertex}")
        return True, f"Successfully removed vertex {vertex}"
    
    def remove_edge(self, vertex1, vertex2):
        """Remove an edge between two vertices"""
        if vertex1 not in self.vertices or vertex2 not in self.vertices:
            return False, f"One or both vertices do not exist"
        
        # Remove edge from vertex1 to vertex2
        original_length = len(self.adjacency_list[vertex1])
        self.adjacency_list[vertex1] = [(neighbor, weight) for neighbor, weight in self.adjacency_list[vertex1] 
                                       if neighbor != vertex2]
        
        edge_removed = len(self.adjacency_list[vertex1]) < original_length
        
        # For undirected graph, remove reverse edge
        if not self.directed and edge_removed:
            self.adjacency_list[vertex2] = [(neighbor, weight) for neighbor, weight in self.adjacency_list[vertex2] 
                                           if neighbor != vertex1]
        
        if edge_removed:
            self.history.append(f"Removed edge {vertex1} -> {vertex2}")
            return True, f"Successfully removed edge {vertex1} -> {vertex2}"
        else:
            return False, f"Edge {vertex1} -> {vertex2} does not exist"
    
    def get_neighbors(self, vertex):
        """Get neighbors of a vertex"""
        if vertex not in self.vertices:
            return [], f"Vertex {vertex} does not exist"
        
        neighbors = [neighbor for neighbor, weight in self.adjacency_list[vertex]]
        self.history.append(f"Retrieved neighbors of {vertex}: {neighbors}")
        return neighbors, f"Neighbors of {vertex}: {neighbors}"
    
    def bfs(self, start_vertex):
        """Breadth-First Search traversal"""
        if start_vertex not in self.vertices:
            return [], f"Start vertex {start_vertex} does not exist"
        
        visited = set()
        queue = deque([start_vertex])
        traversal_order = []
        
        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                traversal_order.append(vertex)
                
                # Add unvisited neighbors to queue
                for neighbor, weight in self.adjacency_list[vertex]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        
        self.history.append(f"BFS from {start_vertex}: {traversal_order}")
        return traversal_order, f"BFS traversal: {traversal_order}"
    
    def dfs(self, start_vertex):
        """Depth-First Search traversal"""
        if start_vertex not in self.vertices:
            return [], f"Start vertex {start_vertex} does not exist"
        
        visited = set()
        traversal_order = []
        
        def dfs_recursive(vertex):
            visited.add(vertex)
            traversal_order.append(vertex)
            
            for neighbor, weight in self.adjacency_list[vertex]:
                if neighbor not in visited:
                    dfs_recursive(neighbor)
        
        dfs_recursive(start_vertex)
        self.history.append(f"DFS from {start_vertex}: {traversal_order}")
        return traversal_order, f"DFS traversal: {traversal_order}"
    
    def has_path(self, start, end):
        """Check if there's a path between two vertices"""
        if start not in self.vertices or end not in self.vertices:
            return False, f"One or both vertices do not exist"
        
        visited = set()
        queue = deque([start])
        
        while queue:
            vertex = queue.popleft()
            if vertex == end:
                self.history.append(f"Path found from {start} to {end}")
                return True, f"Path exists from {start} to {end}"
            
            if vertex not in visited:
                visited.add(vertex)
                for neighbor, weight in self.adjacency_list[vertex]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        
        self.history.append(f"No path from {start} to {end}")
        return False, f"No path exists from {start} to {end}"
    
    def get_graph_data(self):
        """Get graph data for visualization"""
        edges = []
        for vertex in self.vertices:
            for neighbor, weight in self.adjacency_list[vertex]:
                if self.directed or vertex < neighbor:  # Avoid duplicate edges for undirected graphs
                    edges.append((vertex, neighbor, weight))
        
        return {
            'vertices': list(self.vertices),
            'edges': edges,
            'directed': self.directed
        }
    
    def get_adjacency_matrix(self):
        """Get adjacency matrix representation"""
        vertices_list = sorted(list(self.vertices))
        size = len(vertices_list)
        matrix = [[0 for _ in range(size)] for _ in range(size)]
        
        vertex_to_index = {vertex: i for i, vertex in enumerate(vertices_list)}
        
        for vertex in self.vertices:
            for neighbor, weight in self.adjacency_list[vertex]:
                i = vertex_to_index[vertex]
                j = vertex_to_index[neighbor]
                matrix[i][j] = weight
        
        return matrix, vertices_list
    
    def is_empty(self):
        """Check if graph is empty"""
        return len(self.vertices) == 0
    
    def vertex_count(self):
        """Get number of vertices"""
        return len(self.vertices)
    
    def edge_count(self):
        """Get number of edges"""
        total_edges = sum(len(neighbors) for neighbors in self.adjacency_list.values())
        return total_edges if self.directed else total_edges // 2
    
    def clear(self):
        """Clear the graph"""
        self.adjacency_list.clear()
        self.vertices.clear()
        self.history.append("Graph cleared")
    
    def get_history(self):
        """Return operation history"""
        return self.history.copy()
    
    def clear_history(self):
        """Clear operation history"""
        self.history.clear()
    
    def __str__(self):
        result = f"{'Directed' if self.directed else 'Undirected'} Graph:\n"
        for vertex in sorted(self.vertices):
            neighbors = [f"{neighbor}(w:{weight})" for neighbor, weight in self.adjacency_list[vertex]]
            result += f"  {vertex}: {neighbors}\n"
        return result

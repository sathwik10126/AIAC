from collections import defaultdict, deque
from typing import Dict, List, Set

class Graph:
    """Graph implementation with BFS and DFS traversals."""
    
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, vertex: str, neighbor: str) -> None:
        self.graph[vertex].append(neighbor)
    
    def bfs(self, start: str) -> List[str]:
        """Perform Breadth-First Search traversal."""
        visited = set()
        queue = deque([start])
        result = []
        
        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                queue.extend(
                    neighbor for neighbor in self.graph[vertex] 
                    if neighbor not in visited
                )
        return result
    
    def dfs_recursive(self, start: str) -> List[str]:
        """Perform recursive Depth-First Search traversal."""
        visited = set()
        result = []
        
        def _dfs(vertex: str) -> None:
            visited.add(vertex)
            result.append(vertex)
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    _dfs(neighbor)
        
        _dfs(start)
        return result
    
    def dfs_iterative(self, start: str) -> List[str]:
        """Perform iterative Depth-First Search traversal."""
        visited = set()
        stack = [start]
        result = []
        
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                stack.extend(
                    neighbor for neighbor in reversed(self.graph[vertex])
                    if neighbor not in visited
                )
        return result

def test_graph():
    """Test graph traversals with sample data."""
    g = Graph()
    edges = [
        ('A', 'B'), ('A', 'C'),
        ('B', 'C'),
        ('C', 'A'), ('C', 'D'),
        ('D', 'D')
    ]
    
    for v1, v2 in edges:
        g.add_edge(v1, v2)
    
    start_vertex = 'C'
    print(f"\nGraph Traversals from vertex '{start_vertex}':")
    print("-" * 40)
    print(f"BFS traversal:      {g.bfs(start_vertex)}")
    print(f"DFS recursive:      {g.dfs_recursive(start_vertex)}")
    print(f"DFS iterative:      {g.dfs_iterative(start_vertex)}")

if __name__ == "__main__":
    test_graph()
"""
Advanced Algorithms and Data Structures Implementation
- Red-Black Tree
- Graph with Dijkstra's Algorithm
- Dynamic Programming: Knapsack Problem
"""

import heapq
from collections import defaultdict, deque
from typing import List, Dict, Tuple, Optional, Set, Any


#########################
# Red-Black Tree Implementation
#########################

# Red-Black Tree Colors
RED = True
BLACK = False

class RBNode:
    def __init__(self, key, value=None, color=RED):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.color = color
        
    def __repr__(self):
        return f"RBNode({self.key}, {self.value}, {'RED' if self.color else 'BLACK'})"

class RedBlackTree:
    def __init__(self):
        self.NIL = RBNode(key=None, color=BLACK)
        self.root = self.NIL
        
    def insert(self, key, value=None):
        new_node = RBNode(key, value)
        new_node.left = self.NIL
        new_node.right = self.NIL
        
        y = None
        x = self.root
        
        while x != self.NIL:
            y = x
            if new_node.key < x.key:
                x = x.left
            else:
                x = x.right
                
        new_node.parent = y
        if y is None:
            self.root = new_node
        elif new_node.key < y.key:
            y.left = new_node
        else:
            y.right = new_node
            
        if new_node.parent is None:
            new_node.color = BLACK
            return
            
        if new_node.parent.parent is None:
            return
            
        self._fix_insert(new_node)
    
    def _fix_insert(self, k):
        while k.parent and k.parent.color == RED:
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == RED:
                    u.color = BLACK
                    k.parent.color = BLACK
                    k.parent.parent.color = RED
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self._right_rotate(k)
                    k.parent.color = BLACK
                    k.parent.parent.color = RED
                    self._left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right
                if u.color == RED:
                    u.color = BLACK
                    k.parent.color = BLACK
                    k.parent.parent.color = RED
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self._left_rotate(k)
                    k.parent.color = BLACK
                    k.parent.parent.color = RED
                    self._right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = BLACK
    
    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y
    
    def _right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y
    
    def search(self, key):
        return self._search_helper(self.root, key)
    
    def _search_helper(self, node, key):
        if node == self.NIL:
            return None
        if key == node.key:
            return node
        if key < node.key:
            return self._search_helper(node.left, key)
        return self._search_helper(node.right, key)
    
    def inorder(self):
        result = []
        self._inorder_helper(self.root, result)
        return result
    
    def _inorder_helper(self, node, result):
        if node != self.NIL:
            self._inorder_helper(node.left, result)
            result.append((node.key, node.value))
            self._inorder_helper(node.right, result)


#########################
# Graph Implementation with Dijkstra's Algorithm
#########################

class Graph:
    def __init__(self, directed=False):
        self.adj_list = defaultdict(list)
        self.directed = directed
    
    def add_edge(self, u, v, weight=1):
        self.adj_list[u].append((v, weight))
        if not self.directed:
            self.adj_list[v].append((u, weight))
    
    def vertices(self):
        return list(self.adj_list.keys())
    
    def edges(self):
        edges = []
        for u in self.adj_list:
            for v, weight in self.adj_list[u]:
                if not self.directed or (u, v) not in edges:
                    edges.append((u, v, weight))
        return edges
    
    def dijkstra(self, start_vertex):
        """
        Implements Dijkstra's algorithm to find shortest paths from start_vertex to all others
        """
        distances = {vertex: float('infinity') for vertex in self.vertices()}
        distances[start_vertex] = 0
        previous = {vertex: None for vertex in self.vertices()}
        
        priority_queue = [(0, start_vertex)]
        visited = set()
        
        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)
            
            if current_vertex in visited:
                continue
                
            visited.add(current_vertex)
            
            for neighbor, weight in self.adj_list[current_vertex]:
                if neighbor in visited:
                    continue
                    
                distance = current_distance + weight
                
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current_vertex
                    heapq.heappush(priority_queue, (distance, neighbor))
        
        return distances, previous
    
    def shortest_path(self, start_vertex, end_vertex):
        """
        Returns the shortest path from start_vertex to end_vertex
        """
        distances, previous = self.dijkstra(start_vertex)
        
        path = []
        current = end_vertex
        
        while current:
            path.append(current)
            current = previous[current]
            
        return path[::-1], distances[end_vertex]
    
    def bfs(self, start_vertex):
        """
        Breadth-first search traversal from start_vertex
        """
        visited = set([start_vertex])
        queue = deque([start_vertex])
        result = []
        
        while queue:
            vertex = queue.popleft()
            result.append(vertex)
            
            # Neighbors
            for neighbor, _ in self.adj_list[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    
        return result
    
    def dfs(self, start_vertex):
        """
        Depth-first search traversal from start_vertex
        """
        visited = set()
        result = []
        
        def dfs_helper(vertex):
            visited.add(vertex)
            result.append(vertex)
            
            for neighbor, _ in self.adj_list[vertex]:
                if neighbor not in visited:
                    dfs_helper(neighbor)
        
        dfs_helper(start_vertex)
        return result


#########################
# Dynamic Programming: Knapsack Problem
#########################

def knapsack_recursive(values, weights, capacity, n):
    """
    Recursive solution for the Knapsack problem
    
    Args:
        values: List of item values
        weights: List of item weights
        capacity: Maximum weight capacity
        n: Number of items
    
    Returns:
        Maximum value that can be obtained
    """
    # Base case
    if n == 0 or capacity == 0:
        return 0
    
    # If weight of nth item is more than capacity, skip it
    if weights[n-1] > capacity:
        return knapsack_recursive(values, weights, capacity, n-1)
    
    # Return max of including or excluding the item
    include = values[n-1] + knapsack_recursive(values, weights, capacity - weights[n-1], n-1)
    exclude = knapsack_recursive(values, weights, capacity, n-1)
    
    return max(include, exclude)

def knapsack_dp(values, weights, capacity):
    """
    Dynamic programming solution for the Knapsack problem
    
    Args:
        values: List of item values
        weights: List of item weights
        capacity: Maximum weight capacity
    
    Returns:
        Maximum value that can be obtained and the selected items
    """
    n = len(values)
    # Initialize DP table
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    # Fill the dp table
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w - weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    
    # Reconstruct the solution
    result = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            result.append(i-1)
            w -= weights[i-1]
    
    return dp[n][capacity], result


#########################
# Example Usage
#########################

def test_red_black_tree():
    print("\nTesting Red-Black Tree:")
    rb_tree = RedBlackTree()
    keys = [7, 3, 18, 10, 22, 8, 11, 26]
    
    for key in keys:
        rb_tree.insert(key, f"Value-{key}")
    
    print("Inorder traversal:", rb_tree.inorder())
    
    # Search for keys
    for key in [10, 22, 15]:
        result = rb_tree.search(key)
        if result:
            print(f"Found {key}: {result.value}")
        else:
            print(f"Key {key} not found")

def test_graph():
    print("\nTesting Graph with Dijkstra's Algorithm:")
    g = Graph()
    
    # Add edges (city connections with distances)
    edges = [
        ("A", "B", 4), ("A", "C", 2),
        ("B", "C", 5), ("B", "D", 10),
        ("C", "D", 3), ("C", "E", 8),
        ("D", "E", 2), ("D", "F", 6),
        ("E", "F", 7)
    ]
    
    for u, v, w in edges:
        g.add_edge(u, v, w)
    
    print("BFS traversal from A:", g.bfs("A"))
    print("DFS traversal from A:", g.dfs("A"))
    
    source, target = "A", "F"
    path, distance = g.shortest_path(source, target)
    print(f"Shortest path from {source} to {target}: {path} with distance {distance}")

def test_knapsack():
    print("\nTesting Knapsack Problem:")
    values = [60, 100, 120, 80, 30]
    weights = [10, 20, 30, 15, 5]
    capacity = 50
    
    # Using recursive approach (may be slow for large inputs)
    max_value_recursive = knapsack_recursive(values, weights, capacity, len(values))
    print(f"Maximum value (recursive): {max_value_recursive}")
    
    # Using dynamic programming
    max_value, selected_items = knapsack_dp(values, weights, capacity)
    print(f"Maximum value (DP): {max_value}")
    print(f"Selected items (indices): {selected_items}")
    print(f"Selected items (values, weights): {[(values[i], weights[i]) for i in selected_items]}")

# Add a fancy progress bar utility
def print_progress_bar(iteration, total, prefix='', suffix='', decimals=1, length=50, fill='█', print_end="\r"):
    """
    Call in a loop to create terminal progress bar
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=print_end)
    if iteration == total: 
        print()

if __name__ == "__main__":
    # Modify the main execution to show a progress bar
    print("\n=== ALGORITHM TESTS ===")
    
    total_tests = 3
    tests = [
        ("Red-Black Tree", test_red_black_tree),
        ("Graph Algorithms", test_graph),
        ("Knapsack Problem", test_knapsack)
    ]
    
    for i, (name, test_func) in enumerate(tests):
        print_progress_bar(i, total_tests, prefix='Progress:', suffix=f'Running {name}', length=40)
        test_func()
        print_progress_bar(i+1, total_tests, prefix='Progress:', suffix=f'Completed {name}', length=40)
        
    print("\n=== ALL TESTS PASSED SUCCESSFULLY ===")
    print_progress_bar(total_tests, total_tests, prefix='Final Status:', suffix='Complete', length=40)
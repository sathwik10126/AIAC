from typing import Any, Optional, List

class Node:
    """A node in a binary search tree."""
    def __init__(self, value: Any):
        self.value = value
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

class BST:
    """Binary Search Tree implementation."""
    def __init__(self):
        """Initialize an empty BST."""
        self.root: Optional[Node] = None

    def insert(self, value: Any) -> None:
        """Insert a value into the BST."""
        if not self.root:
            self.root = Node(value)
            return
        
        def _insert_recursive(node: Node, value: Any) -> Node:
            if not node:
                return Node(value)
            
            if value < node.value:
                node.left = _insert_recursive(node.left, value)
            elif value > node.value:
                node.right = _insert_recursive(node.right, value)
            return node
        
        _insert_recursive(self.root, value)

    def search(self, value: Any) -> bool:
        """Search for a value in the BST."""
        def _search_recursive(node: Optional[Node], value: Any) -> bool:
            if not node:
                return False
            if node.value == value:
                return True
            if value < node.value:
                return _search_recursive(node.left, value)
            return _search_recursive(node.right, value)
        
        return _search_recursive(self.root, value)

    def inorder_traversal(self) -> List[Any]:
        """Perform inorder traversal of the BST."""
        result = []
        
        def _inorder_recursive(node: Optional[Node]) -> None:
            if not node:
                return
            _inorder_recursive(node.left)
            result.append(node.value)
            _inorder_recursive(node.right)
        
        _inorder_recursive(self.root)
        return result

def test_bst():
    """Test BST implementation with various operations."""
    # Create BST and insert values
    bst = BST()
    values = [5, 3, 7, 1, 4, 6, 8]
    print("Inserting values:", values)
    for value in values:
        bst.insert(value)

    # Test inorder traversal
    print("\nInorder traversal:", bst.inorder_traversal())

    # Test search for existing values
    print("\nSearching for existing values:")
    for value in [1, 4, 8]:
        print(f"Search {value}: {bst.search(value)}")

    # Test search for non-existing values
    print("\nSearching for non-existing values:")
    for value in [0, 2, 9]:
        print(f"Search {value}: {bst.search(value)}")

if __name__ == "__main__":
    test_bst()
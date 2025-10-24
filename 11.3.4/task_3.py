from typing import Any, Optional

class Node:
    """A node in a singly linked list."""
    def __init__(self, data: Any):
        self.data = data
        self.next: Optional[Node] = None

class LinkedList:
    """Singly linked list implementation."""
    def __init__(self):
        """Initialize empty linked list."""
        self.head: Optional[Node] = None
    
    def insert_at_end(self, data: Any) -> None:
        """Insert a new node at the end of the list."""
        new_node = Node(data)
        
        # If list is empty, make new node the head
        if not self.head:
            self.head = new_node
            return
        
        # Traverse to the last node
        current = self.head
        while current.next:
            current = current.next
            
        # Link the last node to our new node
        current.next = new_node
    
    def delete_value(self, data: Any) -> bool:
        """Delete the first occurrence of data in the list."""
        if not self.head:
            return False
        
        # Special case: deleting head node
        if self.head.data == data:
            self.head = self.head.next  # Move head to next node
            return True
        
        # Search for the node to delete while keeping track of previous node
        current = self.head
        while current.next:
            if current.next.data == data:
                # Update the previous node's next pointer to skip the deleted node
                current.next = current.next.next
                return True
            current = current.next
            
        return False
    
    def traverse(self) -> list:
        """Return list of all values in the linked list."""
        values = []
        current = self.head
        while current:
            values.append(current.data)
            current = current.next
        return values

def test_linked_list():
    """Test the LinkedList implementation."""
    ll = LinkedList()
    
    # Test 1: Empty list
    print("Empty list:", ll.traverse())
    
    # Test 2: Insertions
    ll.insert_at_end(1)
    ll.insert_at_end(2)
    ll.insert_at_end(3)
    print("After insertions:", ll.traverse())
    
    # Test 3: Delete middle value
    ll.delete_value(2)
    print("After deleting 2:", ll.traverse())
    
    # Test 4: Delete head
    ll.delete_value(1)
    print("After deleting head:", ll.traverse())
    
    # Test 5: Delete non-existent value
    result = ll.delete_value(5)
    print("Delete non-existent value:", result)
    
    # Test 6: Delete last remaining value
    ll.delete_value(3)
    print("After deleting last value:", ll.traverse())
    
    # Test 7: Insert after empty
    ll.insert_at_end(10)
    print("After inserting into empty list:", ll.traverse())

if __name__ == "__main__":
    test_linked_list()
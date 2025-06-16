# Node class represents a single node in the binary search tree
class Node:
    def __init__(self, info):
        """
        Initialize a new tree node
        
        Args:
            info: The value to be stored in the node
        """
        self.info = info      # Node's value
        self.left = None      # Left child reference
        self.right = None     # Right child reference
        self.level = None     # Level in the tree (not used in this solution)

    def __str__(self):
        """String representation of the node"""
        return str(self.info)


class BinarySearchTree:
    """Implementation of a Binary Search Tree data structure"""
    
    def __init__(self):
        """Initialize an empty binary search tree"""
        self.root = None

    def create(self, val):
        """
        Insert a new value into the binary search tree
        
        Args:
            val: Value to insert into the tree
            
        Note:
            - If value is less than current node, go left
            - If value is greater than current node, go right
            - If value equals current node, ignore (no duplicates)
        """
        if self.root == None:
            # If tree is empty, create root node
            self.root = Node(val)
        else:
            current = self.root
            
            while True:
                if val < current.info:
                    # Value is less than current node, go left
                    if current.left:
                        current = current.left
                    else:
                        # Found position to insert new node
                        current.left = Node(val)
                        break
                elif val > current.info:
                    # Value is greater than current node, go right
                    if current.right:
                        current = current.right
                    else:
                        # Found position to insert new node
                        current.right = Node(val)
                        break
                else:
                    # Value already exists in tree
                    break


def h(root, current):
    """
    Helper function to calculate the height of the tree recursively
    
    Args:
        root: Current node being processed
        current: Current height in the recursion (-1 for root level)
    
    Returns:
        int: Maximum height found in this subtree
    """
    if root == None:
        # Base case: reached a null node
        return current
    else:
        # Recursively calculate height of left and right subtrees
        # and return the maximum height found
        return max(h(root.left, current + 1), h(root.right, current + 1))


def height(root):
    """
    Calculate the height of a binary tree
    
    Args:
        root: Root node of the tree
    
    Returns:
        int: Height of the tree (number of edges in longest path from root to leaf)
    """
    return h(root, -1)


# Driver code
tree = BinarySearchTree()
# Read number of nodes
t = int(input())

# Read space-separated values and convert to integer list
arr = list(map(int, input().split()))

# Create the binary search tree
for i in range(t):
    tree.create(arr[i])

# Print the height of the tree
print(height(tree.root))

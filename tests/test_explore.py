
from src.binary_tree import Tree

class TestBinaryExplore:

    def test_creation(self):
        root = Tree()
        left = Tree()
        right = Tree()
        
        root.left = left 
        root.right = right 

        assert root.left == left
    
    def test_binary_length(self):

        root = Tree()
        left = Tree()
        right = Tree()
        
        root.left = left 
        root.right = right 

        assert Tree.length(root) == 3
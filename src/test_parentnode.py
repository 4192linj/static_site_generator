import unittest
from htmlnode import ParentNode, LeafNode

class TestParentNode(unittest.TestCase):
    def test_init(self):
        node = ParentNode(tag="div", children=[LeafNode(value="Hello, World!")])
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.children, [LeafNode(value="Hello, World!")])
        self.assertEqual(node.props, None)

    def test_to_html(self):
        node = ParentNode(tag="div", children=[LeafNode(value="Hello, World!")])
        self.assertEqual(node.to_html(), "<div>Hello, World!</div>")
        node = ParentNode("p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
        )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")
        

if __name__ == "__main__":
    unittest.main()
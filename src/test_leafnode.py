import unittest
from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_init(self):
        node = LeafNode(value="Hello, World!")
        self.assertEqual(node.value, "Hello, World!")
        self.assertEqual(node.tag, None)
        self.assertEqual(node.props, None)

    def test_value_error_raised(self):
        node = LeafNode(value=None)
        self.assertRaises(ValueError, node.to_html)

    def test_to_html(self):
        node = LeafNode(value="Hello, World!")
        self.assertEqual(node.to_html(), "Hello, World!")
        node = LeafNode(value="Hello, World!", tag="div")
        self.assertEqual(node.to_html(), "<div>Hello, World!</div>")
        node = LeafNode(value="Hello, World!", tag="div", props={"class": "test", "id": "test"})
        self.assertEqual(node.to_html(), "<div class=test id=test>Hello, World!</div>")

if __name__ == "__main__":
    unittest.main()
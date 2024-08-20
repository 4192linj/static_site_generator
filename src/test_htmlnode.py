import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_init(self):
        node = HTMLNode(tag="div", value="Hello, World!", children=[], props={})
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "Hello, World!")
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {})
    
    def test_props_to_html(self):
        node = HTMLNode(tag="div", value="Hello, World!", children=[], props={"class": "test", "id": "test"})
        self.assertEqual(node.props_to_html(), "class=test id=test")

    def test_to_html(self):
        node = HTMLNode(tag="div", value="Hello, World!", children=[], props={"class": "test", "id": "test"})
        self.assertRaises(NotImplementedError, node.to_html)

if __name__ == "__main__":
    unittest.main()
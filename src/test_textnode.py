import unittest
from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        n_1 = TextNode("Hello", "Bold", "www.123.com")
        n_2 = TextNode("Hello", "Bold", "www.123.com")
        self.assertEqual(n_1,n_2)
    
    def test_not_eq(self):
        n_1 = TextNode("Hello", "Bold", "www.456.com")
        n_2 = TextNode("Hiya", "Italic", "www.123.com")
        self.assertNotEqual(n_1,n_2)
    
    def test_none_case(self):
        n_1 = TextNode("Hello", "Bold", "www.456.com")
        n_2 = None
        self.assertNotEqual(n_1,n_2)

    def test_create_node(self):
        n_1 = TextNode("Hello", "Bold", "www.123.com")
        self.assertEqual(n_1.url, "www.123.com")

if __name__ == "__main__":
    unittest.main()
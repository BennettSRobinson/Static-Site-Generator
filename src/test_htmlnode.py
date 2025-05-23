import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_only_props_eq(self):
        node = HTMLNode(None, None, None, {"href": "https://www.google.com","target": "_blank"})
        node2 = " href=\"https://www.google.com\" target=\"_blank\""
        self.assertEqual(node.props_to_html(), node2)
    def test_no_space(self):
        node = HTMLNode(None, None, None, {"href": "https://www.google.com","target": "_blank"})
        node2 = " href=\"https://www.google.com\"target=\"_blank\""
        self.assertNotEqual(node.props_to_html(), node2)
    def test_multiple_props(self):
        node = HTMLNode(None, None, None, {"href": "https://www.google.com","target": "_blank", "title": "this is an example"})
        node2 = " href=\"https://www.google.com\" target=\"_blank\" title=\"this is an example\""
        self.assertEqual(node.props_to_html(), node2)
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')
    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")
    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
if __name__ == "__main__":
    unittest.main()
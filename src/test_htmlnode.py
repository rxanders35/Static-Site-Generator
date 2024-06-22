import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        htmlnode = HTMLNode(
            "div",
            "Hello world!", 
             None, 
            {"class":"greeting", " href":"https://boot.dev"},
            )
        self.assertEqual(
            htmlnode.props_to_html(), 
            'class = "greeting" href = "https://boot.dev"'
        )

if __name__ == "__main__":
    unittest.main()
    

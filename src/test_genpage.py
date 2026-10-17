import unittest
from genpage import extract_title

class TestGenPage(unittest.TestCase):
    def test_extract_title(self):
        title = extract_title("# Hello")
        self.assertEqual(title, "Hello")

    def test_extract_title_with_whitespace(self):
        title = extract_title("#    Hello World   ")
        self.assertEqual(title, "Hello World")

    def test_extract_title_multiline(self):
        md = """
This is a paragraph

#  The Real Title  

- item 1
"""
        title = extract_title(md)
        self.assertEqual(title, "The Real Title")

    def test_extract_title_no_header_raises(self):
        with self.assertRaises(Exception):
            extract_title("No header here")

    def test_extract_title_only_h2_raises(self):
        with self.assertRaises(Exception):
            extract_title("## Only an H2 Header")

    def test_extract_title_h2_before_h1(self):
        md = "## Subheading\n\n# The Main Title"
        self.assertEqual(extract_title(md), "The Main Title")

    def test_extract_title_empty_raises(self):
        with self.assertRaises(Exception):
            extract_title("")

if __name__ == "__main__":
    unittest.main()

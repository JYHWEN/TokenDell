# test_tokendell.py
"""
Tests for TokenDell module.
"""

import unittest
from tokendell import TokenDell

class TestTokenDell(unittest.TestCase):
    """Test cases for TokenDell class."""

    def test_initialization(self):
        """Test class initialization."""
        instance = TokenDell()
        self.assertIsInstance(instance, TokenDell)

    def test_run_method(self):
        """Test the run method."""
        instance = TokenDell()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

# test_errorcatch.py
"""
Tests for ErrorCatch module.
"""

import unittest
from errorcatch import ErrorCatch

class TestErrorCatch(unittest.TestCase):
    """Test cases for ErrorCatch class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ErrorCatch()
        self.assertIsInstance(instance, ErrorCatch)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ErrorCatch()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

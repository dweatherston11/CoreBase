# test_corebase.py
"""
Tests for CoreBase module.
"""

import unittest
from corebase import CoreBase

class TestCoreBase(unittest.TestCase):
    """Test cases for CoreBase class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CoreBase()
        self.assertIsInstance(instance, CoreBase)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CoreBase()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

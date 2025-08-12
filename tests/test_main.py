"""
Tests for the train-or-nah application.
"""

import unittest
from train_or_nah import __version__


class TestTrainOrNah(unittest.TestCase):
    """Test cases for train-or-nah."""
    
    def test_version(self):
        """Test that version is defined."""
        self.assertIsNotNone(__version__)
        
    def test_version_format(self):
        """Test that version follows semantic versioning."""
        parts = __version__.split('.')
        self.assertEqual(len(parts), 3)


if __name__ == "__main__":
    unittest.main()

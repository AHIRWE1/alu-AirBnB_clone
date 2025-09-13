#!/usr/bin/python3
"""
Unit tests for console.py
"""

import unittest
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO


class TestConsole(unittest.TestCase):
    """Test cases for HBNBCommand console."""

    def setUp(self):
        """Set up a console instance for tests."""
        self.console = HBNBCommand()

    def test_quit_command(self):
        """Test quit command returns True."""
        self.assertTrue(self.console.do_quit(""))

    def test_EOF_command(self):
        """Test EOF command returns True."""
        with patch("sys.stdout", new=StringIO()) as fake_out:
            result = self.console.do_EOF("")
            self.assertTrue(result)
            self.assertEqual(fake_out.getvalue(), "\n")

    def test_emptyline(self):
        """Test emptyline does nothing."""
        result = self.console.emptyline()
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
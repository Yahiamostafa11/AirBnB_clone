#!/usr/bin/python3
"""Unittest for the console.py file

Unittest classes:
    TestHBNBCommand
"""
import os
import sys
import unittest
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch


classes = {
    "BaseModel",
    "User",
    "State",
    "City",
    "Amenity",
    "Place",
    "Review",
}


class TestHBNBCommand(unittest.TestCase):
    """Unittest for the console.py file"""

    def setUp(self):
        """Set up the environment to test the console"""
        self.console = HBNBCommand()
        self.mock_stdin = StringIO()
        self.mock_stdout = StringIO()
        self.patcher = patch('sys.stdout', self.mock_stdout)
        self.patcher.start()
        self.addCleanup(self.patcher.stop)

    def tearDown(self):
        """Clean the environment after the test"""
        try:
            os.remove("file.json")

        except FileNotFoundError:
            pass

    def test_quit(self):
        """Test the quit command in and out of the console"""
        with patch('sys.stdin', StringIO('quit\n')) as mock_stdin:
            self.console.onecmd("quit")
            self.assertEqual(self.mock_stdout.getvalue(), "")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(self.console.onecmd("quit"))

    def test_EOF(self):
        """Test the EOF command in and out of the console"""
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertTrue(self.console.onecmd("EOF"))

    def test_create(self):
        """Test the create command in and out of the console"""
        with patch('sys.stdin', StringIO('create BaseModel\n')) as mock_stdin:
            self.console.onecmd("create BaseModel")
            self.assertEqual(self.mock_stdout.getvalue(), "")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(self.console.onecmd("create BaseModel"))

    def test_show(self):
        """Test the show command in and out of the console"""
        with patch('sys.stdin', StringIO('show BaseModel\n')) as mock_stdin:
            self.console.onecmd("show")
            self.assertEqual(self.mock_stdout.getvalue(),
                             "** class doesn't exist **\n")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(self.console.onecmd("show BaseModel"))
        with patch('sys.stdout', new=StringIO()) as output:
            self.console.onecmd("show BaseModel")
            self.assertTrue(output.getvalue().strip() ==
                            "** instance id missing **")
        with patch('sys.stdout', new=StringIO()) as output:
            self.console.onecmd("show BaseModel 1234-1234-1234")
            self.assertTrue(output.getvalue().strip() ==
                            "** no instance found **")

    def test_destroy(self):
        """Test the destroy command in and out of the console"""
        with patch('sys.stdin', StringIO('destroy BaseModel\n')) as mock_stdin:
            self.console.onecmd("destroy BaseModel")
            self.assertEqual(
                self.mock_stdout.getvalue(), "** class doesn't exist **\n")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(self.console.onecmd("destroy BaseModel"))
        with patch('sys.stdout', new=StringIO()) as output:
            self.console.onecmd("destroy BaseModel")
            self.assertTrue(output.getvalue().strip() ==
                            "** instance id missing **")
        with patch('sys.stdout', new=StringIO()) as output:
            self.console.onecmd("destroy BaseModel 1234-1234-1234")
            self.assertTrue(output.getvalue().strip() ==
                            "** no instance found **")

    def test_all(self):
        """Test the all command in and out of the console"""
        with patch('sys.stdin', StringIO('all BaseModel\n')) as mock_stdin:
            self.console.onecmd("all BaseModel")
            self.assertEqual(
                self.mock_stdout.getvalue(), "** class doesn't exist **\n")
        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("all BaseModel")
            self.assertTrue(self.console.onecmd
                            ("all BaseModel"))

    def test_emptyline(self):
        """Test the emptyline command"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(self.console.onecmd("") is None)

    def test_unknown_command(self):
        """Test an unknown command"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.console.onecmd("unknown"))

    def test_create_with_args(self):
        """Test the create command with arguments"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("create BaseModel name=\"Holberton\" age=89")
            self.assertTrue(len(output.getvalue()) > 0)

    def test_show_with_args(self):
        """Test the show command with arguments"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("show BaseModel 121212")
            self.assertEqual(output.getvalue(), "** no instance found **\n")


if __name__ == "__main__":
    unittest.main()

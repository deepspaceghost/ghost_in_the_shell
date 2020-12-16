#!/usr/bin/python3

import os
from puppet_master import puppet_master
import unittest


class TestPuppetMaster(unittest.TestCase):
    """
    """

    def test_create_file(self):
        """
        """

        print("Testing function...")
        puppet_master.create_file("test.txt", "test text")
        self.assertTrue(os.path.exists("test.txt"))
        os.remove("test.txt")

    def test_create_dir(self):
        """
        """

        print("Testing function...")
        puppet_master.create_dir("test")
        self.assertTrue(os.path.exists("test"))
        os.rmdir("test")

    def test_delete_file(self):
        """
        """

        print("Testing function...")
        puppet_master.create_file("test.txt", "test text")
        puppet_master.delete_file("test.txt")
        self.assertFalse(os.path.exists("test.txt"))

    def test_rename_file(self):
        """
        """

        print("Testing function...")
        puppet_master.create_file("test.txt", "test text")
        puppet_master.rename_file("test.txt", "test2.txt")
        self.assertTrue(os.path.exists("test2.txt"))
        os.remove("test2.txt")


if __name__ == "__main__":
    """
    """

    unittest.main()

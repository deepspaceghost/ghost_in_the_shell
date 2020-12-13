#!/usr/bin/python3

import unittest
import os
from puppet_master import puppet_master


class TestPuppetMaster(unittest.TestCase):
    """
    """

    def test_create_file(self):
        """
        """

        puppet_master.create_file("text.txt", "test text")
        self.assertTrue(os.path.exists("text.txt"))
        os.remove("text.txt")


if __name__ == "__main__":
    """
    """

    unittest.main()

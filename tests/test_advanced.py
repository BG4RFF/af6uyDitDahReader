# -*- coding: utf-8 -*-

import unittest

from .context import ditDahReader


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_translate(self):
        self.assertEqual(ditDahReader.morse.translate(
            "a book"), ".- -...:---:---:-.-")


if __name__ == '__main__':
    unittest.main()

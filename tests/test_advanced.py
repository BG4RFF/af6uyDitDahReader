# -*- coding: utf-8 -*-

import unittest

from .context import ditDahReader


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_translate(self):
        m = ditDahReader.Morse()
        self.assertEqual(m.translate("a book"), ".- -...:---:---:-.-")
        self.assertEqual(m.translate("AF6UY"), ".-:..-.:-....:..-:-.--")


if __name__ == '__main__':
    unittest.main()

# -*- coding: utf-8 -*-

import string
import unittest

from .context import ditDahReader


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_translate(self):
        """
          test translate for a few words
          TODO: should find some morse website that produces similar syntax
          to test against
        """
        m = ditDahReader.Morse()
        self.assertEqual(m.translate("a book"), ".- -...:---:---:-.-")
        self.assertEqual(m.translate("AF6UY"), ".-:..-.:-....:..-:-.--")
        self.assertEqual(m.translate("àðþ"), ".--.-:..-..:.--..")

    def test_morse_dict_uniq(self):
        """
          test to see if the morse dict English letters, numbers
          and punctuation are all unique morse code
        """
        m = ""
        for l in string.ascii_lowercase:
            m = m + ditDahReader.morse_dict[l]
        for l in string.digits:
            m = m + ditDahReader.morse_dict[l]
        for l in string.punctuation:
            for l in ditDahReader.morse_dict:
                m = m + ditDahReader.morse_dict[l]

        l_len = len(l)
        # set creates unique list
        self.assertEqual(len(set(l)), l_len)


if __name__ == '__main__':
    unittest.main()

﻿# -*- coding: utf-8-with-signature-unix; fill-column: 77 -*-
# -*- indent-tabs-mode: nil -*-

import sys
from twisted.trial.unittest import SkipTest, TestCase

from pyutil.jsonutil import encoder

CASES = [
    (u'/\\"\ucafe\ubabe\uab98\ufcde\ubcda\uef4a\x08\x0c\n\r\t`1~!@#$%^&*()_+-=[]{}|;:\',./<>?', '"/\\\\\\"\\ucafe\\ubabe\\uab98\\ufcde\\ubcda\\uef4a\\b\\f\\n\\r\\t`1~!@#$%^&*()_+-=[]{}|;:\',./<>?"'),
    (u'\u0123\u4567\u89ab\ucdef\uabcd\uef4a', '"\\u0123\\u4567\\u89ab\\ucdef\\uabcd\\uef4a"'),
    (u'controls', '"controls"'),
    (u'\x08\x0c\n\r\t', '"\\b\\f\\n\\r\\t"'),
    (u'{"object with 1 member":["array with 1 element"]}', '"{\\"object with 1 member\\":[\\"array with 1 element\\"]}"'),
    (u' s p a c e d ', '" s p a c e d "'),
    (u'\U0001d120', '"\\ud834\\udd20"'),
    (u'\u03b1\u03a9', '"\\u03b1\\u03a9"'),
    (b'\xce\xb1\xce\xa9', '"\\u03b1\\u03a9"'),
    (u'\u03b1\u03a9', '"\\u03b1\\u03a9"'),
    (b'\xce\xb1\xce\xa9', '"\\u03b1\\u03a9"'),
    (u'\u03b1\u03a9', '"\\u03b1\\u03a9"'),
    (u'\u03b1\u03a9', '"\\u03b1\\u03a9"'),
    (u"`1~!@#$%^&*()_+-={':[,]}|;.</>?", '"`1~!@#$%^&*()_+-={\':[,]}|;.</>?"'),
    (u'\x08\x0c\n\r\t', '"\\b\\f\\n\\r\\t"'),
    (u'\u0123\u4567\u89ab\ucdef\uabcd\uef4a', '"\\u0123\\u4567\\u89ab\\ucdef\\uabcd\\uef4a"'),
]

class TestEncodeBaseStringAscii(TestCase):
    def test_py_encode_basestring_ascii(self):
        self._test_encode_basestring_ascii(encoder.py_encode_basestring_ascii)

    def test_c_encode_basestring_ascii(self):
        if not encoder.c_encode_basestring_ascii:
            raise SkipTest("no C extension speedups available to test")
        self._test_encode_basestring_ascii(encoder.c_encode_basestring_ascii)

    def _test_encode_basestring_ascii(self, encode_basestring_ascii):
        for input_string, expect in CASES:
            result = encode_basestring_ascii(input_string)
            self.assertEqual(result, expect)

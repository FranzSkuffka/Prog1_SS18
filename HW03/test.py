from unittest.mock import patch
from unittest import TestCase
from unittest.mock import call
import unittest

from hw03 import main, main_2
print('testin')

class Test(TestCase):

    @patch('hw03._input', side_effect=['Jan', '3', 'y', '5', 'n'])
    @patch('hw03._print', create=True)
    def test_something(self, _input, _print):
        main()
        _input.assert_has_calls(
          [
            call('Hello Jan'),
            call('***'),
            call('*****'),
            call('Goodbye Jan')
          ]
        )

class AnotherTest(TestCase):

    @patch('hw03._input', side_effect=['TImiiiimy', '1000', 'y', 'nooooo moooore', 'n'])
    @patch('hw03._print', create=True)
    def test_something(self, _input, _print):
        main()
        _input.assert_has_calls(
          [
            call('Hello TImiiiimy'),
            call('*' * 1000),
            call('Sorry, I did not understand'),
            call('Goodbye TImiiiimy')
          ]
        )

class OtherProgramTest(TestCase):

    @patch('hw03._input', side_effect=['TImiiiimy', 'y', '1000', 'y', 'nooooo moooore', 'n'])
    @patch('hw03._print', create=True)
    def test_something(self, _input, _print):
        main_2()
        _input.assert_has_calls(
          [
            call('*' * 1000),
            call('Sorry, I did not understand'),
          ]
        )


if __name__ == '__main__':
    unittest.main()
    Mock()

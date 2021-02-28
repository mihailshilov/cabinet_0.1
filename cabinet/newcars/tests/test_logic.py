# from django.test import TestCase
from unittest import TestCase

from newcars.logic import operations


class LogicTestCase(TestCase):
    def test_plus(self):
        result = operations(6, 3, '+')
        self.assertEqual(9, result)
        # return True

    def test_minus(self):
        result = operations(6, 3, '-')
        self.assertEqual(3, result)

    def test_multiply(self):
        result = operations(6, 3, '*')
        self.assertEqual(18, result)

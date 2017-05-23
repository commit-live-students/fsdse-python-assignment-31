from unittest import TestCase


class TestSolution(TestCase):
    def test_solution(self):
        from build import solution
        d = {'one': ['a', 'b'], 'two': ['c', 'd']}
        result = solution(d)
        self.assertEqual(result, ['ac', 'ad', 'bc', 'bd'])

import unittest
from track_and_trace import routes


class TestCase(unittest.TestCase):
    def home(self):
        result = track_and_trace.home('a', 'b', 'c')
        self.assertEqual(result, 'abc')
        print(result)

    
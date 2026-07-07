import unittest


class TestCase:
    def __init__(self):
        self.test_count=12

    def __str__(self):
        return str(self.test_count)
t1= TestCase()
print(t1)
import unittest

def add(x, y):
    return x+y

class Test(unittest.TestCase):
    def testadd1(self):
        self.assertEqual(add(10, 7), 17)

if __name__ == "__main__":
    unittest.main()


import unittest
from cap import cap_text
# Kiểm tra xem python sau khi capitalize có như kỳ vọng không


class TestCap(unittest.TestCase):
    def test_one_word(self):
        text = 'python'
        result = cap_text(text)
        self.assertEqual(result, 'Python')

    def test_mutiply_word(self):
        text = 'monty python'
        result = cap_text(text)
        self.assertEqual(result, 'Monty Python')


if __name__ == '__main__':
    unittest.main()

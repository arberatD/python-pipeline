import unittest
from main import get_full_name

class TestFullName(unittest.TestCase):
    def test_get_full_name(self):
        expected_full_name = "Arberat Dushi"
        self.assertEqual(get_full_name(), expected_full_name)

if __name__ == '__main__':
    unittest.main()

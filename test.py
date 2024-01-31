import unittest
from unittest.mock import patch

class TestFullName(unittest.TestCase):
    @patch('builtins.input', side_effect=['Vorname', 'Nachname'])
    def test_get_full_name(self, input):
        self.assertEqual(get_full_name(), 'Vorname Nachname')

if __name__ == '__main__':
    unittest.main()
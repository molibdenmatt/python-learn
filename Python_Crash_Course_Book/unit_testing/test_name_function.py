import unittest
from name_function import get_formatted_name


class NameTestCase(unittest.TestCase):
    """Tests for the name_function.py script"""

    def test_first_last_name(self):
        """Is Janis Joplin correctly formatted?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_middle_last_name(self):
        """Is Wolfgang Amadeus Mozzart correctly formatted?"""
        formatted_name = get_formatted_name('wolfgang', 'mozzart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozzart')


if __name__ == '__main__':
    unittest.main()

import unittest
from phonebook import PhoneBook


class TestPhoneBook(unittest.TestCase):

    def setUp(self):
        self.phonebook = PhoneBook()

    def test_lookup_entry_by_name(self):
        self.phonebook.add('Person', '112233112233')
        self.assertEqual('112233112233', self.phonebook.lookup('Person'))

    def test_missing_entry_raises_KeyError(self):
        with self.assertRaises(KeyError):
            self.phonebook.lookup('Unknown Phone Number')

    def test_empty_phonebook_is_consistent(self):
        self.assertTrue(self.phonebook.is_consistent())

    def test_phonebook_with_normal_entries_are_consistent(self):
        self.phonebook.add('Bob', '12345')
        self.phonebook.add('Mary', '012345')
        self.assertTrue(self.phonebook.is_consistent())

    def test_phonebook_with_duplicate_entries_are_inconsistent(self):
        self.phonebook.add('Bob', '12345')
        self.phonebook.add('Mary', '12345')
        self.assertFalse(self.phonebook.is_consistent())

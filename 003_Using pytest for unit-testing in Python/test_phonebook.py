import pytest
from phonebook import PhoneBook


# Using fixtures in pytest
@pytest.fixture
def phonebook(tmpdir):
    phonebook = PhoneBook(tmpdir)
    return phonebook


# No need to import pytest!!
def test_add_and_lookup_entry(phonebook):
    # phonebook = PhoneBook()
    phonebook.add('Bob', '123')
    assert '123' == phonebook.lookup('Bob')


def test_phonebook_gives_access_to_names_and_numbers(phonebook):
    # phonebook = PhoneBook()
    phonebook.add('Alice', '12345')
    assert 'Alice' in phonebook.names()
    assert '12345' in phonebook.numbers()


# Using pytest method
def test_missing_entry_raises_keyerror(phonebook):
    # phonebook = PhoneBook()
    with pytest.raises(KeyError):
        phonebook.lookup('missing')

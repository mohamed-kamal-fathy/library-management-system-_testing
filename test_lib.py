import pytest
import tkinter as tk
from lib import LibraryManagementSystem



@pytest.fixture
def mock_master():
    return tk.Tk()


@pytest.fixture
def test_instance(mock_master):
    return LibraryManagementSystem(mock_master, "books.json")


@pytest.mark.add
def test_add_book(test_instance):
    test_instance.entry_add.insert(0, "Test Book")
    test_instance.add_book()
    assert "Test Book" in test_instance.books

@pytest.mark.skip
def test_2_add_book(test_instance):
    test_instance.entry_add.insert(0, "add Book")
    test_instance.add_book()
    assert "add Book" in test_instance.books


@pytest.mark.delete
def test_delete_book(test_instance):
    test_instance.entry_delete.insert(0, "deleted Book")
    test_instance.delete_book()
    assert "deleted Book" not in [book for book in test_instance.books]

@pytest.mark.xfail
def test_2_delete_book(test_instance):
    test_instance.entry_delete.insert(0, "deleted Book")
    test_instance.delete_book()
    assert "deleted Book" in [book for book in test_instance.books]


@pytest.mark.search
@pytest.mark.parametrize("search_term, expected_result", [("Test Book", True), ("Nonexistent Book", False)])
def test_search_book(test_instance, search_term, expected_result:bool):
    test_instance.entry_search.insert(0, search_term)
    search_results = test_instance.search_book()
    assert (search_term in search_results) == expected_result

# Measure code coverage 
@pytest.mark.coverage
def test_coverage():
    assert True


import pytest
from src.logic import WordProcessor

def test_initial_count():
    processor = WordProcessor()
    assert processor.get_count() == 0

def test_unique_addition():
    processor = WordProcessor()
    processor.add_text("apple banana apple")
    # Even though apple is there twice, count should be 2
    assert processor.get_count() == 2

def test_case_insensitivity():
    processor = WordProcessor()
    processor.add_text("Apple APPLE apple")
    assert processor.get_count() == 1

def test_punctuation_handling():
    processor = WordProcessor()
    processor.add_text("Hello, world! Hello...")
    assert processor.get_count() == 2
    assert "hello" in processor.unique_words
    assert "world" in processor.unique_words

def test_clear_functionality():
    processor = WordProcessor()
    processor.add_text("some words")
    processor.clear()
    assert processor.get_count() == 0
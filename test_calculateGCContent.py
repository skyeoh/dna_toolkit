import pytest
from dna_toolkit import calculateGCContent


def test_for_string_with_all_G():
    assert calculateGCContent("GGGGG") == 100

def test_for_string_with_all_C():
    assert calculateGCContent("CCC") == 100

def test_for_string_with_all_GC():
    assert calculateGCContent("GGCCCGCGCCG") == 100

def test_for_string_with_no_GC():
    assert calculateGCContent("ATTTAATATT") == 0

def test_for_arbitrary_string_1():
    assert calculateGCContent("CCTATTTATTAAGTTAATCTACAGGCAC") == 32 # exact value is 32.1428...

def test_for_arbitrary_string_2():
    assert calculateGCContent("CCTATTTACCAAGTTAAGCTACAGGCAC") == 43 # exact value is 42.8571...

def test_for_arbitrary_string_with_only_starting_index_specified():
    assert calculateGCContent("CCTATTTACCAAGTTAAGCTACAGGTAC", 12) == 44 # exact value is 43.75

def test_for_arbitrary_string_with_both_indices_specified_for_entire_string():
    assert calculateGCContent("CCTATTTACCAAGTTAAGCTACAGGTAC", 0, 28) == 39 # exact value is 39.2857...

def test_for_arbitrary_string_with_both_indices_specified_for_first_half():
    assert calculateGCContent("CCTATTTACCAAGTTAAGCTACAGGTAC", 0, 15) == 33 # exact value is 33.3333...

def test_for_arbitrary_string_with_both_indices_specified_for_second_half():
    assert calculateGCContent("CCTATTTACCAAGTTAAGCTACAGGTAC", 12, 28) == 44 # exact value is 43.75

def test_for_arbitrary_string_with_both_indices_specified():
    assert calculateGCContent("CCTATTTACCAAGTTAAGCTACAGGTAC", 9, 20) == 36 # exact value is 36.3636...

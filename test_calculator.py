import pytest
from calculator import mult


def test_mult_two_numbers():
    assert mult(2, 2) == 4

def test_mult_error():
    assert mult(3, 3) == 9
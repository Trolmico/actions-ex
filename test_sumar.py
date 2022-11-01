import pytest
from main import sumar
from main import restar

def test_sumar():
    assert sumar(2,3) == 5

def test_restar():
    assert sumar(3,2) == 1
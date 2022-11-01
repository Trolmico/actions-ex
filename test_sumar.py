import pytest
from main import sumar
from main import restar
from main import multiplicar

def test_sumar():
    assert sumar(2,3) == 6

def test_restar():
    assert restar(3,2) == 1

def test_multiplicar():
    assert multiplicar(2,2) == 4
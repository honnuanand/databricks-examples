"""Tests for mylib core functions"""
import pytest
from mylib import greet, add, multiply

def test_greet():
    """Test the greet function"""
    assert greet("Test") == "Hello, Test! Welcome to Databricks."
    assert greet("") == "Hello, ! Welcome to Databricks."

def test_add():
    """Test the add function"""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_multiply():
    """Test the multiply function"""
    assert multiply(2, 3) == 6
    assert multiply(-2, 3) == -6
    assert multiply(0, 5) == 0 
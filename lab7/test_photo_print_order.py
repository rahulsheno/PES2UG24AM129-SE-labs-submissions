"""
Lab 7: Fuzzing for Input Validation Bugs
File: test_photo_print_order.py
Author: Rahul Vivek Shenoy (PES2UG24AM129)
Target: photo_print_order.py

Property-based fuzz testing using Hypothesis to discover edge cases and crashes.
"""

from hypothesis import given, strategies as st
from photo_print_order import parse_order, file_size_average, payable_amount


@given(st.text() | st.none())
def test_parse_order_no_crash(s):
    """Fuzz test for parse_order: ensures function never crashes on arbitrary text or None."""
    try:
        parse_order(s)
    except Exception as e:
        assert False, f"parse_order crashed with: {e}"


@given(st.text() | st.none())
def test_file_size_average_no_crash(s):
    """Fuzz test for file_size_average: ensures function never crashes on arbitrary text or None."""
    try:
        file_size_average(s)
    except Exception as e:
        assert False, f"file_size_average crashed with: {e}"


@given(st.text() | st.none())
def test_payable_amount_no_crash(s):
    """Fuzz test for payable_amount: ensures function never crashes on arbitrary text or None."""
    try:
        payable_amount(s)
    except Exception as e:
        assert False, f"payable_amount crashed with: {e}"

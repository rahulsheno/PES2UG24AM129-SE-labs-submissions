"""
Lab 6: Code and Branch Coverage Analysis
File: test_photo_print_order.py
Author: Rahul Vivek Shenoy (PES2UG24AM129)
Target: photo_print_order.py

Comprehensive test suite achieving 100% Code Coverage and 100% Branch Coverage.
"""

import pytest
from photo_print_order import extra_print_charge, order_valid, dispatch_status


# ============================================================================
# Tests for extra_print_charge
# ============================================================================

def test_extra_print_charge_unknown_size():
    with pytest.raises(ValueError, match="unknown print size"):
        extra_print_charge("11x14", 10, "matte", False)


def test_extra_print_charge_negative_copies():
    with pytest.raises(ValueError, match="invalid copies"):
        extra_print_charge("4x6", -1, "matte", False)


def test_extra_print_charge_within_included():
    assert extra_print_charge("4x6", 20, "matte", False) == 0
    assert extra_print_charge("4x6", 15, "matte", False) == 0


def test_extra_print_charge_member_discount_non_8x10():
    assert extra_print_charge("4x6", 30, "matte", True) == 5 * 4


def test_extra_print_charge_member_8x10():
    assert extra_print_charge("8x10", 20, "matte", True) == 10 * 4


def test_extra_print_charge_non_member_glossy_small_extra():
    assert extra_print_charge("5x7", 25, "glossy", False) == 10 * 7


def test_extra_print_charge_extra_over_50_matte():
    assert extra_print_charge("4x6", 80, "matte", False) == 60 * 6


def test_extra_print_charge_extra_over_50_canvas():
    assert extra_print_charge("4x6", 80, "canvas", False) == 60 * 14


def test_extra_print_charge_extra_over_50_glossy():
    assert extra_print_charge("4x6", 80, "glossy", False) == 60 * 9


# ============================================================================
# Tests for order_valid
# ============================================================================

def test_order_valid_rush_true_valid():
    assert order_valid(10, 50, is_rush=True) is True


def test_order_valid_rush_true_invalid():
    assert order_valid(10, 51, is_rush=True) is False


def test_order_valid_non_rush_file_size_exceeded():
    assert order_valid(26, 100, is_rush=False) is False


def test_order_valid_non_rush_within_limit():
    assert order_valid(25, 500, is_rush=False) is True


def test_order_valid_non_rush_copies_exceeded():
    assert order_valid(20, 501, is_rush=False) is False


# ============================================================================
# Tests for dispatch_status
# ============================================================================

def test_dispatch_status_framed_international_on_time():
    assert dispatch_status(48, is_framed=True, is_international=True) == "on_time"


def test_dispatch_status_framed_international_tight():
    assert dispatch_status(42, is_framed=True, is_international=True) == "tight"


def test_dispatch_status_framed_international_missed():
    assert dispatch_status(41, is_framed=True, is_international=True) == "missed"


def test_dispatch_status_unframed_domestic_on_time():
    assert dispatch_status(12, is_framed=False, is_international=False) == "on_time"


def test_dispatch_status_unframed_domestic_tight():
    assert dispatch_status(6, is_framed=False, is_international=False) == "tight"


def test_dispatch_status_unframed_domestic_missed():
    assert dispatch_status(5, is_framed=False, is_international=False) == "missed"

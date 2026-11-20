"""
Lab 6: Code and Branch Coverage Analysis
Deliverable: BranchCoverageTest_photo_print_order.py
Author: Rahul Vivek Shenoy (PES2UG24AM129)
Target: photo_print_order.py

Test suite designed to achieve 100% Branch Coverage (evaluating every decision
and boolean predicate to both True and False).
"""

import pytest
from photo_print_order import extra_print_charge, order_valid, dispatch_status


# ============================================================================
# Tests for extra_print_charge (Branch Coverage)
# ============================================================================

def test_extra_print_charge_unknown_size():
    """Branch: print_size not in INCLUDED_PRINTS -> True."""
    with pytest.raises(ValueError, match="unknown print size"):
        extra_print_charge("11x14", 10, "matte", False)


def test_extra_print_charge_negative_copies():
    """Branch: copies < 0 -> True."""
    with pytest.raises(ValueError, match="invalid copies"):
        extra_print_charge("4x6", -1, "matte", False)


def test_extra_print_charge_within_included():
    """Branch: extra <= 0 -> True (exact boundary and strictly less)."""
    # 4x6 included = 20. copies = 20 -> extra = 0
    assert extra_print_charge("4x6", 20, "matte", False) == 0
    # 4x6 included = 20. copies = 15 -> extra = -5 < 0
    assert extra_print_charge("4x6", 15, "matte", False) == 0


def test_extra_print_charge_member_discount_non_8x10():
    """Branch: is_member True AND print_size != '8x10' -> True (included += 5)."""
    # 4x6 included = 20 + 5 = 25. copies = 30 -> extra = 5. matte -> rate 4
    assert extra_print_charge("4x6", 30, "matte", True) == 5 * 4


def test_extra_print_charge_member_8x10():
    """Branch: is_member True AND print_size == '8x10' -> False (no +5 bonus)."""
    # 8x10 included = 10 (not 15). copies = 20 -> extra = 10. matte -> rate 4
    assert extra_print_charge("8x10", 20, "matte", True) == 10 * 4


def test_extra_print_charge_non_member_glossy_small_extra():
    """Branch: is_member False, finish != 'matte' (glossy), extra <= 50."""
    # 5x7 included = 15. copies = 25 -> extra = 10. glossy rate = 7
    assert extra_print_charge("5x7", 25, "glossy", False) == 10 * 7


def test_extra_print_charge_extra_over_50_matte():
    """Branch: extra > 50 -> True, finish == 'matte' -> True, finish == 'canvas' -> False."""
    # 4x6 included = 20. copies = 80 -> extra = 60. rate = 4 + 2 = 6
    assert extra_print_charge("4x6", 80, "matte", False) == 60 * 6


def test_extra_print_charge_extra_over_50_canvas():
    """Branch: extra > 50 -> True, finish != 'matte' (rate 7), finish == 'canvas' -> True (rate + 5 = 14)."""
    # 4x6 included = 20. copies = 80 -> extra = 60. rate = 7 + 2 + 5 = 14
    assert extra_print_charge("4x6", 80, "canvas", False) == 60 * 14


def test_extra_print_charge_extra_over_50_glossy():
    """Branch: extra > 50 -> True, finish != 'matte' (rate 7), finish == 'canvas' -> False (rate 7 + 2 = 9)."""
    # 4x6 included = 20. copies = 80 -> extra = 60. rate = 7 + 2 = 9
    assert extra_print_charge("4x6", 80, "glossy", False) == 60 * 9


# ============================================================================
# Tests for order_valid (Branch Coverage)
# ============================================================================

def test_order_valid_rush_true_valid():
    """Branch: is_rush True -> copies <= 50 evaluates to True."""
    assert order_valid(10, 50, is_rush=True) is True


def test_order_valid_rush_true_invalid():
    """Branch: is_rush True -> copies <= 50 evaluates to False."""
    assert order_valid(10, 51, is_rush=True) is False


def test_order_valid_non_rush_file_size_exceeded():
    """Branch: is_rush False -> file_mb > 25 evaluates to True (returns False)."""
    assert order_valid(26, 100, is_rush=False) is False


def test_order_valid_non_rush_within_limit():
    """Branch: is_rush False -> file_mb <= 25 -> copies <= 500 evaluates to True."""
    assert order_valid(25, 500, is_rush=False) is True


def test_order_valid_non_rush_copies_exceeded():
    """Branch: is_rush False -> file_mb <= 25 -> copies <= 500 evaluates to False."""
    assert order_valid(20, 501, is_rush=False) is False


# ============================================================================
# Tests for dispatch_status (Branch Coverage)
# ============================================================================

def test_dispatch_status_framed_international_on_time():
    """Branch: is_framed True (24), is_international True (+24=48), hours >= cutoff (True)."""
    assert dispatch_status(48, is_framed=True, is_international=True) == "on_time"


def test_dispatch_status_framed_international_tight():
    """Branch: is_framed True, is_international True (cutoff 48), hours < cutoff but >= cutoff - 6 (True)."""
    assert dispatch_status(42, is_framed=True, is_international=True) == "tight"


def test_dispatch_status_framed_international_missed():
    """Branch: is_framed True, is_international True (cutoff 48), hours < cutoff - 6 (False)."""
    assert dispatch_status(41, is_framed=True, is_international=True) == "missed"


def test_dispatch_status_unframed_domestic_on_time():
    """Branch: is_framed False (12), is_international False (+0=12), hours >= cutoff (True)."""
    assert dispatch_status(12, is_framed=False, is_international=False) == "on_time"


def test_dispatch_status_unframed_domestic_tight():
    """Branch: is_framed False, is_international False (cutoff 12), hours >= 6 (True)."""
    assert dispatch_status(6, is_framed=False, is_international=False) == "tight"


def test_dispatch_status_unframed_domestic_missed():
    """Branch: is_framed False, is_international False (cutoff 12), hours < 6 (False)."""
    assert dispatch_status(5, is_framed=False, is_international=False) == "missed"

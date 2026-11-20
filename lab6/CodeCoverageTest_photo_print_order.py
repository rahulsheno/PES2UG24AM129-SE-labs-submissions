"""
Lab 6: Code and Branch Coverage Analysis
Deliverable: CodeCoverageTest_photo_print_order.py
Author: Rahul Vivek Shenoy (PES2UG24AM129)
Target: photo_print_order.py

Test suite designed to achieve 100% Statement/Line Coverage (>90% requirement).
"""

import pytest
from photo_print_order import extra_print_charge, order_valid, dispatch_status


# ============================================================================
# Tests for extra_print_charge (Statement Coverage)
# ============================================================================

def test_extra_print_charge_unknown_size():
    """Covers lines 5-6: print_size not in INCLUDED_PRINTS exception."""
    with pytest.raises(ValueError, match="unknown print size"):
        extra_print_charge("11x14", 10, "matte", False)


def test_extra_print_charge_negative_copies():
    """Covers lines 7-8: copies < 0 exception."""
    with pytest.raises(ValueError, match="invalid copies"):
        extra_print_charge("4x6", -5, "matte", False)


def test_extra_print_charge_member_within_included():
    """Covers lines 9-14: member bonus (+5) and extra <= 0 returning 0."""
    # 4x6 included is 20 + 5 (member) = 25. Copies = 15 -> extra = -10 <= 0
    assert extra_print_charge("4x6", 15, "matte", True) == 0


def test_extra_print_charge_matte_standard():
    """Covers lines 15-16, 23: finish == 'matte' rate = 4 with extra <= 50."""
    # 4x6 included is 20. Copies = 30 -> extra = 10. rate = 4
    assert extra_print_charge("4x6", 30, "matte", False) == 10 * 4


def test_extra_print_charge_canvas_large_order():
    """Covers lines 17-23: finish != 'matte' (rate=7), extra > 50 (+2), finish == 'canvas' (+5)."""
    # 4x6 included is 20. Copies = 100 -> extra = 80 (>50). rate = 7 + 2 + 5 = 14
    assert extra_print_charge("4x6", 100, "canvas", False) == 80 * 14


# ============================================================================
# Tests for order_valid (Statement Coverage)
# ============================================================================

def test_order_valid_rush_allowed():
    """Covers lines 27-28: is_rush is True, copies <= 50."""
    assert order_valid(10, 30, is_rush=True) is True


def test_order_invalid_file_oversized():
    """Covers lines 29-30: is_rush is False, file_mb > 25 returning False."""
    assert order_valid(30, 10, is_rush=False) is False


def test_order_valid_standard_within_limits():
    """Covers line 31: is_rush is False, file_mb <= 25, copies <= 500 returning True."""
    assert order_valid(10, 100, is_rush=False) is True


# ============================================================================
# Tests for dispatch_status (Statement Coverage)
# ============================================================================

def test_dispatch_status_framed_international_on_time():
    """Covers lines 35-36, 39-42: framed (cutoff=24), international (+24=48), on_time."""
    assert dispatch_status(50, is_framed=True, is_international=True) == "on_time"


def test_dispatch_status_unframed_domestic_tight():
    """Covers lines 37-38, 43-44: unframed (cutoff=12), domestic (+0=12), tight (>=6)."""
    assert dispatch_status(10, is_framed=False, is_international=False) == "tight"


def test_dispatch_status_unframed_domestic_missed():
    """Covers line 45: hours < cutoff - 6 returning 'missed'."""
    assert dispatch_status(2, is_framed=False, is_international=False) == "missed"

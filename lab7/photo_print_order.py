"""
Lab 7: Fuzzing for Input Validation Bugs
File: photo_print_order.py (Fixed & Hardened)
Author: Rahul Vivek Shenoy (PES2UG24AM129)

Hardened functions resistant to malformed, unexpected, or malicious fuzz inputs.
"""

import math


def parse_order(text):
    """
    Parses print size and copies from input string formatted as 'size:copies'.
    
    Hardened against:
    - Non-string / None inputs
    - Missing or multiple ':' delimiters
    - Non-digit / negative copy numbers
    - Empty strings or whitespace
    Returns (size, copies) tuple or None if invalid.
    """
    if not isinstance(text, str):
        return None
    parts = text.split(':')
    if len(parts) != 2:
        return None
    size = parts[0].strip().upper()
    copies_str = parts[1].strip()
    if not size or not copies_str.isdigit():
        return None
    try:
        copies = int(copies_str)
        if copies < 0:
            return None
        return size, copies
    except (ValueError, TypeError):
        return None


def file_size_average(sizes_csv):
    """
    Computes average file size in MB from a CSV string of numbers.
    
    Hardened against:
    - Non-string / None inputs
    - Empty strings / whitespace / empty tokens (e.g. '1,,3')
    - Non-numeric tokens
    - Division by zero on empty input
    Returns integer average, or 0 if input is invalid/empty.
    """
    if not isinstance(sizes_csv, str) or not sizes_csv.strip():
        return 0
    try:
        values = []
        for r in sizes_csv.split(','):
            r_clean = r.strip()
            if not r_clean:
                continue
            val = int(r_clean)
            if val >= 0:
                values.append(val)
        if not values:
            return 0
        return sum(values) // len(values)
    except (ValueError, TypeError, ZeroDivisionError):
        return 0


def payable_amount(text):
    """
    Calculates payable amount with 18% GST and discount from 'amount|discount'.
    
    Hardened against:
    - Non-string / None inputs
    - Missing or multiple '|' delimiters
    - Non-float / NaN / Infinity values
    - Negative amounts or discounts
    - Numeric overflows
    Returns final rounded non-negative payable float, or 0.0 if invalid.
    """
    if not isinstance(text, str):
        return 0.0
    parts = text.split('|')
    if len(parts) != 2:
        return 0.0
    try:
        amount_str = parts[0].strip()
        discount_str = parts[1].strip()
        amount = float(amount_str)
        discount = float(discount_str)
        if math.isnan(amount) or math.isinf(amount) or math.isnan(discount) or math.isinf(discount):
            return 0.0
        if amount < 0 or discount < 0:
            return 0.0
        total = amount * 1.18 - discount
        return max(round(total, 2), 0.0)
    except (ValueError, TypeError, OverflowError):
        return 0.0


def main():
    print("==== Running parse_order ====")
    user_input = input("Enter print size:copies (e.g. 4x6:25): ")
    result = parse_order(user_input)
    print("Size and Copies:", result)

    print("\n==== Running file_size_average ====")
    user_input = input("Enter file sizes in MB as CSV (e.g. 4,8,12): ")
    result = file_size_average(user_input)
    print("Average File Size:", result)

    print("\n==== Running payable_amount ====")
    user_input = input("Enter amount|discount (e.g. 450|50): ")
    result = payable_amount(user_input)
    print("Payable Amount:", result)


if __name__ == "__main__":
    main()

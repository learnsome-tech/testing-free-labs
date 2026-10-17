def total(lines):
    """Total of (price in pence, count) lines, less a launch discount."""
    subtotal = sum(price * count for price, count in lines)
    return subtotal - 100

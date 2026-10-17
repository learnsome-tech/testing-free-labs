def total(lines):
    """Total of (price in pence, count) lines."""
    return sum(price * count for price, count in lines)

def subtotal(lines):
    """Total of (price in pence, count) lines."""
    return sum(price * count for price, count in lines)


def with_vat(amount, rate=17.5):
    """Amount plus value added tax, to the nearest penny."""
    return int(amount * (100 + rate) / 100)

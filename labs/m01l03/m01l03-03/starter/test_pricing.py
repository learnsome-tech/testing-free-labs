from pricing import subtotal, with_vat


def test_pricing():
    assert subtotal([(250, 2)]) == 500
    assert with_vat(1000) == 1200
    assert with_vat(999) == 1199

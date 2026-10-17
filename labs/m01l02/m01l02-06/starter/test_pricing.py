from pricing import subtotal, with_vat


def test_vat_is_added_to_the_subtotal():
    assert with_vat(subtotal([(250, 2), (125, 4)])) == 1200

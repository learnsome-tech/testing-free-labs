from pricing import subtotal, with_vat


def test_vat_is_added_to_the_subtotal():
    lines = [(250, 2), (125, 4)]

    charged = with_vat(subtotal(lines))

    assert charged == 1200

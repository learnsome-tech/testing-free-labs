from pricing import quote


def test_quote_reports_the_whole_calculation():
    q = quote([(250, 2), (125, 4)])

    assert q["subtotal"] == 1000
    assert q["vat"] == 175
    assert q["total"] == 1175

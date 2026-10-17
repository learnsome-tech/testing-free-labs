import time

import pytest

from pricing import subtotal, with_vat


def test_vat_rounds_to_the_penny():
    assert with_vat(999) == 1199


@pytest.mark.slow
def test_the_price_service_answers():
    time.sleep(0.35)
    assert with_vat(subtotal([(100, 1)])) == 120

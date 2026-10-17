from cart import total


def test_two_lines_add_up():
    assert total([(250, 2), (125, 4)]) == 1000

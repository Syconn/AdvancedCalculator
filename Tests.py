from bakery import assert_equal
from Calculator import calculate


if __name__ == "__main__":
    assert_equal(calculate("2 + 2"), "4")
    assert_equal(calculate("2 * 3"), "6")
    assert_equal(calculate("5 - 4"), "1")
    assert_equal(calculate("5 / 4"), "1.25")

    assert_equal(calculate("2 + 2 + 4"), "8")
    assert_equal(calculate("2 * 3 + 2"), "8")
    assert_equal(calculate("5 - 4 * 2"), "-3")
    assert_equal(calculate("5 / 4 - 2"), "-0.75")
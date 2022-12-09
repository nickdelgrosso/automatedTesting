from titanic_utils import is_adult


def test_16_is_not_adult():
    assert not is_adult(16)


def test_19_is_adult():
    assert is_adult(19)

    
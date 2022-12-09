import sys
sys.path.append("./")

from titanic_utils import utils


def test_is_adult():
    assert utils.is_adult(11) == False
    assert utils.is_adult(20) == True
    assert utils.is_adult(18) == True
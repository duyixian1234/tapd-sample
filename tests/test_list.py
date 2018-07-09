import sys

sys.path.append('../')

from pipsource import sources


def test_list_not_empty():
    assert sources


def test_list_have_pypi():
    assert 'Pypi' in sources
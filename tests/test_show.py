import sys

sys.path.append('../')

from pipsource.show import current

def test_show_all():
    output = current()
    assert output
import sys, os

sys.path.insert(0, os.path.abspath('.'))

import skeleton.a

def test_a():
    assert skeleton.a.f(1) == 1

import pytest
from main import fcnmath, tow_ok

def test_fcnmath():
    x1, x2, y1, y2 = 0, 1, 0, 1
    x_v = 1
    y_v = 1
    ny_v1 = 0.7071067811865475
    d1 = 1.4142135623730951
    a1 = 0.7853981633974483
    nx_v1 = 0.7071067811865475
    nx_v, ny_v, d, a = fcnmath(x1, x2, y1, y2)
    assert nx_v1 == nx_v and ny_v1 == ny_v and d1 == d and a1 == a
    "Should be 0.7071067811865475, 1.4142135623730951, 0.7853981633974483, 0.7071067811865475"


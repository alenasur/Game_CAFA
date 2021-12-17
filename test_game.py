import math
import random

import pygame.mouse
import pytest
from pygame import mouse
from main import fcnmath, tow_ok, towers


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


def test_fcnmath_eg():
    x1, x2, y1, y2 = 1, 5, 2, 5
    x_v = 4
    y_v = 3
    ny_v1 = 0.6
    d1 = 5
    a1 = 0.6435011087932844
    nx_v1 = 0.8
    nx_v, ny_v, d, a = fcnmath(x1, x2, y1, y2)
    assert nx_v1 == nx_v and ny_v1 == ny_v and d1 == d and a1 == a
    "Should be 0.8, 0.6, 5, 0.6435011087932844"


def test_fcnmath_sanya():
    x1, x2, y1, y2 = 5, 10, 3, 6
    x_v = 5
    y_v = 3
    d1 = 5.8309518948453
    nx_v1 = 0.8574929257125443
    ny_v1 = 0.5144957554275266
    a1 = 0.5404195002705842
    nx_v, ny_v, d, a = fcnmath(x1, x2, y1, y2)
    assert nx_v1 == nx_v and ny_v1 == ny_v and d1 == d and a1 == a
    "Should be 0.8574929257125443, 0.5144957554275266, 5.8309518948453, 0.5404195002705842"


def test_fcnmath_12():
    x1, x2, y1, y2 = 22, 10, 16, 11
    x_v = -12
    y_v = -5
    d1 = 13
    nx_v1 = -0.9230769230769231
    ny_v1 = -0.38461538461538464
    a1 = -2.746801533890032
    nx_v, ny_v, d, a = fcnmath(x1, x2, y1, y2)
    assert nx_v1 == nx_v and ny_v1 == ny_v and d1 == d and a1 == a
    "Should be 0.9230769230769231, 0.38461538461538464, 13, 0.3947911196997615"


x = 15
y = 45


def test_tow_ok1(x, y):
    x += 30 / 2
    y += 30 / 2
    for t in towers:
        if t.x == x and t.y == y:
            b = False
    a = tow_ok(x, y)
    assert a == b



mp = pygame.mouse.get_pos()


def test_tow_ok(x, y):
    x = math.floor(mp[0] / 30) * 30 + 15
    y = math.floor(mp[0] / 30) * 30 + 15
    x1, y1 = 15, 45
    xxx = tow_ok(x1, y1)
    assert xxx == True


def test_tow_ok():
    x, y = 15, 45
    assert tow_ok(x, y) == True

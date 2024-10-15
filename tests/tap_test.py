from typing import Any

import pytest

from src.higher_order_tap_proxy import HigherOrderTapProxy
from src.tap import tap
from tests.artifacts.sample_object import SampleObject


def test_tap_with_callback() -> None:
    def callback(obj) -> None:
        obj.value += 10

    obj = SampleObject()
    result = tap(obj, callback)

    assert result is obj
    assert obj.value == 10


def test_tap_without_callback() -> None:
    obj = SampleObject()
    result = tap(obj)

    assert isinstance(result, HigherOrderTapProxy)
    assert result.target is obj


def test_tap_chaining() -> None:
    obj = SampleObject()
    result = tap(obj).increment().double().add(3)

    assert result.target is obj
    assert obj.value == 5


def test_tap_with_different_object_types() -> None:
    lst: list[int] = [1, 2, 3]

    tap(lst).append(4).reverse()

    assert lst == [4, 3, 2, 1]

    d: dict[str, int] = {"a": 1}

    tap(d).update({"b": 2})

    assert d == {"a": 1, "b": 2}


def test_nested_tap() -> None:
    obj = SampleObject()
    result = tap(tap(obj).increment()).double()

    assert result.value == 2


def test_tap_with_lambda() -> None:
    obj = SampleObject()
    result = tap(obj, lambda x: x.increment().double())

    assert obj.value == 2
    assert result is obj


def test_error_handling() -> None:
    obj = SampleObject()

    with pytest.raises(AttributeError):
        tap(obj).non_existent_method()


def test_tap_property_access() -> None:
    obj = SampleObject()
    obj.value = 10

    result = tap(obj).value

    assert result == 10


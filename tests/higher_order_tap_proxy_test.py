from higher_order_tap_proxy import HigherOrderTapProxy
from tests.artifacts.sample_object import SampleObject


def test_higher_order_tap_proxy() -> None:
    obj = SampleObject()
    proxy = HigherOrderTapProxy(obj)

    result = proxy.increment().double().add(3)

    assert isinstance(result, HigherOrderTapProxy)
    assert obj.value == 5
    assert proxy.target.value == 5

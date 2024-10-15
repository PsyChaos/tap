from typing import Any

from src.higher_order_tap_proxy import HigherOrderTapProxy


def tap(value, callback=None) -> HigherOrderTapProxy | Any:
    """
    Tap into a value, optionally performing a callback on it, and return the value or a proxy object.

    This function allows you to pass a value through a callback for inspection or modification
    without interrupting the value's flow in a method chain. If no callback is provided, it
    returns a proxy object that allows dynamic method calls on the value.

    Args:
        value: The value to be passed through or tapped into.
        callback: An optional callable function that takes the value as an argument. If provided,
                     the callback will be invoked with the value.
    Returns:
        The original value if a callback is provided. Otherwise, a `HigherOrderTapProxy`
        object for chaining dynamic method calls.
    """
    if callback is None:
        return HigherOrderTapProxy(value)

    callback(value)

    return value

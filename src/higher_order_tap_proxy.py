from typing import Callable, Self


class HigherOrderTapProxy:
    def __init__(self, target) -> None:
        """
        Create a new tap proxy instance.

        Args:
            target: The target being tapped.
        """
        self.target = target

    def __getattr__(self, attr) -> Callable[..., Self]:
        """
        Dynamically pass method calls to the target.

        Args:
            attr: The attribute name being accessed.
        Returns:
            A callable that will invoke the method on the target and return self, or the attribute itself if it is not callable.
        """

        target_attr = getattr(self.target, attr)
        
        if callable(target_attr):
            def wrapper(*args, **kwargs):
                target_attr(*args, **kwargs)
                return self
            return wrapper
        else:
            return target_attr

    def __repr__(self) -> str:
        return f"HigherOrderTapProxy({self.target})"

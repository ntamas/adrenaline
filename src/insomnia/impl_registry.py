import platform
from contextlib import contextmanager
from typing import Dict, Iterator, Optional

from .types import Insomnia, InsomniaContext

__all__ = ("get_implementation",)


_implementations = {}  # type: Dict[str, Insomnia]


def get_implementation(name: Optional[str] = None) -> Insomnia:
    if name is None:
        name = platform.system()

    name = name.lower()
    impl = _implementations.get(name)
    if impl is None:
        _implementations[name] = impl = import_implementation(name)

    return impl


def import_implementation(name: str) -> Insomnia:
    if name == "darwin":
        from ._impl.darwin import _enter, _exit, _verify
    elif name == "windows":
        from ._impl.windows import _enter, _exit, _verify
    elif name == "dummy":
        from ._impl.dummy import _enter, _exit, _verify
    elif name == "failing":
        from ._impl.failing import _enter, _exit, _verify
    else:
        raise NotImplementedError(f"No such implementation: {name!r}")

    class _InsomniaImpl(Insomnia):
        @contextmanager
        def enter(
            self, *, display: bool = False, reason: Optional[str] = None
        ) -> Iterator[None]:
            try:
                _enter(display=display, reason=reason or "Python insomnia module")
                yield
            finally:
                _exit()

        def verify(self) -> bool:
            return _verify()

    return _InsomniaImpl()

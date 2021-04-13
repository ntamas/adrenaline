import platform
from contextlib import contextmanager

from .impl_registry import get_implementation

__all__ = ("insomnia", "is_insomniac")

_impl = get_implementation()

insomnia = _impl.enter
is_insomniac = _impl.verify

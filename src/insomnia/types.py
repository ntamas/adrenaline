from typing import ContextManager

try:
    from typing import Protocol
except ImportError:
    from typing_extensions import Protocol


__all__ = ("Insomnia", "InsomniaContext")


#: Type specification for a context that suppresses sleep when entered and restores
#: the previous state when exited
InsomniaContext = ContextManager[None]


class Insomnia(Protocol):
    def enter(self, *, display: bool, reason: str) -> InsomniaContext:
        pass

    def verify(self) -> bool:
        pass

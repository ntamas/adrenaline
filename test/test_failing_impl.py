from pytest import raises

from insomnia import get_implementation


def test_failing_implementation_fails_as_expected():
    insomnia = get_implementation("failing")
    with raises(NotImplementedError):
        with insomnia.enter():
            pass


def test_failing_implementation_returns_false_when_verified():
    insomnia = get_implementation("failing")
    assert not insomnia.verify()

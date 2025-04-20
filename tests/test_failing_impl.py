from pytest import raises

from adrenaline import get_implementation


def test_failing_implementation_fails_as_expected():
    adrenaline = get_implementation("failing")
    with raises(NotImplementedError):
        with adrenaline.prevent_sleep():
            pass


def test_failing_implementation_returns_false_when_verified():
    adrenaline = get_implementation("failing")
    assert not adrenaline.is_sleep_prevented()

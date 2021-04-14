from adrenaline import is_sleep_prevented, prevent_sleep


def test_context_manager_works():
    assert not is_sleep_prevented()

    with prevent_sleep():
        assert is_sleep_prevented()

    assert not is_sleep_prevented()


def test_context_manager_works_with_exceptions():
    assert not is_sleep_prevented()

    try:
        with prevent_sleep():
            assert is_sleep_prevented()
            raise ValueError("test")

    except ValueError:
        assert not is_sleep_prevented()

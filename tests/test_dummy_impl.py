from adrenaline import get_implementation


def test_dummy_implementation_works():
    adrenaline = get_implementation("dummy")

    assert not adrenaline.is_sleep_prevented()

    with adrenaline.prevent_sleep():
        assert adrenaline.is_sleep_prevented()

    assert not adrenaline.is_sleep_prevented()

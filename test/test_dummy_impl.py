from insomnia import get_implementation


def test_dummy_implementation_works():
    insomnia = get_implementation("dummy")

    assert not insomnia.verify()

    with insomnia.enter():
        assert insomnia.verify()

    assert not insomnia.verify()

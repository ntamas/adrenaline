from insomnia import insomnia, is_insomniac


def test_context_manager_works():
    assert not is_insomniac()

    with insomnia():
        assert is_insomniac()

    assert not is_insomniac()

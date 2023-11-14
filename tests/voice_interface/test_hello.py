import pytest

from drawing2story_ui.voice_interface.hello import hello


def test_create_database_with_user():
    hello_result = hello()
    assert hello_result is not None
    assert hello_result.startswith("Hello!")

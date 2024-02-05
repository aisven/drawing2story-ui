import pytest

from drawing2story_ui.voice_interface.tts_with_pyttsx3 import say_text_with_pyttsx3
from drawing2story_ui.voice_interface.tts_with_pyttsx3 import try_anna_with_pyttsx3
from drawing2story_ui.voice_interface.tts_with_pyttsx3 import try_all_available_voices_with_pyttsx3

# Windows
# global_driver_name = "sapi5"
# macOS
global_driver_name = "nsss"
# Ubuntu
# global_driver_name = "espeak"


def test_say_text_with_pyttsx3_on_macos():
    text = "I'll be back."
    say_text_with_pyttsx3(text=text, driver_name=global_driver_name, debug=True)


@pytest.mark.skip("skipped test")
def test_try_anna_with_pyttsx3_on_macos():
    try_anna_with_pyttsx3(driver_name=global_driver_name, debug=True)


@pytest.mark.skip("another skipped test")
def test_try_all_available_voices_with_pyttsx3_on_macos():
    try_all_available_voices_with_pyttsx3(driver_name=global_driver_name, debug=True)

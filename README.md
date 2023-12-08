# drawing2story-ui

This project is a user interface to the tool drawind2story.

# Hoan's notes
STT (Speech to text)
I used Speech Recognition library with real time recording.
Challenges:
1. A recording duration needs to be set (e.g 5s). User can only talk for 5s
-> Can be improve with Voice Activity Detection (either with AI or not)

Currently looking up this library:
1. WhisperX (https://github.com/m-bain/whisperX)

TTS (Text to speech)
Currently testing:
1. Tortoise TTS (https://github.com/neonbjb/tortoise-tts)
Testing on Colab: https://colab.research.google.com/github/neonbjb/tortoise-tts/blob/main/tortoise_tts.ipynb#scrollTo=Gen09NM4hONQ

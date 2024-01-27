import pyttsx3
import logging


def say_text_with_pyttsx3(text: str, driver_name: str, debug: bool):

    # pyttsx3 is these days also known as py3-tts
    # https://pypi.org/project/py3-tts/
    # https://py3-tts.vigneshrao.com/support/

    # pyttsx3 delegates to speech synthesis engines of the operating systems
    # SAPI5 on Windows XP and Windows Vista and Windows 8,8.1 , 10
    # NSSpeechSynthesizer on Mac OS X 10.5 (Leopard) and 10.6 (Snow Leopard)
    # espeak on Ubuntu Desktop Edition 8.10 (Intrepid), 9.04 (Jaunty), and 9.10 (Karmic)

    # it works offline i.e. it does not require any connection to some API

    engine = pyttsx3.init(driverName=driver_name, debug=debug)
    engine.say(text)
    engine.runAndWait()


def try_anna_with_pyttsx3(driver_name: str, debug: bool):
    logger = logging.getLogger("ourlog")
    logger.setLevel(logging.INFO)

    engine = pyttsx3.init(driverName=driver_name, debug=debug)

    # first let's reduce the rate
    rate = engine.getProperty('rate')
    logger.info(f"rate={rate}")
    new_rate = rate * 0.8
    logger.info(f"new_rate={new_rate}")
    engine.setProperty('rate', new_rate)

    # second let's reduce the volume
    volume = engine.getProperty('volume')
    logger.info(f"volume={volume}")
    new_volume = volume * 0.9
    logger.info(f"new_volume={new_volume}")
    engine.setProperty('volume', new_volume)

    voices = engine.getProperty('voices')
    done = False
    for voice in voices:
        if voice.id == "com.apple.voice.compact.de-DE.Anna":
            logger.info(f"-----")
            logger.info(f"voice={voice}")
            engine.setProperty('voice', voice.id)
            engine.say('Hallo! Ich bin Dein Computer. Wie geht es Dir? Ich hoffe, Du hast einen schönen Tag? Grüße gehen raus an den Professor und alle Kursteilnehmer!')
            #engine.save_to_file('Hallo! Ich bin Dein Computer. Wie geht es Dir? Ich hoffe, Du hast einen schönen Tag? Grüße gehen raus an den Professor und alle Kursteilnehmer!', '/Users/sven/gh/drawing2story-ui/Anna_Hallo_Kurs.mp3')
            engine.runAndWait()
            done = True
            break
        if done:
            break


def try_all_available_voices_with_pyttsx3(driver_name: str, debug: bool):
    logger = logging.getLogger("ourlog")
    logger.setLevel(logging.INFO)

    engine = pyttsx3.init(driverName=driver_name, debug=debug)

    # first let's reduce the rate
    rate = engine.getProperty('rate')
    logger.info(f"rate={rate}")
    new_rate = rate * 0.8
    logger.info(f"new_rate={new_rate}")
    engine.setProperty('rate', new_rate)

    # second let's reduce the volume
    volume = engine.getProperty('volume')
    logger.info(f"volume={volume}")
    new_volume = volume * 0.9
    logger.info(f"new_volume={new_volume}")
    engine.setProperty('volume', new_volume)

    voices = engine.getProperty('voices')
    for voice in voices:
        logger.info(f"-----")
        logger.info(f"voice={voice}")
        engine.setProperty('voice', voice.id)
        engine.say('Hello. I am your computer. Have a nice day.')
        engine.runAndWait()

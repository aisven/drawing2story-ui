from drawing2story_ui.voice_interface.sentiment_analysis_with_heuristic import SentimentEnum
from drawing2story_ui.voice_interface.sentiment_analysis_with_heuristic import analyze_sentiment_with_heuristic


def sentiment_test_case(text: str, score_expected: float, score_0_1_expected: float, label_expected: SentimentEnum):
    score, score_0_1, label, scores = analyze_sentiment_with_heuristic(text)
    label_4_print = label
    if label == "neutral":
        label_4_print = "neutral "
    print(
        f"{score:+.4f}\t\t{score_0_1:.2f}\t{label_4_print}"
        f"\t{scores['neg']:.2f}\t{scores['neu']:.2f}\t{scores['pos']:.2f}\t{text}"
    )
    assert score == score_expected
    assert score_0_1 == score_0_1_expected
    assert label == label_expected.value


def test_analyze_sentiment_positive():
    print(" ")
    print("score\t\tp\t\tlabel\t\t -\t\t |\t\t +\t\ttext")
    sentiment_test_case("No, yes.", 0.4019, 0.70095, SentimentEnum.positive)
    sentiment_test_case("Uhm, yes.", 0.4019, 0.70095, SentimentEnum.positive)
    sentiment_test_case("Oh, yes.", 0.4019, 0.70095, SentimentEnum.positive)
    sentiment_test_case("Oh uhm, yes.", 0.4019, 0.70095, SentimentEnum.positive)
    sentiment_test_case("Ya, oh, uhm, yes.", 0.4019, 0.70095, SentimentEnum.positive)
    sentiment_test_case("Yes.", 0.4019, 0.70095, SentimentEnum.positive)
    sentiment_test_case("Yes, it is a fox.", 0.4019, 0.70095, SentimentEnum.positive)
    sentiment_test_case("Yes, the animal in my drawing is a fox.", 0.4019, 0.70095, SentimentEnum.positive)
    sentiment_test_case("True.", 0.4215, 0.71075, SentimentEnum.positive)
    sentiment_test_case("Yes!", 0.4574, 0.7287, SentimentEnum.positive)
    sentiment_test_case("True!", 0.4753, 0.73765, SentimentEnum.positive)
    sentiment_test_case("Very true.", 0.4754, 0.7377, SentimentEnum.positive)
    sentiment_test_case("Very true!", 0.5244, 0.7622, SentimentEnum.positive)
    sentiment_test_case("Yes. Yes.", 0.6597, 0.82985, SentimentEnum.positive)
    sentiment_test_case("True. Yes.", 0.6705, 0.83525, SentimentEnum.positive)
    sentiment_test_case("Yes, this is true.", 0.6705, 0.83525, SentimentEnum.positive)
    sentiment_test_case("True. True.", 0.6808, 0.8404, SentimentEnum.positive)
    sentiment_test_case("Yes, yes!", 0.69, 0.845, SentimentEnum.positive)
    sentiment_test_case("Yes! Yes.", 0.69, 0.845, SentimentEnum.positive)
    sentiment_test_case("Yes! Yes!", 0.717, 0.8585, SentimentEnum.positive)


def test_analyze_sentiment_neutral():
    print(" ")
    print("score\t\tp\t\tlabel\t\t -\t\t |\t\t +\t\ttext")
    sentiment_test_case("This is crazy.", -0.34, 0.32999999999999996, SentimentEnum.negative)
    sentiment_test_case("I don't know.", 0.0, 0.5, SentimentEnum.neutral)
    sentiment_test_case("Perhaps.", 0.0, 0.5, SentimentEnum.neutral)
    sentiment_test_case("Possibly it is!", 0.0, 0.5, SentimentEnum.neutral)
    sentiment_test_case("Presumably.", 0.0, 0.5, SentimentEnum.neutral)
    sentiment_test_case("Let's go!.", 0.0, 0.5, SentimentEnum.neutral)
    sentiment_test_case("Let me answer this time!", 0.0, 0.5, SentimentEnum.neutral)
    sentiment_test_case("Mum!", 0.0, 0.5, SentimentEnum.neutral)
    sentiment_test_case("Let me ask my mum.", 0.0, 0.5, SentimentEnum.neutral)
    sentiment_test_case("Let me see where my mum is.", 0.0, 0.5, SentimentEnum.neutral)
    sentiment_test_case("Dad?", 0.0, 0.5, SentimentEnum.neutral)
    sentiment_test_case("Daddy, the computer is asking us something.", 0.0, 0.5, SentimentEnum.neutral)
    sentiment_test_case("Can you try harder to figure it out?", 0.0, 0.5, SentimentEnum.neutral)
    sentiment_test_case("Ya.", 0.0, 0.5, SentimentEnum.neutral)
    sentiment_test_case("Ya...", 0.0, 0.5, SentimentEnum.neutral)
    sentiment_test_case("Yesterday you did not ask.", 0.0, 0.5, SentimentEnum.neutral)
    sentiment_test_case("I'll be back.", 0.0, 0.5, SentimentEnum.neutral)
    # ?!
    sentiment_test_case("This is interesting.", 0.4019, 0.70095, SentimentEnum.positive)
    sentiment_test_case("This is exciting.", 0.4939, 0.74695, SentimentEnum.positive)
    sentiment_test_case("This is funny!", 0.4926, 0.7463, SentimentEnum.positive)


def test_analyze_sentiment_negative():
    print(" ")
    print("score\t\tp\t\tlabel\t\t -\t\t |\t\t +\t\ttext")
    sentiment_test_case("No, you failed!", -0.5562, 0.2219, SentimentEnum.negative)
    sentiment_test_case("No uhm yes.", -0.5358, 0.23209999999999997, SentimentEnum.negative)
    sentiment_test_case("No way!", -0.3595, 0.32025000000000003, SentimentEnum.negative)
    sentiment_test_case("No no!", -0.3595, 0.32025000000000003, SentimentEnum.negative)
    sentiment_test_case("No yes.", -0.3089, 0.34555, SentimentEnum.negative)
    sentiment_test_case("No no.", -0.296, 0.352, SentimentEnum.negative)
    sentiment_test_case("I do not like it.", -0.2755, 0.36224999999999996, SentimentEnum.negative)
    sentiment_test_case("Nah.", -0.1027, 0.44865, SentimentEnum.negative)
    # ?!
    sentiment_test_case("Never.", 0.0, 0.5, SentimentEnum.neutral)
    sentiment_test_case("Maybe.", 0.0, 0.5, SentimentEnum.neutral)
    sentiment_test_case("No.", 0.0, 0.5, SentimentEnum.negative)
    sentiment_test_case("Nope.", 0.0, 0.5, SentimentEnum.negative)
    sentiment_test_case("No, no.", 0.0, 0.5, SentimentEnum.negative)
    sentiment_test_case("No. No.", 0.0, 0.5, SentimentEnum.negative)
    sentiment_test_case("No. No!", 0.0, 0.5, SentimentEnum.negative)
    sentiment_test_case("No, it is not.", 0.0, 0.5, SentimentEnum.negative)
    sentiment_test_case("No, it is not a fox.", 0.0, 0.5, SentimentEnum.negative)
    sentiment_test_case("No no no.", 0.2235, 0.61175, SentimentEnum.negative)
    sentiment_test_case("No, it is not, you failed!", 0.4577, 0.72885, SentimentEnum.negative)
    sentiment_test_case("Hahaha no.", 0.5574, 0.7787, SentimentEnum.negative)

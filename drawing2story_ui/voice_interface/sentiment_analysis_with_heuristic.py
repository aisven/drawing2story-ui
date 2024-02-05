from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize

from enum import Enum


class SentimentEnum(Enum):
    positive = "positive"
    negative = "negative"
    neutral = "neutral"


def analyze_sentiment_pure(text):
    analyzer = SentimentIntensityAnalyzer()
    # sentiment compound score will be between -1 and 1
    scores = analyzer.polarity_scores(text)
    score = scores["compound"]
    # translate and scale for a score between 0 and 1
    score_0_1 = (score + 1.0) / 2.0
    # compute sentiment label
    label: str = "na"
    if score <= -0.05:
        label = SentimentEnum.negative.value
    elif 0.05 <= score:
        label = SentimentEnum.positive.value
    else:
        label = SentimentEnum.neutral.value
    return score, score_0_1, label, scores


def analyze_sentiment_with_heuristic(text):
    score, score_0_1, label, scores = analyze_sentiment_pure(text)
    label = apply_heuristic(text, label)
    return score, score_0_1, label, scores


def apply_heuristic(text, label):
    consolidated_label: str
    if label == SentimentEnum.positive.value or label == SentimentEnum.neutral.value:
        no_words_to_count = ["false", "no", "nope", "nah", "wrong"]
        no_word_count, no_word_count_total = count_words(text, no_words_to_count)
        yes_words_to_count = ["true", "yes", "yeh", "yeah", "correct"]
        yes_word_count, yes_word_count_total = count_words(text, yes_words_to_count)
        # note that the following works correctly as intended
        # even if both totals are 0
        # or if the yes-word total is 0
        # or if the no-word total os 0 and the yes-word total is greater than 0
        if yes_word_count_total < no_word_count_total and label == SentimentEnum.neutral.value:
            consolidated_label = SentimentEnum.negative.value
        elif yes_word_count_total < no_word_count_total and label == SentimentEnum.positive.value:
            consolidated_label = SentimentEnum.negative.value
        else:
            consolidated_label = label
    else:
        consolidated_label = label
    return consolidated_label


def count_words(text: str, words_to_count: list[str]) -> (dict[str, int], int):
    # Tokenize the text
    tokens = word_tokenize(text)

    # Remove punctuation and convert to lowercase
    words = [word.lower() for word in tokens if word.isalpha()]

    # Remove stopwords
    # stop_words = set(stopwords.words('english'))
    # words = [word for word in words if word not in stop_words]

    # Count the occurrences of specific  words
    word_count = {word: words.count(word) for word in words_to_count}
    word_count_values = word_count.values()
    total = sum(word_count_values)

    return word_count, total

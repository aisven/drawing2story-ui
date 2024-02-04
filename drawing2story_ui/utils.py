from PIL import Image
from io import BytesIO
import base64
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import random


def resize_image(image_data, max_size=(300, 300)):
    # Open the image from base64-encoded data
    img = Image.open(BytesIO(base64.b64decode(image_data)))

    # Resize the image while maintaining the aspect ratio
    img.thumbnail(max_size)

    # Convert the resized image back to base64-encoded data
    resized_image_data = base64.b64encode(img.tobytes()).decode("utf-8")

    return resized_image_data


# def sentiment_analysis(text):
#     # Create a TextBlob object
#     blob = TextBlob(text)
#     # Get the sentiment scores between -1 and 1
#     sentiment = blob.sentiment.polarity
#     # Get the sentiment label
#     if sentiment > 0.5:
#         label = "positive"
#     elif sentiment < -0.5:
#         label = "negative"
#     else:
#         label = "neutral"
#     return sentiment, label


def sentiment_analysis(text):
    # Create a SentimentIntensityAnalyzer object
    analyzer = SentimentIntensityAnalyzer()
    # Get the sentiment scores between -1 and 1
    sentiment = analyzer.polarity_scores(text)["compound"]
    # Get the sentiment label
    if sentiment > 0.0:
        label = "positive"
    elif sentiment < 0.0:
        label = "negative"
    else:
        label = "neutral"
    return sentiment, label


def animal_detection(image_data):
    # Load the image from base64-encoded data
    # generate a random number from 1 to 5
    numbers_of_animals = random.randint(2, 5)
    # generate random animal classes from [fox, owl, spider, cow, elephant]
    animal_classes = ["fox", "owl", "spider", "cow", "elephant"]
    # randomly select an animal class from the list
    animal_class = random.choice(animal_classes)
    numbers_of_animals = 3
    animal_class = "elephant"
    return numbers_of_animals, animal_class


def generate_story(n_animals, animal_class):
    story = (
        f"This is a story about {n_animals} {animal_class}s. One day, they stumbled upon a hidden waterfall with "
        f"magical waters."
    )
    return story

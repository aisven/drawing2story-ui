import base64
import random

from PIL import Image
from io import BytesIO


def resize_image(image_data, max_size=(300, 300)):
    # Open the image from base64-encoded data
    img = Image.open(BytesIO(base64.b64decode(image_data)))

    # Resize the image while maintaining the aspect ratio
    img.thumbnail(max_size)

    # Convert the resized image back to base64-encoded data
    resized_image_data = base64.b64encode(img.tobytes()).decode("utf-8")

    return resized_image_data


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

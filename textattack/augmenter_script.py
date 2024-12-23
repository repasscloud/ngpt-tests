import textattack
from textattack.augmentation import WordNetAugmenter

# Define the augmenter with a synonym replacement strategy
augmenter = WordNetAugmenter(transformations_per_example=5)

# Example input: User queries for corporate travel chatbot
inputs = [
    "Book a flight to New York",
    "Cancel my hotel reservation",
    "Can I see my itinerary for the conference?",
]

# Generate augmented data
augmented_data = []
for input_text in inputs:
    augmented = augmenter.augment(input_text)
    augmented_data.extend([(input_text, aug) for aug in augmented])

# Output the augmented data
for original, augmented in augmented_data:
    print(f"Original: {original}\nAugmented: {augmented}\n")

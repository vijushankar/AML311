import re
from collections import Counter

def most_frequent_words(file_path, num_words):
    # Read the text from the file
    with open(file_path, 'r') as file:
        text = file.read().lower()

    # Use regular expression to split the text into words
    words = re.findall(r'\b\w+\b', text)

    # Count the occurrences of each word using Counter
    word_counter = Counter(words)

    # Get the most frequent words
    most_frequent = word_counter.most_common(num_words)

    return most_frequent

# Test the function with a sample text file
file_path = 'sample_text.txt'  # Replace this with the path to your text file
num_words = 5  # Number of most frequent words to find

result = most_frequent_words(file_path, num_words)

# Display the most frequent words and their frequencies
print(f"The {num_words} most frequent words in the file are:")
for word, frequency in result:
    print(f"{word}: {frequency} occurrences")

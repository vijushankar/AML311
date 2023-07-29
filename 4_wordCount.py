def count_word_occurrences(sentence):
    # Convert the sentence to lowercase to treat uppercase and lowercase versions of the same word as equal.
    sentence = sentence.lower()
    
    # Remove punctuation marks from the sentence.
    punctuation_marks = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for char in sentence:
        if char in punctuation_marks:
            sentence = sentence.replace(char, "")
    
    # Split the sentence into words.
    words = sentence.split()
    
    # Create an empty dictionary to store word occurrences.
    word_occurrences = {}
    
    # Count the occurrences of each word and store them in the dictionary.
    for word in words:
        if word in word_occurrences:
            word_occurrences[word] += 1
        else:
            word_occurrences[word] = 1
    
    return word_occurrences

# Test the function with a sample sentence
sentence = "This is a sample sentence. This sentence is just for testing."
result = count_word_occurrences(sentence)
print(result)

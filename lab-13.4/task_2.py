def build_sentence(words):
    """
    Build a sentence by concatenating a list of words with spaces.

    Args:
        words (list): A list of strings representing words.

    Returns:
        str: A single string representing the concatenated sentence.
    """
    return " ".join(words)

# Example usage
words = ["AI", "helps", "in", "refactoring", "code"]
sentence = build_sentence(words)
print(sentence)
import re

class WordProcessor:
    def __init__(self):
        self.unique_words = set()

    def add_text(self, text):
        """Cleans and adds words to the unique set."""
        if not text:
            return
        
        # Using regex to remove punctuation more effectively
        words = re.findall(r'\b\w+\b', text.lower())
        for word in words:
            self.unique_words.add(word)

    def get_count(self):
        return len(self.unique_words)

    def clear(self):
        self.unique_words.clear()
class Kanji:
    def __init__(self, character, meanings, onyomi, kunyomi):
        self.character = character
        self.meanings = meanings  # List of meanings
        self.onyomi = onyomi      # List of onyomi readings
        self.kunyomi = kunyomi    # List of kunyomi readings

    def get_meanings(self):
        return self.meanings

    def get_readings(self):
        return {
            'onyomi': self.onyomi,
            'kunyomi': self.kunyomi
        }

    def __str__(self):
        return f"Kanji: {self.character}, Meanings: {', '.join(self.meanings)}, Onyomi: {', '.join(self.onyomi)}, Kunyomi: {', '.join(self.kunyomi)}"
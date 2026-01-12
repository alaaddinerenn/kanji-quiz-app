class Quiz:
    def __init__(self, kanji_data):
        self.kanji_data = kanji_data
        self.current_question = None
        self.score = 0

    def generate_meaning_question(self):
        import random
        self.current_question = random.choice(self.kanji_data)
        options = self._generate_options(self.current_question['meanings'])
        return self.current_question['character'], options

    def generate_reading_question(self):
        import random
        self.current_question = random.choice(self.kanji_data)
        options = self._generate_options(self.current_question['readings'])
        return self.current_question['character'], options

    def _generate_options(self, correct_answers):
        import random
        options = set(correct_answers)
        while len(options) < 4:
            random_meaning = random.choice(self.kanji_data)['meanings']
            options.add(random.choice(random_meaning))
        return random.sample(options, 4)

    def validate_answer(self, selected_option):
        return selected_option in self.current_question['meanings'] or selected_option in self.current_question['readings']

    def update_score(self, is_correct):
        if is_correct:
            self.score += 1
        return self.score
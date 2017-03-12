class Card:
    n_correct_translations = 0
    n_incorrect_translations = 0

    def __init__(self, origin_text, translated_text):
        self.origin_text = origin_text
        self.translated_text = translated_text

    def try_translation(self, translated_text):
        if self.translated_text == translated_text:
            self.n_correct_translations += 1
            return True
        else:
            self.n_incorrect_translations += 1
            return False

    def try_back_translation(self, origin_text):
        if self.origin_text == origin_text:
            self.n_correct_translations += 1
            return True
        else:
            self.n_incorrect_translations += 1
            return False

    def __str__(self):
        return '{{\n\t"origin": "{origin}",\n\t"translations": "{translation}"\n}}'.format(
            origin=self.origin_text,
            translation=self.translated_text)

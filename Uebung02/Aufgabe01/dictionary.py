from Uebung02.Aufgabe01.card import Card
import random


class Dictionary:
    cards = []

    def __init__(self, origin_language, destination_language):
        self.origin_language = origin_language
        self.destination_language = destination_language

    def add_card(self, origin_text, translated_text):
        self.cards.append(Card(origin_text, translated_text))

    def get_cards_sorted_by_n_correct(self, n_cards):
        return sorted(self.cards,
                      key=lambda card: card.n_correct_translations,
                      reverse=True
                      )[:n_cards]

    def get_cards_sorted_by_n_incorrect(self, n_cards):
        return sorted(self.cards,
                      key=lambda card: card.n_correct_translations,
                      reverse=True
                      )[:n_cards]

    def start_training(self, n_cards):
        correct_answers = 0
        cards = list(sorted(self.cards,
                            key=lambda card: card.n_incorrect_translations,
                            reverse=True))[:n_cards]
        print("Please type your translations:")
        for card in cards:
            if random.randint(0, 1) == 0:
                translation = input(card.origin_text + ": ")
                correct = card.try_translation(translation)
                print("correct!\n" if correct else "incorrect...\n")
                if correct:
                    correct_answers += 1
            else:
                translation = input(card.translated_text + ": ")
                correct = card.try_back_translation(translation)
                print("correct!\n" if correct else "incorrect...\n")
                if correct:
                    correct_answers += 1

        answer = input(
            "You got {correct} out of {n_questions} correct!"
            "Would you like to try again? (y/n)".format(
                correct=correct_answers,
                n_questions=len(cards)
            )
        )
        if answer == "y":
            return self.start_training(n_cards)

    def translate(self, origin_text):
        return next(filter(lambda card: card.origin_text == origin_text,
                           self.cards)).translated_text

    def translate_back(self, translated_text):
        return next(filter(lambda card: card.translated_text == translated_text,
                           self.cards)).origin_text

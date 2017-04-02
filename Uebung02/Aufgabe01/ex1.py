#!/usr/bin/env python3
# Rafael Kallis 14-708-887
# coding=utf-8
import random


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


def main():
    try:
        dict = Dictionary("English", "Greek")
        dict.add_card("science", "επιστήμη")
        dict.add_card("water", "νερό")
        dict.add_card("darkness", "σκοτάδι")
        dict.add_card("star", "άστρο")
        dict.add_card("economics", "οικονομικά")
        dict.add_card("radius", "ακτίνα")
        dict.add_card("computer", "υπολογιστής")
        dict.add_card("sun", "ήλιος")
        dict.add_card("circle", "κύκλος")
        dict.add_card("light", "φώς")
        print(*dict.cards, sep=',')
        print(dict.translate("computer"))
        print(dict.translate_back("υπολογιστής"))
        dict.start_training(2)
    except UnicodeEncodeError:
        print("Please execute this script using: export PYTHONIOENCODING=utf-8 && python3 result.py")


main()
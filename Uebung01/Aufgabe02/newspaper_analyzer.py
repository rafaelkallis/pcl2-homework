# Rafael Kallis 14-708-887

import re
from functools import reduce
import json


# Takes a file and parses its content into a string
def file_to_string(filename, encoding="utf-8"):
    file = open(filename, mode='r', encoding=encoding)
    content = file.read()
    file.close()
    return content


# Takes a string and writes it into a file
def string_to_file(filename, encoding='utf-8', string=''):
    file = open(filename, mode='w', encoding=encoding)
    file.write(string)
    file.close()


# Maps the text into a list of words
def to_word_list(text=''):
    words_only = re.sub(pattern='[^a-zA-Z0-9\s]*', repl='', string=text)
    words_list = re.split(pattern='\s', string=words_only)
    return words_list


# Maps the text into a list of sentences
def to_sentence_list(text=''):
    return re.split(pattern='\.\s*', string=text)


# Computes the number of words in the given text
def get_n_words(text=''):
    return len(to_word_list(text))


# Computes the longest word in the given text
def get_longest_word(text=''):
    return reduce(lambda w1, w2: w1 if len(w1) > len(w2) else w2, to_word_list(text))


# Computes the shortest word in the given text
def get_shortest_word(text=''):
    return reduce(lambda w1, w2: w1 if len(w1) < len(w2) else w2, to_word_list(text))


# Computes the average word length in the given text
def get_average_wordlen(text=''):
    word_list = to_word_list(text)
    return len("".join(word_list)) / len(word_list)


# Computes the average words per sentence in the given text
def get_average_words_per_sentence(text=''):
    sentence_list = to_sentence_list(text)
    n_words_per_sentence_list = map(lambda sentence: get_n_words(sentence), sentence_list)
    return reduce(lambda n_words1, n_words2: n_words1 + n_words2, n_words_per_sentence_list) / len(sentence_list)


# Computes the median words per sentence in the given text
def get_median_words_per_sentence(text=''):
    sentence_list = to_sentence_list(text)
    n_words_per_sentence_list = sorted(map(lambda sentence: get_n_words(sentence), sentence_list))
    return n_words_per_sentence_list[int(len(n_words_per_sentence_list) / 2)]


# Analyzes the given file and computes various metrics. Metrics are then written into a file named "analysis_output.txt"
def analyse_newspaper(filename, encoding='utf-8'):
    text = file_to_string(filename=filename, encoding=encoding)
    output = {
        'n_words': get_n_words(text),
        'longest_word': get_longest_word(text),
        'shortest_word': get_shortest_word(text),
        'average_word_len': get_average_wordlen(text),
        'average_words_per_sentence': get_average_words_per_sentence(text),
        'median_words_per_sentence': get_median_words_per_sentence(text)
    }
    string_to_file(filename='analysis_output.txt', encoding=encoding, string=json.dumps(output, indent=4))

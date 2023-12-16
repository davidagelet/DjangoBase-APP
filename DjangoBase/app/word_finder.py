import io


class WordFinder:
    def __init__(self, word_dictionary):
        self.dictionary_list = word_dictionary

    def longest_word(self, word):
        word = word.lower()
        letter_count = {letter: word.count(letter) for letter in set(word)}
        longest = ''

        for dict_word in self.dictionary_list:
            if len(dict_word) <= len(longest):
                continue
            if self._can_build_word(dict_word, letter_count):
                longest = dict_word

        return longest

    def _can_build_word(self, dict_word, letter_count):
        for letter in dict_word:
            if dict_word.count(letter) > letter_count.get(letter, 0):
                return False
        return True

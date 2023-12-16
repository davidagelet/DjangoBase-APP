from django.test import TestCase
from app.word_finder import WordFinder


class WordFinderTest(TestCase):
    def setUp(self):
        with open('app/files/google-10000-english.txt', 'r') as file:
            dictionary_list = [line.strip().lower() for line in file]
        self.finder = WordFinder(dictionary_list)

    def test_longest_word(self):
        result = self.finder.longest_word('optonoceari')
        self.assertEqual(result, 'cooperation')
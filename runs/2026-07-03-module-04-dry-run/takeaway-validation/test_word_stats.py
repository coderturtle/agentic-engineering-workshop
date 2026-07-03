import unittest

from word_stats import top_n_words


class TopNWordsTests(unittest.TestCase):
    def test_top_n_words_returns_n_items(self):
        text = "a a a b b c"
        self.assertEqual(top_n_words(text, 2), ["a", "b"])

    def test_top_n_words_handles_ties_alphabetically(self):
        text = "b a"
        self.assertEqual(top_n_words(text, 2), ["a", "b"])


if __name__ == "__main__":
    unittest.main()

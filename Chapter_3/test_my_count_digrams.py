from unittest import TestCase
import my_count_digrams


class TestMakeBigrams(TestCase):
    def test_make_bigrams(self):
        self.assertEqual(
            my_count_digrams.make_bigrams('volvo'),
            ['vo', 'ol', 'lv', 'vo']
        )
        self.assertEqual(
            my_count_digrams.make_bigrams('dinner'),
            ['di', 'in', 'nn', 'ne', 'er']
        )


class TestFilterBigrams(TestCase):
    def test_filter_bigrams(self):
        self.assertEqual(
            my_count_digrams.filter_bigrams('volvo', ['vo']),
            ['vo', 'vo']
        )

        self.assertEqual(
            my_count_digrams.filter_bigrams('volvo', ['vo']),
            ['vo', 'vo']
        )

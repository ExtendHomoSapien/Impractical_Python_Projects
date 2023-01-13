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

class TestIntersection(TestCase):
    def test_filter_bigrams(self):
        lst1 = [9, 9, 74, 21, 45, 11, 63]
        lst2 = [4, 9, 1, 17, 11, 26, 28, 28, 26, 66, 91]

        self.assertEqual(
            my_count_digrams.intersection(candidate=lst1, control=lst2),
            [9, 9, 11]
        )
from unittest import TestCase
import my_count_digrams


class TestMakeDigrams(TestCase):
    def test_make_digrams(self):
        self.assertEqual(
            my_count_digrams.make_digrams('volvo'),
            ['vo', 'ol', 'lv', 'vo']
        )
        self.assertEqual(
            my_count_digrams.make_digrams('dinner'),
            ['di', 'in', 'nn', 'ne', 'er']
        )


class TestFilterDigrams(TestCase):
    def test_filter_digrams(self):
        self.assertEqual(
            my_count_digrams.filter_digrams('volvo', ['vo']),
            ['vo', 'vo']
        )

        self.assertEqual(
            my_count_digrams.filter_digrams('volvo', ['vo']),
            ['vo', 'vo']
        )

class TestIntersection(TestCase):
    def test_filter_digrams(self):
        lst1 = [9, 9, 74, 21, 45, 11, 63]
        lst2 = [4, 9, 1, 17, 11, 26, 28, 28, 26, 66, 91]

        self.assertEqual(
            my_count_digrams.intersection(candidate=lst1, control=lst2),
            [9, 9, 11]
        )
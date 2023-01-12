from unittest import TestCase
import my_count_digrams


class TestMakeBigrams(TestCase):
    def test_make_bigrams(self):
        self.assertEqual(
            my_count_digrams.make_bigrams('volvo'),
            {'vo', 'lv', 'ol'}
        )
        self.assertEqual(
            my_count_digrams.make_bigrams('dinner'),
            {'di', 'in', 'nn','ne','er'}
        )
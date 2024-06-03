import unittest

from schooner_dice import score_calculator


class Testscore_calculator(unittest.TestCase):

    def test_score_ones(self):
        self.assertEqual(
            score_calculator.score(score_calculator.Category.ONES, [1, 2, 3, 4, 5]), 1
        )
        self.assertEqual(
            score_calculator.score(score_calculator.Category.ONES, [1, 2, 3, 4, 1]), 2
        )
        self.assertEqual(
            score_calculator.score(score_calculator.Category.ONES, [2, 2, 3, 4, 5]), 0
        )

    def test_score_twos(self):
        self.assertEqual(
            score_calculator.score(score_calculator.Category.TWOS, [1, 2, 3, 4, 5]), 2
        )
        self.assertEqual(
            score_calculator.score(score_calculator.Category.TWOS, [2, 2, 2, 2, 2]), 10
        )
        self.assertEqual(
            score_calculator.score(score_calculator.Category.TWOS, [1, 1, 3, 4, 5]), 0
        )

    def test_score_eights(self):
        self.assertEqual(
            score_calculator.score(score_calculator.Category.EIGHTS, [8, 7, 6, 5, 4]), 8
        )
        self.assertEqual(
            score_calculator.score(score_calculator.Category.EIGHTS, [1, 8, 2, 8, 3]),
            16,
        )
        self.assertEqual(
            score_calculator.score(score_calculator.Category.EIGHTS, [3, 4, 5, 6, 7]), 0
        )

    def test_score_three_of_a_kind(self):
        self.assertEqual(
            score_calculator.score(
                score_calculator.Category.THREE_OF_A_KIND, [1, 2, 2, 2, 5]
            ),
            12,
        )
        self.assertEqual(
            score_calculator.score(
                score_calculator.Category.THREE_OF_A_KIND, [1, 2, 2, 4, 5]
            ),
            0,
        )

    def test_score_four_of_a_kind(self):
        self.assertEqual(
            score_calculator.score(
                score_calculator.Category.FOUR_OF_A_KIND, [1, 2, 2, 2, 2]
            ),
            9,
        )
        self.assertEqual(
            score_calculator.score(
                score_calculator.Category.FOUR_OF_A_KIND, [8, 8, 8, 8, 8]
            ),
            40,
        )
        self.assertEqual(
            score_calculator.score(
                score_calculator.Category.FOUR_OF_A_KIND, [1, 2, 2, 2, 5]
            ),
            0,
        )

    def test_score_full_house(self):
        self.assertEqual(
            score_calculator.score(
                score_calculator.Category.FULL_HOUSE, [1, 2, 2, 2, 1]
            ),
            25,
        )
        self.assertEqual(
            score_calculator.score(
                score_calculator.Category.FULL_HOUSE, [7, 7, 8, 8, 8]
            ),
            25,
        )
        self.assertEqual(
            score_calculator.score(
                score_calculator.Category.FULL_HOUSE, [1, 2, 2, 2, 5]
            ),
            0,
        )

    def test_score_small_straight(self):
        self.assertEqual(
            score_calculator.score(
                score_calculator.Category.SMALL_STRAIGHT, [1, 2, 3, 4, 5]
            ),
            30,
        )
        self.assertEqual(
            score_calculator.score(
                score_calculator.Category.SMALL_STRAIGHT, [1, 4, 3, 4, 2]
            ),
            30,
        )
        self.assertEqual(
            score_calculator.score(
                score_calculator.Category.SMALL_STRAIGHT, [1, 2, 3, 3, 3]
            ),
            0,
        )

    def test_score_large_straight(self):
        self.assertEqual(
            score_calculator.score(
                score_calculator.Category.LARGE_STRAIGHT, [4, 2, 3, 1, 5]
            ),
            40,
        )
        self.assertEqual(
            score_calculator.score(
                score_calculator.Category.LARGE_STRAIGHT, [4, 3, 1, 2, 4]
            ),
            0,
        )
        self.assertEqual(
            score_calculator.score(
                score_calculator.Category.LARGE_STRAIGHT, [7, 6, 1, 2, 8]
            ),
            0,
        )

    def test_score_all_different(self):
        self.assertEqual(
            score_calculator.score(
                score_calculator.Category.ALL_DIFFERENT, [4, 2, 3, 1, 5]
            ),
            35,
        )
        self.assertEqual(
            score_calculator.score(
                score_calculator.Category.ALL_DIFFERENT, [4, 5, 3, 1, 5]
            ),
            0,
        )
        self.assertEqual(
            score_calculator.score(
                score_calculator.Category.ALL_DIFFERENT, [8, 8, 8, 8, 8]
            ),
            0,
        )

    def test_score_schooner(self):
        self.assertEqual(
            score_calculator.score(score_calculator.Category.SCHOONER, [1, 1, 1, 1, 1]),
            50,
        )
        self.assertEqual(
            score_calculator.score(score_calculator.Category.SCHOONER, [4, 4, 4, 4, 4]),
            50,
        )
        self.assertEqual(
            score_calculator.score(score_calculator.Category.SCHOONER, [8, 8, 8, 8, 8]),
            50,
        )
        self.assertEqual(
            score_calculator.score(score_calculator.Category.SCHOONER, [4, 5, 6, 7, 8]),
            0,
        )
        self.assertEqual(
            score_calculator.score(score_calculator.Category.SCHOONER, [4, 4, 4, 4, 1]),
            0,
        )

    def test_score_chance(self):
        self.assertEqual(
            score_calculator.score(score_calculator.Category.CHANCE, [1, 1, 1, 1, 1]), 5
        )
        self.assertEqual(
            score_calculator.score(score_calculator.Category.CHANCE, [1, 2, 3, 4, 5]),
            15,
        )
        self.assertEqual(
            score_calculator.score(score_calculator.Category.CHANCE, [8, 7, 6, 5, 4]),
            30,
        )
        self.assertEqual(
            score_calculator.score(score_calculator.Category.CHANCE, [8, 8, 8, 8, 8]),
            40,
        )

    def test_top_categories(self):
        self.assertEqual(
            score_calculator.top_categories([1, 2, 3, 4, 5]),
            [score_calculator.Category.LARGE_STRAIGHT],
        )
        self.assertEqual(
            score_calculator.top_categories([4, 5, 6, 7, 8]),
            [score_calculator.Category.LARGE_STRAIGHT],
        )
        self.assertEqual(
            score_calculator.top_categories([1, 2, 3, 4, 4]),
            [score_calculator.Category.SMALL_STRAIGHT],
        )
        self.assertEqual(
            score_calculator.top_categories([4, 5, 6, 7, 7]),
            [score_calculator.Category.SMALL_STRAIGHT],
        )
        self.assertEqual(
            score_calculator.top_categories([1, 3, 5, 7, 8]),
            [score_calculator.Category.ALL_DIFFERENT],
        )
        self.assertEqual(
            score_calculator.top_categories([8, 7, 6, 5, 3]),
            [score_calculator.Category.ALL_DIFFERENT],
        )
        self.assertEqual(
            score_calculator.top_categories([8, 8, 8, 8, 8]),
            [score_calculator.Category.SCHOONER],
        )
        self.assertEqual(
            score_calculator.top_categories([1, 1, 1, 1, 1]),
            [score_calculator.Category.SCHOONER],
        )
        self.assertEqual(
            score_calculator.top_categories([8, 8, 8, 8, 1]),
            [
                score_calculator.Category.THREE_OF_A_KIND,
                score_calculator.Category.FOUR_OF_A_KIND,
                score_calculator.Category.CHANCE,
            ],
        )
        self.assertEqual(
            score_calculator.top_categories([1, 1, 1, 1, 8]),
            [
                score_calculator.Category.THREE_OF_A_KIND,
                score_calculator.Category.FOUR_OF_A_KIND,
                score_calculator.Category.CHANCE,
            ],
        )
        self.assertEqual(
            score_calculator.top_categories([7, 7, 8, 8, 8]),
            [
                score_calculator.Category.THREE_OF_A_KIND,
                score_calculator.Category.CHANCE,
            ],
        )
        self.assertEqual(
            score_calculator.top_categories([1, 1, 2, 2, 2]),
            [score_calculator.Category.FULL_HOUSE],
        )
        self.assertEqual(
            score_calculator.top_categories([2, 2, 7, 7, 7]),
            [
                score_calculator.Category.THREE_OF_A_KIND,
                score_calculator.Category.CHANCE,
                score_calculator.Category.FULL_HOUSE,
            ],
        )


if __name__ == "__main__":
    unittest.main()

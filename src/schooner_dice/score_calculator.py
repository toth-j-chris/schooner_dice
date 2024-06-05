"""A module for scoring a dice game.

This module contains scoring logic for a dice game that involves rolling
five eight-sided dice. The values of the dice are used to determine whether
the dice_roll qualifies for a certain Category. The Category determines how the overall
score of the dice_roll is calculated.

    Typical usage example:
    # get the score for the ONES category of a dice_roll
    score(Category.ONES, [1, 1, 1, 1, 1]) # returns 5

    # get the top scoring categories for a roll
    top_categories([1, 1, 1, 1, 1]) # returns Category.SCHOONER
"""

from enum import Enum
from collections import Counter


class Category(Enum):
    """Enum aliasing category names to int values.

    The number categories (ONES, TWOS, ... , EIGHTS) map to the die value that
    they represent.

    THREE_OF_A_KIND, FOUR_OF_A_KIND, and CHANCE have arbitrary values.

    The remaining aliases map to the score-value for their respective category.
    """

    ONES = 1
    TWOS = 2
    THREES = 3
    FOURS = 4
    FIVES = 5
    SIXES = 6
    SEVENS = 7
    EIGHTS = 8
    THREE_OF_A_KIND = 9
    FOUR_OF_A_KIND = 10
    CHANCE = 11
    FULL_HOUSE = 25
    SMALL_STRAIGHT = 30
    ALL_DIFFERENT = 35
    LARGE_STRAIGHT = 40
    SCHOONER = 50

    @classmethod
    def is_number_category(cls, category: Enum) -> bool:
        if category in {
            cls.ONES,
            cls.TWOS,
            cls.THREES,
            cls.FOURS,
            cls.FIVES,
            cls.SIXES,
            cls.SEVENS,
            cls.EIGHTS,
        }:
            return True

        return False


def score(category: Category, dice_roll: list[int]) -> int:
    """Calculates the score for the given Category and dice_roll.

    Args:
        category: The Category to score against.
        dice_roll: A list of ints representing the rolled dice.

    Returns:
        An integer representing the score for the dice_roll in the given
        category.
    """
    # dictionary of # occurrences for each die value
    roll_counts = Counter(dice_roll)
    roll_set = set(dice_roll)
    
    if Category.is_number_category(category):
        return roll_counts.get(category.value, 0) * category.value

    if category == Category.THREE_OF_A_KIND and any(
        count >= 3 for count in roll_counts.values()
    ):
        return sum(dice_roll)

    if category == Category.FOUR_OF_A_KIND and any(
        count >= 4 for count in roll_counts.values()
    ):
        return sum(dice_roll)

    if (
        category == Category.FULL_HOUSE
        and 3 in roll_counts.values()
        and 2 in roll_counts.values()
    ):
        return Category.FULL_HOUSE.value

    if category == Category.SMALL_STRAIGHT and _has_straight(dice_roll, 4):
        return Category.SMALL_STRAIGHT.value

    if category == Category.ALL_DIFFERENT and len(roll_set) == 5:
        return Category.ALL_DIFFERENT.value

    if category == Category.LARGE_STRAIGHT and _has_straight(dice_roll, 5):
        return Category.LARGE_STRAIGHT.value

    if category == Category.SCHOONER and len(roll_set) == 1:
        return Category.SCHOONER.value

    if category == Category.CHANCE:
        return sum(dice_roll)

    return 0


def _has_straight(roll_set: set[int], length: int) -> bool:
    """Checks dice_roll for a straight of {length} size.

    A straight consists of consecutive numbers occurring in the same dice_roll.
    The length defines how many consecutive numbers need to be present to
    return True.

    Args:
        dice_roll: A list of ints representing the rolled dice.
        length: The number of consecutive values to check for.

    Returns:
        True if a straight of the specified length is present in the dice roll.
        False if there is no straight of the specified length.
    """
    # sorted list of the unique values in the dice_roll
    sorted_rolls = sorted(roll_set)

    # if range initializes with 0 or negative, not enough values for a straight
    for i in range((len(sorted_rolls) - length) + 1):
        # sliding window looking for a straight subarray
        if sorted_rolls[i + length - 1] - sorted_rolls[i] == length - 1:
            return True
    return False


def top_categories(dice_roll: list[int]) -> list[Category]:
    """Calculate the highest scoring categories for a given dice_roll.

    If more than one Category has the highest score, all categories with
    the high score will be returned in the list. If only one category has
    the highest score, the return type will still be a list, but will contain
    only one Category.

    Args:
        dice_roll: A list of ints representing the rolled dice.

    Returns:
        A list of one or more Categories.
    """

    scores = {category: score(category, dice_roll) for category in Category}
    top_score = max(scores.values())
    return [category for category, cat_score in scores.items() if cat_score == top_score]

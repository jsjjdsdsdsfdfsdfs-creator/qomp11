"""
QOMP - Utility Functions
Common functions for numerology, date calculations, and system operations
"""

from datetime import datetime, date, timedelta
from typing import Union, List, Tuple
import math
from .config import PYTHAGOREAN_MAP, CHALDEAN_MAP, MASTER_NUMBERS, VEDIC_MAP

# ============================================================================
# REDUCTION FUNCTIONS
# ============================================================================

def reduce_to_single_digit(num: int, preserve_master: bool = True) -> int:
    """
    Reduce a number to single digit, optionally preserving master numbers.
    
    Args:
        num: Number to reduce
        preserve_master: If True, keep 11, 22, 33, etc. Otherwise reduce to 1-9
    
    Returns:
        Reduced number (1-9 or 11, 22, 33 if preserve_master=True)
    """
    if num < 1:
        return 1
    
    while num >= 10:
        if preserve_master and num in MASTER_NUMBERS:
            return num
        num = sum(int(digit) for digit in str(num))
    
    return num


def sum_digits(num: int) -> int:
    """Sum all digits in a number"""
    return sum(int(d) for d in str(abs(num)))


def name_to_value(name: str, letter_map: dict, include_vowels_only: bool = False) -> int:
    """
    Convert a name to numerical value using given letter mapping.
    
    Args:
        name: Name or text to convert
        letter_map: Dictionary mapping letters to numbers
        include_vowels_only: If True, only sum vowel letters
    
    Returns:
        Sum of letter values (not reduced)
    """
    name_upper = name.upper().strip()
    total = 0
    
    for char in name_upper:
        if char.isalpha() and char in letter_map:
            total += letter_map[char]
    
    return total if total > 0 else 0


def get_vowel_sum(name: str, letter_map: dict, vowel_set: set) -> int:
    """Sum only vowel letters"""
    name_upper = name.upper().strip()
    total = 0
    
    for char in name_upper:
        if char in vowel_set and char in letter_map:
            total += letter_map[char]
    
    return total


def get_consonant_sum(name: str, letter_map: dict, vowel_set: set) -> int:
    """Sum only consonant letters"""
    name_upper = name.upper().strip()
    total = 0
    
    for char in name_upper:
        if char.isalpha() and char not in vowel_set and char in letter_map:
            total += letter_map[char]
    
    return total


# ============================================================================
# DATE CALCULATIONS
# ============================================================================

def universal_year(year: int) -> int:
    """Calculate universal year number"""
    return reduce_to_single_digit(sum_digits(year))


def personal_year(birth_day: int, birth_month: int, current_year: int) -> int:
    """
    Calculate personal year number
    personal_year = reduce(birth_day + birth_month + universal_year)
    """
    u_year = universal_year(current_year)
    return reduce_to_single_digit(birth_day + birth_month + u_year)


def personal_month(birth_day: int, birth_month: int, current_year: int, current_month: int) -> int:
    """
    Calculate personal month number
    personal_month = reduce(personal_year + current_month)
    """
    p_year = personal_year(birth_day, birth_month, current_year)
    return reduce_to_single_digit(p_year + current_month)


def personal_day(birth_day: int, birth_month: int, current_year: int, 
                 current_month: int, current_day: int) -> int:
    """
    Calculate personal day number
    personal_day = reduce(personal_month + current_day)
    """
    p_month = personal_month(birth_day, birth_month, current_year, current_month)
    return reduce_to_single_digit(p_month + current_day)


def gregorian_to_hebrew_year(gregorian_year: int) -> int:
    """Convert Gregorian year to Hebrew year (approximation)"""
    return gregorian_year + 3760


def is_leap_year(year: int) -> bool:
    """Check if year is leap year"""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def days_in_month(year: int, month: int) -> int:
    """Get number of days in month"""
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 29 if is_leap_year(year) else 28
    else:
        raise ValueError(f"Invalid month: {month}")


# ============================================================================
# PYTHAGOREAN NUMEROLOGY
# ============================================================================

def pythagorean_life_path(birth_day: int, birth_month: int, birth_year: int) -> int:
    """
    Calculate Pythagorean life path number
    life_path = reduce(month + day + sum_digits(year))
    """
    year_sum = sum_digits(birth_year)
    return reduce_to_single_digit(birth_day + birth_month + year_sum)


def pythagorean_expression(name: str) -> Tuple[int, int]:
    """
    Calculate Pythagorean expression number
    
    Returns:
        (compound_value, reduced_value)
    """
    compound = name_to_value(name, PYTHAGOREAN_MAP)
    reduced = reduce_to_single_digit(compound)
    return (compound, reduced)


def pythagorean_soul_urge(name: str) -> int:
    """Calculate Pythagorean soul urge (vowels only)"""
    vowel_sum = get_vowel_sum(name, PYTHAGOREAN_MAP, {'A', 'E', 'I', 'O', 'U'})
    return reduce_to_single_digit(vowel_sum)


def pythagorean_personality(name: str) -> int:
    """Calculate Pythagorean personality number (consonants only)"""
    consonant_sum = get_consonant_sum(name, PYTHAGOREAN_MAP, {'A', 'E', 'I', 'O', 'U'})
    return reduce_to_single_digit(consonant_sum)


def pythagorean_pinnacles(birth_day: int, birth_month: int, birth_year: int) -> List[int]:
    """
    Calculate Pythagorean pinnacles
    1st = reduce(month + day)
    2nd = reduce(day + sum_digits(year))
    3rd = reduce(1st + 2nd)
    4th = reduce(month + sum_digits(year))
    """
    month_day = reduce_to_single_digit(birth_month + birth_day)
    day_year = reduce_to_single_digit(birth_day + sum_digits(birth_year))
    p1 = month_day
    p2 = day_year
    p3 = reduce_to_single_digit(p1 + p2)
    p4 = reduce_to_single_digit(birth_month + sum_digits(birth_year))
    
    return [p1, p2, p3, p4]


def pythagorean_challenges(birth_day: int, birth_month: int, birth_year: int) -> List[int]:
    """
    Calculate Pythagorean challenges
    ch1 = |month - day|
    ch2 = |day - sum_digits(year)|
    ch3 = |ch1 - ch2|
    ch4 = |month - sum_digits(year)|
    """
    year_sum = sum_digits(birth_year)
    ch1 = abs(birth_month - birth_day)
    ch2 = abs(birth_day - year_sum)
    ch3 = abs(ch1 - ch2)
    ch4 = abs(birth_month - year_sum)
    
    return [ch1, ch2, ch3, ch4]


# ============================================================================
# CHALDEAN NUMEROLOGY
# ============================================================================

def chaldean_birth_number(birth_day: int) -> int:
    """Chaldean birth number = reduce(day)"""
    return reduce_to_single_digit(birth_day)


def chaldean_destiny_number(birth_day: int, birth_month: int, birth_year: int) -> int:
    """Chaldean destiny = reduce(day + month + sum_digits(year))"""
    year_sum = sum_digits(birth_year)
    return reduce_to_single_digit(birth_day + birth_month + year_sum)


def chaldean_name_number(name: str) -> Tuple[int, int]:
    """
    Chaldean name number
    
    Returns:
        (compound_value, reduced_value)
    """
    compound = name_to_value(name, CHALDEAN_MAP)
    reduced = reduce_to_single_digit(compound)
    return (compound, reduced)


def check_karmic_debt(compound_value: int, reduced_value: int) -> Tuple[bool, List[int]]:
    """
    Check for Chaldean karmic debts
    
    Returns:
        (has_debt, list_of_debts)
    """
    debts = []
    
    # Classic karmic debts
    if compound_value in [13, 14, 16, 19]:
        debts.append(compound_value)
    
    # Hidden debts (reduced value matches debt pattern but compound wasn't explicit debt)
    if reduced_value in [4, 5, 7, 1] and compound_value not in [13, 14, 16, 19]:
        # This is a hidden debt pattern
        pass
    
    return (len(debts) > 0, debts)


# ============================================================================
# LUNAR CALCULATIONS
# ============================================================================

def lunar_day(analysis_date: date, reference_new_moon: date = None) -> float:
    """
    Calculate lunar day (tithi)
    Reference: 6 Jan 2000 was a new moon
    
    Args:
        analysis_date: Date to calculate for
        reference_new_moon: Reference new moon date (default: 2000-01-06)
    
    Returns:
        Lunar day (1-29.53, approximately)
    """
    if reference_new_moon is None:
        reference_new_moon = date(2000, 1, 6)
    
    days_diff = (analysis_date - reference_new_moon).days
    lunar_cycle = 29.53
    
    return (days_diff % lunar_cycle) + 1


def lunar_phase_name(lunar_day: float) -> str:
    """Get name of lunar phase"""
    if 1 <= lunar_day < 8:
        return "Waxing Crescent"
    elif 8 <= lunar_day < 15:
        return "Waxing Gibbous"
    elif 15 <= lunar_day < 22:
        return "Waning Gibbous"
    else:
        return "Waning Crescent"


# ============================================================================
# CHINESE CALCULATIONS
# ============================================================================

def chinese_stem_branch_year(year: int) -> Tuple[int, int]:
    """
    Calculate Chinese zodiac stem and branch for year
    stem = (year - 4) % 10
    branch = year % 12
    """
    stem = (year - 4) % 10
    branch = year % 12
    return (stem, branch)


def chinese_animal_year(year: int) -> str:
    """Get Chinese zodiac animal for year"""
    animals = ['Rat', 'Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake',
               'Horse', 'Goat', 'Monkey', 'Rooster', 'Dog', 'Pig']
    return animals[year % 12]


def ordinal_date(dt: date) -> int:
    """Get ordinal date number (days since year 0)"""
    return dt.toordinal()


def iching_hexagram(days_since_epoch: int) -> int:
    """
    Calculate I-Ching hexagram for a given day
    hex = (lower_trigram * 8) + upper_trigram + 1
    where trigrams are calculated from days
    """
    upper = (days_since_epoch // 8) % 8
    lower = days_since_epoch % 8
    hex_num = (lower * 8) + upper + 1
    return max(1, min(64, hex_num))


# ============================================================================
# ANGULAR CALCULATIONS
# ============================================================================

def normalize_angle(angle: float) -> float:
    """Normalize angle to 0-360 range"""
    return angle % 360


def angle_difference(angle1: float, angle2: float) -> float:
    """
    Calculate smallest difference between two angles
    Returns value between 0 and 180
    """
    diff = abs(angle1 - angle2)
    if diff > 180:
        diff = 360 - diff
    return diff


def cos_distance(angle: float) -> float:
    """
    Calculate harmonic distance using cosine
    Used for CPI and other calculations
    """
    # Convert angle to radians and calculate cosine
    rad = math.radians(angle)
    return math.cos(rad)


# ============================================================================
# PRICE LEVEL CALCULATIONS
# ============================================================================

def fibonacci_levels(price: float, depth: int = 3) -> dict:
    """
    Calculate Fibonacci support and resistance levels
    
    Args:
        price: Current price
        depth: Number of levels to calculate
    
    Returns:
        Dictionary with levels
    """
    fib_ratios = [0.236, 0.382, 0.5, 0.618, 0.786, 1.0]
    
    support = {}
    resistance = {}
    
    for i, ratio in enumerate(fib_ratios[:depth]):
        support[f"S{i+1}"] = price * (1 - ratio)
        resistance[f"R{i+1}"] = price * (1 + ratio)
    
    return {"support": support, "resistance": resistance}


def numerology_price_levels(price: float, numerology_value: int) -> List[float]:
    """
    Calculate price levels based on numerology value
    
    Simple approach: use numerology number as percentage variance
    """
    offset = (numerology_value / 100.0)
    
    return [
        price * (1 - offset),
        price,
        price * (1 + offset),
    ]


# ============================================================================
# TEXT & TRANSLATION
# ============================================================================

def to_english(text: str) -> str:
    """Convert text to English (placeholder for translation)"""
    # In production, use proper translation library
    return text


def to_farsi(text: str) -> str:
    """Convert text to Farsi (placeholder for translation)"""
    # In production, use proper translation library
    return text


__all__ = [
    'reduce_to_single_digit', 'sum_digits', 'name_to_value',
    'universal_year', 'personal_year', 'personal_month', 'personal_day',
    'pythagorean_life_path', 'pythagorean_expression',
    'chaldean_birth_number', 'chaldean_destiny_number',
    'lunar_day', 'lunar_phase_name',
    'chinese_stem_branch_year', 'chinese_animal_year',
    'iching_hexagram', 'angle_difference', 'normalize_angle',
    'fibonacci_levels', 'numerology_price_levels'
]

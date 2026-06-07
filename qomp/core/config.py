"""
QOMP - Quantum Optimization Multi-dimensional Positioning
Financial AI System with Numerology & Astrology Analysis

Core configuration and constants
"""

from enum import Enum
from datetime import datetime
from typing import Dict

# ============================================================================
# SYSTEM CONFIGURATION
# ============================================================================

class AssetType(Enum):
    """Supported asset types"""
    STOCK = "stock"
    CRYPTO = "crypto"
    FOREX = "forex"
    INDEX = "index"
    COMMODITY = "commodity"
    REALESTATE = "realestate"
    METAL = "metal"
    TECHNOLOGY = "technology"

class TimeFrame(Enum):
    """Supported time frames"""
    M1 = "1m"
    M5 = "5m"
    M15 = "15m"
    M30 = "30m"
    H1 = "1h"
    H4 = "4h"
    D1 = "1d"
    W1 = "1w"
    MN = "1mo"

class SignalType(Enum):
    """Trading signal types"""
    BUY = "BUY"
    SELL = "SELL"
    NEUTRAL = "NEUTRAL"
    HOLD = "HOLD"

# ============================================================================
# NUMEROLOGY LETTER MAPPINGS
# ============================================================================

PYTHAGOREAN_MAP = {
    'A': 1, 'J': 1, 'S': 1,
    'B': 2, 'K': 2, 'T': 2,
    'C': 3, 'L': 3, 'U': 3,
    'D': 4, 'M': 4, 'V': 4,
    'E': 5, 'N': 5, 'W': 5,
    'F': 6, 'O': 6, 'X': 6,
    'G': 7, 'P': 7, 'Y': 7,
    'H': 8, 'Q': 8, 'Z': 8,
    'I': 9, 'R': 9
}

PYTHAGOREAN_VOWELS = {'A', 'E', 'I', 'O', 'U'}

CHALDEAN_MAP = {
    'A': 1, 'I': 1, 'J': 1, 'Q': 1, 'Y': 1,
    'B': 2, 'K': 2, 'R': 2,
    'C': 3, 'G': 3, 'L': 3, 'S': 3,
    'D': 4, 'M': 4, 'T': 4,
    'E': 5, 'H': 5, 'N': 5, 'X': 5,
    'U': 6, 'V': 6, 'W': 6,
    'O': 7, 'Z': 7,
    'F': 8, 'P': 8
}

CHALDEAN_VOWELS = {'A', 'E', 'I', 'O', 'U', 'Y'}  # Y at end is vowel

VEDIC_MAP = CHALDEAN_MAP  # Same as Chaldean (Chiero system)
VEDIC_VOWELS = CHALDEAN_VOWELS

CHINESE_STEM_NAMES = ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']
CHINESE_BRANCH_NAMES = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']
CHINESE_ANIMALS = ['Rat', 'Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake', 
                   'Horse', 'Goat', 'Monkey', 'Rooster', 'Dog', 'Pig']

# ============================================================================
# NUMEROLOGY ANALYSIS CONSTANTS
# ============================================================================

MASTER_NUMBERS = {11, 22, 33, 44, 55, 66, 77, 88, 99}
CHALDEAN_KARMIC_DEBTS = {13, 14, 16, 19}

# Chaldean Cycloscope Phase Mapping
CYCLOSCOPE_PHASES = {
    1: {"name": "Initiation", "markets": ["Technology", "Crypto", "Innovation"], "planet": "Sun"},
    2: {"name": "Cooperation", "markets": ["Bonds", "Joint Ventures", "Partnerships"], "planet": "Moon"},
    3: {"name": "Creativity", "markets": ["Media", "Gaming", "Entertainment"], "planet": "Jupiter"},
    4: {"name": "Consolidation", "markets": ["Real Estate", "Infrastructure", "Construction"], "planet": "Rahu"},
    5: {"name": "Volatility", "markets": ["Forex", "Commodities", "Energy"], "planet": "Mercury"},
    6: {"name": "Value", "markets": ["Consumer", "Healthcare", "Utilities"], "planet": "Venus"},
    7: {"name": "Research", "markets": ["Biotech", "R&D", "Education"], "planet": "Ketu"},
    8: {"name": "Power", "markets": ["Blue-chip Stocks", "Banks", "Finance"], "planet": "Saturn"},
    9: {"name": "Completion", "markets": ["Gold", "Cash", "Precious Metals"], "planet": "Mars"}
}

# Kabbalistic Sefirot Market Mapping
SEFIROT_MAP = {
    1: {"name": "Keter (Unity)", "markets": ["New Ventures", "IPOs"], "element": "Ether"},
    2: {"name": "Chokmah (Wisdom)", "markets": ["R&D", "Tech Startups"], "element": "Fire"},
    3: {"name": "Binah (Understanding)", "markets": ["Analysis", "Data Services"], "element": "Water"},
    4: {"name": "Chesed (Expansion)", "markets": ["Bull Markets", "Liquidity"], "element": "Water"},
    5: {"name": "Gevurah (Contraction)", "markets": ["Risk-off", "Corrections"], "element": "Fire"},
    6: {"name": "Tiferet (Balance)", "markets": ["Dividend Stocks", "Balanced Funds"], "element": "Air"},
    7: {"name": "Netzach (Speculation)", "markets": ["Crypto", "Options"], "element": "Venus"},
    8: {"name": "Hod (Mind)", "markets": ["Algo Trading", "Structured Finance"], "element": "Mercury"},
    9: {"name": "Yesod (Foundation)", "markets": ["Infrastructure", "Real Estate"], "element": "Moon"},
    10: {"name": "Malkuth (Physical)", "markets": ["Commodities", "Physical Assets"], "element": "Earth"}
}

# Chinese Ba Zi Elements
CHINESE_ELEMENTS = {
    0: "Wood",
    1: "Fire", 
    2: "Earth",
    3: "Metal",
    4: "Water"
}

ELEMENT_PRODUCTION = {  # Element X produces Element Y
    "Wood": "Fire",
    "Fire": "Earth",
    "Earth": "Metal",
    "Metal": "Water",
    "Water": "Wood"
}

ELEMENT_CONTROL = {  # Element X controls Element Y
    "Wood": "Earth",
    "Fire": "Metal",
    "Earth": "Water",
    "Metal": "Wood",
    "Water": "Fire"
}

# Qi Men Dun Jia Doors
QIMEN_DOORS = {
    0: {'name': '休', 'code': 'Rest'},
    1: {'name': '生', 'code': 'Life'},
    2: {'name': '傷', 'code': 'Harm'},
    3: {'name': '杜', 'code': 'Blocked'},
    4: {'name': '景', 'code': 'Vision'},
    5: {'name': '死', 'code': 'Death'},
    6: {'name': '驚', 'code': 'Shock'},
    7: {'name': '開', 'code': 'Open'},
    8: {'name': '開', 'code': 'Open'},  # Repeats for 9 stems
}

# Chinese Auspicious & Inauspicious Numbers (81 Numbers)
AUSPICIOUS_81 = {15, 16, 24, 29, 32, 33, 41, 52, 53, 55, 63, 68, 81}
INAUSPICIOUS_81 = {14, 19, 22, 26, 27, 34, 36, 40, 42, 43, 44, 46, 49, 50, 
                   56, 58, 59, 60, 62, 64, 66, 69, 70, 74, 76, 78, 79, 80}

# ============================================================================
# ASTROLOGY CONSTANTS
# ============================================================================

ZODIAC_SIGNS = [
    'Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo',
    'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces'
]

PLANETS = ['Sun', 'Moon', 'Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 
           'Uranus', 'Neptune', 'Pluto', 'Node']

ASPECTS = {
    'conjunction': {'orb': 8, 'type': 'hard'},
    'opposition': {'orb': 8, 'type': 'hard'},
    'trine': {'orb': 6, 'type': 'soft'},
    'square': {'orb': 6, 'type': 'hard'},
    'sextile': {'orb': 4, 'type': 'soft'},
}

# ============================================================================
# ML & SIGNAL PROCESSING
# ============================================================================

# Default weights for signal fusion
SIGNAL_WEIGHTS = {
    'ml_model': 0.50,           # Machine Learning prediction
    'numerology': 0.30,         # All numerology schools combined
    'astrology': 0.20,          # Astrology transits & natal
}

# Signal thresholds
BUY_THRESHOLD = 0.52
SELL_THRESHOLD = 0.48
CONFIDENCE_BOOST = 1.05  # Cycloscope phase alignment boost

# ============================================================================
# HEBREW ALPHABET & GEMATRIA
# ============================================================================

HEBREW_LETTERS = {
    'A': 'א', 'B': 'ב', 'C': 'כ', 'D': 'ד', 'E': 'ה',
    'F': 'פ', 'G': 'ג', 'H': 'ה', 'I': 'י', 'J': 'י',
    'K': 'כ', 'L': 'ל', 'M': 'מ', 'N': 'נ', 'O': 'ו',
    'P': 'פ', 'Q': 'ק', 'R': 'ר', 'S': 'ס', 'T': 'ט',
    'U': 'ו', 'V': 'ו', 'W': 'ו', 'X': 'צ', 'Y': 'י', 'Z': 'ז'
}

GEMATRIA_STANDARD = {
    'א': 1, 'ב': 2, 'ג': 3, 'ד': 4, 'ה': 5, 'ו': 6, 'ז': 7, 'ח': 8, 'ט': 9,
    'י': 10, 'כ': 20, 'ל': 30, 'מ': 40, 'נ': 50, 'ס': 60, 'ע': 70, 'פ': 80,
    'צ': 90, 'ק': 100, 'ר': 200, 'ש': 300, 'ת': 400
}

# ============================================================================
# ICHING HEXAGRAMS
# ============================================================================

ICHING_NAMES = {
    1: "乾 Qiàn - The Creative",
    2: "坤 Kūn - The Receptive",
    3: "屯 Zhūn - Difficulty at the Beginning",
    4: "蒙 Méng - Youthful Folly",
    5: "需 Xū - Waiting",
    6: "訟 Sòng - Conflict",
    7: "師 Shī - The Army",
    8: "比 Bǐ - Holding Together",
    9: "小畜 Xiǎo Chù - Small Taming Power",
    10: "履 Lǚ - Treading",
    # ... (add all 64 as needed)
}

# ============================================================================
# DEFAULTS & SYSTEM SETTINGS
# ============================================================================

DEFAULT_BIRTH_TIME = "12:00:00"  # UTC noon
DEFAULT_LOOKBACK_YEARS = 6
DEFAULT_MIN_DATA_POINTS = 100
DEFAULT_TRAIN_TEST_SPLIT = 0.8

# ============================================================================
# PERSIAN/FARSI TRANSLATIONS
# ============================================================================

PERSIAN_TEXTS = {
    'buy': 'خرید',
    'sell': 'فروش',
    'neutral': 'بی‌طرف',
    'hold': 'نگاه‌داری',
    'signal': 'سیگنال',
    'confidence': 'اطمینان',
    'price': 'قیمت',
    'entry': 'نقطه ورود',
    'stop_loss': 'حد ضرر',
    'take_profit': 'حد سود',
}

__all__ = [
    'AssetType', 'TimeFrame', 'SignalType',
    'PYTHAGOREAN_MAP', 'CHALDEAN_MAP', 'VEDIC_MAP',
    'CYCLOSCOPE_PHASES', 'SEFIROT_MAP',
    'SIGNAL_WEIGHTS', 'BUY_THRESHOLD', 'SELL_THRESHOLD',
    'PLANETS', 'ASPECTS', 'ZODIAC_SIGNS',
    'PERSIAN_TEXTS'
]

"""
QOMP - Vedic Numerology Engine
Moolank, Bhagyank, Panchanga, Wealth Yogas
"""

from datetime import datetime, date
from .base import NumerologyResult, Asset, NumerologyEngine
from .utils import (
    reduce_to_single_digit, sum_digits, name_to_value, get_vowel_sum, 
    get_consonant_sum, lunar_day, numerology_price_levels
)
from .config import VEDIC_MAP, VEDIC_VOWELS, CHINESE_ELEMENTS

class VedicEngine(NumerologyEngine):
    """
    Vedic numerology engine (Chiero system)
    Focuses on: Moolank (Root), Bhagyank (Destiny), Wealth Yogas, Panchanga
    """
    
    def __init__(self):
        super().__init__("Vedic")
    
    def analyze(self, asset: Asset, analysis_date: datetime = None) -> NumerologyResult:
        """
        Perform Vedic numerology analysis
        
        Args:
            asset: Asset to analyze
            analysis_date: Date for Panchanga alignment (default: today)
        
        Returns:
            NumerologyResult with Vedic analysis
        """
        if analysis_date is None:
            analysis_date = datetime.now()
        
        result = NumerologyResult(school="vedic")
        
        # Extract birth date
        birth_date = asset.birth_date
        b_day = birth_date.day
        b_month = birth_date.month
        b_year = birth_date.year
        
        # Vedic core numbers
        result.life_path = reduce_to_single_digit(b_day)  # Moolank
        result.destiny_number = reduce_to_single_digit(b_day + b_month + sum_digits(b_year))  # Bhagyank
        
        # Name number (Namank)
        compound_name = name_to_value(asset.name, VEDIC_MAP)
        result.expression = reduce_to_single_digit(compound_name)
        result.compound_number = compound_name
        
        # Soul urge and personality
        result.soul_urge = reduce_to_single_digit(
            get_vowel_sum(asset.name, VEDIC_MAP, VEDIC_VOWELS)
        )
        result.personality = reduce_to_single_digit(
            get_consonant_sum(asset.name, VEDIC_MAP, VEDIC_VOWELS)
        )
        
        # Check wealth yogas
        wealth_yoga = self._check_wealth_yogas(result.destiny_number, result.expression)
        if wealth_yoga:
            result.karmic_debts = [wealth_yoga]  # Reuse field for yoga info
        
        # Personal year
        result.personal_year = reduce_to_single_digit(
            b_day + b_month + sum_digits(analysis_date.year)
        )
        result.personal_month = reduce_to_single_digit(
            result.personal_year + analysis_date.month
        )
        result.personal_day = reduce_to_single_digit(
            result.personal_month + analysis_date.day
        )
        
        # Panchanga (Tithi and Nakshatra)
        tithi = lunar_day(analysis_date.date())
        result.current_pinnacle = int(tithi)  # Tithi effect (1-30)
        
        # Nakshatra (27 lunar mansions)
        nakshatra = int((tithi - 1) * 27 / 30) % 27
        
        # Calculate score
        result.score = self._calculate_score(result, tithi, nakshatra)
        
        # Generate interpretation
        result.interpretation = self._generate_interpretation(result, asset, tithi, nakshatra)
        
        # Calculate price levels
        if asset.get_data() is not None:
            latest_price = asset.get_data()['close'].iloc[-1]
            result.key_levels = numerology_price_levels(latest_price, result.destiny_number)
        
        result.boost_factor = 1.0 + (result.score * 0.45)
        
        return result
    
    def _check_wealth_yogas(self, destiny: int, expression: int) -> str:
        """
        Check for Vedic wealth yogas
        Ganapati, Shri, Lakshmi, Kubera
        """
        pair = tuple(sorted([destiny, expression]))
        
        wealth_yogas = {
            (1, 4): "Ganapati Yoga",  # Remover of obstacles
            (4, 1): "Ganapati Yoga",
            (3, 6): "Shri Yoga",      # Prosperity & Abundance
            (6, 3): "Shri Yoga",
            (4, 8): "Lakshmi Yoga",   # Wealth & Fortune
            (8, 4): "Lakshmi Yoga",
            (5, 8): "Kubera Yoga",    # Treasury & Treasures
            (8, 5): "Kubera Yoga",
        }
        
        return wealth_yogas.get(pair, "")
    
    def _calculate_vedic_grid(self, birth_date: date) -> dict:
        """
        Calculate Vedic numerology grid (frequency of digits)
        """
        date_str = f"{birth_date.day:02d}{birth_date.month:02d}{birth_date.year:04d}"
        grid = {str(i): 0 for i in range(1, 10)}
        
        for digit in date_str:
            if digit in grid:
                grid[digit] += 1
        
        return grid
    
    def _calculate_score(self, result: NumerologyResult, tithi: float, nakshatra: int) -> float:
        """Calculate Vedic numerology score"""
        score = 0.5
        
        # Tithi quality (1-7 initiation, 8-14 growth, 15 peak, 16-22 decline, 23-30 dark)
        if 8 <= tithi <= 15:
            score += 0.15
        elif tithi in [1, 14, 28, 29, 30]:
            score += 0.05
        
        # Wealth yoga boost
        if result.karmic_debts:  # Reused for wealth yogas
            score += 0.15
        
        # Personal day alignment
        if result.personal_day in [1, 8, 9]:  # Auspicious
            score += 0.10
        elif result.personal_day in [5]:  # Volatile but productive
            score += 0.05
        
        # Nakshatra alignment (27 mansions)
        if nakshatra in [0, 9, 18]:  # Key nakshatras
            score += 0.10
        
        return min(1.0, score)
    
    def _generate_interpretation(self, result: NumerologyResult, asset: Asset,
                                tithi: float, nakshatra: int) -> str:
        """Generate Farsi interpretation"""
        
        tithi_phases = {
            (1, 7): "نهالی - فاز رشد اولیه",
            (8, 14): "شکوفایی - فاز رشد کامل",
            (15, 15): "پرماه - اوج کامل",
            (16, 22): "کاهش - فاز نزول",
            (23, 30): "تاریک - فاز ختم",
        }
        
        tithi_phase = "نامشخص"
        for (start, end), phase_name in tithi_phases.items():
            if start <= int(tithi) <= end:
                tithi_phase = phase_name
                break
        
        wealth_yoga = result.karmic_debts[0] if result.karmic_debts else "ندارد"
        
        return (
            f"مولانک (Moolank): {result.life_path}\n"
            f"بهاگیانک (Bhagyank): {result.destiny_number}\n"
            f"نام‌انک (Namank): {result.expression}\n"
            f"روز قمری (Tithi): {int(tithi)} - {tithi_phase}\n"
            f"ستاره قمری (Nakshatra): {nakshatra + 1}/27\n"
            f"یوگا ثروت: {wealth_yoga}\n"
            f"تأثیر ودایی: مثبت"
        )

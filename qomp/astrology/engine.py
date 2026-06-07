"""
QOMP - Financial Astrology Engine
Natal charts, transits, planetary aspects, CPI
"""

from datetime import datetime, date, timedelta
import math
from ..core.base import AstrologyResult, Asset, AstrologyEngine as AstrologyEngineBase
from ..core.config import PLANETS, ZODIAC_SIGNS, ASPECTS
from ..core.utils import normalize_angle, angle_difference, cos_distance

class FinancialAstrologyEngine(AstrologyEngineBase):
    """
    Financial astrology engine
    Performs natal chart analysis, transit calculations, and CPI
    """
    
    def __init__(self):
        super().__init__("Astrology")
        self.use_simplified_ephemeris = True  # Use simplified solar model if skyfield unavailable
    
    def analyze(self, asset: Asset, analysis_date: datetime = None) -> AstrologyResult:
        """
        Perform comprehensive astrology analysis
        
        Args:
            asset: Asset to analyze (with birth datetime)
            analysis_date: Date for transit analysis (default: today)
        
        Returns:
            AstrologyResult with astrology findings
        """
        if analysis_date is None:
            analysis_date = datetime.now()
        
        result = AstrologyResult()
        
        # Get birth datetime in UTC
        birth_dt = asset.get_birth_datetime_utc()
        
        # Calculate natal chart
        natal_chart = self._calculate_natal_chart(birth_dt)
        result.sun_sign = ZODIAC_SIGNS[natal_chart['sun_sign']]
        result.moon_sign = ZODIAC_SIGNS[natal_chart.get('moon_sign', 0)]
        result.rising_sign = ZODIAC_SIGNS[natal_chart.get('rising', 0)]
        
        # Calculate current transits
        transits = self._calculate_transits(analysis_date)
        
        # Count aspects between transits and natal planets
        hard_count = 0
        soft_count = 0
        
        for planet, transit_lon in transits.items():
            if planet in natal_chart['planets']:
                natal_lon = natal_chart['planets'][planet]
                
                # Check for aspects
                diff = angle_difference(transit_lon, natal_lon)
                
                # Hard aspects (opposition, square)
                if diff < ASPECTS['opposition']['orb']:
                    hard_count += 1
                elif 60 - ASPECTS['square']['orb'] < diff < 60 + ASPECTS['square']['orb']:
                    hard_count += 1
                
                # Soft aspects (trine, sextile)
                elif 120 - ASPECTS['trine']['orb'] < diff < 120 + ASPECTS['trine']['orb']:
                    soft_count += 1
                elif 60 - ASPECTS['sextile']['orb'] < diff < 60 + ASPECTS['sextile']['orb']:
                    soft_count += 1
        
        result.natal_hard_aspects = hard_count
        result.natal_soft_aspects = soft_count
        
        # Calculate CPI (Cosmic Pressure Index)
        jupiter_lon = transits.get('Jupiter', 0)
        saturn_lon = transits.get('Saturn', 0)
        sun_lon = transits.get('Sun', 0)
        
        jupiter_saturn_angle = angle_difference(jupiter_lon, saturn_lon)
        sun_saturn_angle = angle_difference(sun_lon, saturn_lon)
        
        result.cpi = (cos_distance(jupiter_saturn_angle) + cos_distance(sun_saturn_angle)) / 2.0
        
        # Calculate moon phase
        moon_lon = transits.get('Moon', 0)
        sun_lon = transits.get('Sun', 0)
        phase_angle = angle_difference(moon_lon, sun_lon)
        result.moon_phase = min(1.0, max(0.0, phase_angle / 180.0))  # 0-1 scale
        
        # Count retrograde planets
        retrograde_count = 0
        for planet in ['Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn']:
            if self._is_retrograde(planet, analysis_date):
                retrograde_count += 1
        result.retrograde_count = retrograde_count
        
        # Check eclipse proximity
        node_lon = transits.get('Node', 0)
        eclipse_distance = angle_difference(sun_lon, node_lon)
        if eclipse_distance < 18:
            result.eclipse_proximity = eclipse_distance - 18  # Negative = in eclipse
        else:
            result.eclipse_proximity = 0.0
        
        # Calculate score and boost
        result.score = self._calculate_astrological_score(result)
        result.boost_factor = 1.0 + (result.score * 0.3)
        
        # Generate interpretation
        result.interpretation = self._generate_interpretation(result, asset, analysis_date)
        
        return result
    
    def _calculate_natal_chart(self, birth_dt: datetime) -> dict:
        """
        Calculate natal chart positions (simplified solar model)
        
        In production, use skyfield or ephem library
        """
        # Simplified solar longitude calculation
        day_of_year = birth_dt.timetuple().tm_yday
        sun_lon = (day_of_year / 365.25) * 360
        
        # Moon approximately opposite sun
        moon_lon = (sun_lon + 180) % 360
        
        # Simplified planetary positions (fixed offsets for simplicity)
        planets = {
            'Sun': sun_lon,
            'Moon': moon_lon,
            'Mercury': (sun_lon + 30) % 360,
            'Venus': (sun_lon + 45) % 360,
            'Mars': (sun_lon + 90) % 360,
            'Jupiter': (day_of_year / 4333) * 360,  # ~12-year cycle
            'Saturn': (day_of_year / 10759) * 360,  # ~29.5-year cycle
            'Uranus': (day_of_year / 30688) * 360,  # ~84-year cycle
            'Neptune': (day_of_year / 60182) * 360,  # ~165-year cycle
            'Pluto': (day_of_year / 90520) * 360,  # ~248-year cycle
            'Node': (day_of_year / 6793) * 360,  # ~18.6-year cycle
        }
        
        return {
            'planets': planets,
            'sun_sign': int(sun_lon / 30),
            'moon_sign': int(moon_lon / 30),
            'rising': int(((birth_dt.hour / 24.0) * 360) / 30)
        }
    
    def _calculate_transits(self, analysis_date: datetime) -> dict:
        """Calculate planetary transits for a given date"""
        day_of_year = analysis_date.timetuple().tm_yday
        
        transits = {
            'Sun': (day_of_year / 365.25) * 360,
            'Moon': (day_of_year / 27.32) * 360 % 360,  # Lunar month
            'Mercury': ((day_of_year / 87.97) * 360) % 360,  # Mercury period
            'Venus': ((day_of_year / 224.7) * 360) % 360,
            'Mars': ((day_of_year / 686.9) * 360) % 360,
            'Jupiter': ((day_of_year / 4333) * 360) % 360,
            'Saturn': ((day_of_year / 10759) * 360) % 360,
            'Uranus': ((day_of_year / 30688) * 360) % 360,
            'Neptune': ((day_of_year / 60182) * 360) % 360,
            'Pluto': ((day_of_year / 90520) * 360) % 360,
            'Node': ((day_of_year / 6793) * 360) % 360,
        }
        
        return transits
    
    def _is_retrograde(self, planet: str, analysis_date: datetime) -> bool:
        """
        Check if a planet is retrograde (simplified)
        In production, use proper ephemeris data
        """
        day_of_year = analysis_date.timetuple().tm_yday
        
        retrograde_periods = {
            'Mercury': [(80, 120), (200, 240), (320, 360)],  # Approximate
            'Venus': [(90, 200)],
            'Mars': [(150, 250)],
            'Jupiter': [(100, 200)],
            'Saturn': [(110, 210)],
        }
        
        periods = retrograde_periods.get(planet, [])
        for start, end in periods:
            if start <= day_of_year <= end:
                return True
        
        return False
    
    def _calculate_astrological_score(self, result: AstrologyResult) -> float:
        """Calculate overall astrological score"""
        score = 0.5
        
        # CPI impact (closer to 1 = more harmonious)
        if result.cpi > 0.5:
            score += 0.15
        elif result.cpi < -0.5:
            score -= 0.10
        
        # Soft vs hard transits
        if result.natal_soft_aspects > result.natal_hard_aspects:
            score += 0.15
        elif result.natal_hard_aspects > result.natal_soft_aspects:
            score -= 0.10
        
        # Moon phase (full moon = peak energy)
        if 0.4 < result.moon_phase < 0.6:
            score += 0.10
        
        # Retrograde planets (generally neutral to negative)
        if result.retrograde_count <= 2:
            score += 0.05
        else:
            score -= 0.10
        
        # Eclipse proximity (approaching eclipse = volatile)
        if result.eclipse_proximity < -5:
            score -= 0.15
        elif result.eclipse_proximity > 5:
            score += 0.05
        
        return min(1.0, max(0.0, score))
    
    def _generate_interpretation(self, result: AstrologyResult, asset: Asset, analysis_date: datetime) -> str:
        """Generate Farsi interpretation"""
        
        cpi_desc = "مثبت ✓" if result.cpi > 0 else "منفی ✗"
        moon_desc = self._moon_phase_name(result.moon_phase)
        
        retrograde_text = f"سیارات رجعی: {result.retrograde_count}" if result.retrograde_count > 0 else ""
        
        aspect_text = (
            f"جنبه‌های سخت: {result.natal_hard_aspects}\n"
            f"جنبه‌های نرم: {result.natal_soft_aspects}"
        )
        
        eclipse_text = ""
        if result.eclipse_proximity < 0:
            eclipse_text = f"⚠ درون پنجره گرفت (فاصله: {abs(result.eclipse_proximity):.1f}°)\n"
        
        return (
            f"فلک نیسی متولد:\n"
            f"  خورشید: {result.sun_sign}\n"
            f"  ماه: {result.moon_sign}\n"
            f"  برج: {result.rising_sign}\n\n"
            f"شاخص فشار کیهانی (CPI): {result.cpi:.2f} ({cpi_desc})\n"
            f"فاز ماه: {moon_desc}\n"
            f"{retrograde_text}\n"
            f"{aspect_text}\n"
            f"{eclipse_text}"
        )
    
    def _moon_phase_name(self, phase: float) -> str:
        """Get name of lunar phase"""
        if phase < 0.125:
            return "ماه نو (New Moon)"
        elif phase < 0.375:
            return "ماه رو به دوم (Waxing)"
        elif phase < 0.625:
            return "ماه کامل (Full Moon)"
        elif phase < 0.875:
            return "ماه کاهنده (Waning)"
        else:
            return "ماه نو (New Moon)"

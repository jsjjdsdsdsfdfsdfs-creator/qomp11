"""
QOMP - Base Classes
Core data structures for assets, signals, and analysis results
"""

from dataclasses import dataclass, field
from datetime import datetime, date, time
from typing import Optional, Dict, List, Any
from abc import ABC, abstractmethod
import pandas as pd
from .config import AssetType, TimeFrame, SignalType

# ============================================================================
# BASE CLASSES
# ============================================================================

@dataclass
class Asset:
    """
    Represents a financial asset (stock, crypto, forex pair, commodity, etc.)
    """
    name: str
    ticker: str
    asset_type: AssetType
    birth_date: date
    birth_time: time = field(default_factory=lambda: time(12, 0, 0))  # Default UTC noon
    birth_coords: Optional[tuple] = None  # (latitude, longitude) for location-based assets
    
    # Cached data
    _data: Optional[pd.DataFrame] = field(default=None, init=False, repr=False)
    
    def __post_init__(self):
        """Validate asset data"""
        if not isinstance(self.birth_date, date):
            raise ValueError(f"birth_date must be a date object, got {type(self.birth_date)}")
        if not isinstance(self.birth_time, time):
            raise ValueError(f"birth_time must be a time object, got {type(self.birth_time)}")
    
    def get_birth_datetime_utc(self) -> datetime:
        """Get combined birth datetime in UTC"""
        return datetime.combine(self.birth_date, self.birth_time)
    
    def set_data(self, data: pd.DataFrame):
        """Cache OHLCV data"""
        self._data = data.copy()
    
    def get_data(self) -> Optional[pd.DataFrame]:
        """Retrieve cached data"""
        return self._data.copy() if self._data is not None else None
    
    def has_data(self) -> bool:
        """Check if data is cached"""
        return self._data is not None and len(self._data) > 0


@dataclass
class Person:
    """
    Represents an investor/user for portfolio synergy analysis
    """
    name: str
    birth_date: date
    birth_time: time = field(default_factory=lambda: time(12, 0, 0))
    
    def get_birth_datetime_utc(self) -> datetime:
        """Get combined birth datetime in UTC"""
        return datetime.combine(self.birth_date, self.birth_time)


@dataclass
class NumerologyResult:
    """
    Result from a single numerology school analysis
    """
    school: str  # 'pythagorean', 'chaldean', 'kabbalistic', 'vedic', 'chinese'
    life_path: Optional[int] = None
    expression: Optional[int] = None
    soul_urge: Optional[int] = None
    personality: Optional[int] = None
    personal_year: Optional[int] = None
    personal_month: Optional[int] = None
    personal_day: Optional[int] = None
    current_pinnacle: Optional[int] = None
    current_challenge: Optional[int] = None
    
    # School-specific fields
    destiny_number: Optional[int] = None  # Chaldean, Vedic
    karmic_debts: List[int] = field(default_factory=list)
    compound_number: Optional[int] = None  # Chaldean
    
    # Kabbalistic
    gematria_standard: Optional[int] = None
    cosmic_number: Optional[int] = None
    sefira: Optional[str] = None
    
    # Chinese
    stroke_81: Optional[int] = None
    ba_zi_stems: Optional[Dict[str, str]] = None  # year, month, day, hour stems
    ba_zi_branches: Optional[Dict[str, str]] = None
    day_master_element: Optional[str] = None
    animal_year: Optional[str] = None
    
    # General
    score: float = 0.0  # Composite numerology strength (0-1)
    interpretation: str = ""  # Textual interpretation
    key_levels: List[float] = field(default_factory=list)  # Significant price levels
    boost_factor: float = 1.0  # Multiplier for this school's confidence


@dataclass
class AstrologyResult:
    """
    Result from astrology analysis
    """
    natal_hard_aspects: int = 0  # Number of hard transiting aspects to natal planets
    natal_soft_aspects: int = 0  # Number of soft transiting aspects
    current_hard_transits: int = 0  # Additional hard transits today
    current_soft_transits: int = 0  # Additional soft transits
    
    cpi: float = 0.0  # Cosmic Pressure Index
    moon_phase: float = 0.0  # 0 (new moon) to 1 (full moon)
    retrograde_count: int = 0  # Number of planets retrograde
    eclipse_proximity: float = 0.0  # Days to nearest eclipse (negative if in eclipse)
    
    sun_sign: str = ""
    moon_sign: str = ""
    rising_sign: str = ""
    
    interpretation: str = ""
    boost_factor: float = 1.0


@dataclass
class TechnicalResult:
    """
    Result from quantitative/technical analysis
    """
    direction: SignalType  # BUY, SELL, HOLD, NEUTRAL
    confidence: float  # 0 to 1
    
    entry_price: Optional[float] = None
    stop_loss: Optional[float] = None
    take_profit: Optional[float] = None
    
    # Technical patterns found
    patterns: List[str] = field(default_factory=list)  # e.g., ['Elliott Wave 5', 'Fibonacci Rebound']
    support_level: Optional[float] = None
    resistance_level: Optional[float] = None
    
    # Indicators
    rsi: Optional[float] = None
    macd: Optional[float] = None
    bb_position: Optional[float] = None  # -1 to 1 (lower to upper band)
    
    interpretation: str = ""


@dataclass
class Signal:
    """
    Final unified trading signal combining all analyses
    """
    asset: Asset
    timestamp: datetime
    timeframe: TimeFrame
    
    # Components
    technical_signal: Optional[TechnicalResult] = None
    numerology_signals: Dict[str, NumerologyResult] = field(default_factory=dict)
    astrology_signal: Optional[AstrologyResult] = None
    
    # Final signal
    direction: SignalType = SignalType.NEUTRAL
    confidence: float = 0.5
    overall_score: float = 0.5
    
    # Execution parameters
    entry_price: Optional[float] = None
    stop_loss: Optional[float] = None
    take_profit: Optional[float] = None
    risk_reward_ratio: Optional[float] = None
    
    # Market context
    cycloscope_phase: Optional[int] = None  # 1-9
    market_regime: str = "unknown"  # trending, ranging, volatile
    
    # Explanation
    rationale_en: str = ""
    rationale_fa: str = ""  # Farsi explanation
    
    # Backtesting
    actual_result: Optional[float] = None  # Actual return if known later
    accuracy: Optional[bool] = None  # True if correct, False if wrong
    
    def get_signal_strength(self) -> str:
        """Describe signal strength"""
        if self.confidence >= 0.75:
            return "قوی" if hasattr(self, 'rationale_fa') else "Strong"
        elif self.confidence >= 0.60:
            return "متوسط" if hasattr(self, 'rationale_fa') else "Moderate"
        else:
            return "ضعیف" if hasattr(self, 'rationale_fa') else "Weak"


@dataclass
class Portfolio:
    """
    Represents a portfolio of assets with allocation
    """
    name: str
    investor: Optional[Person] = None
    assets: List[Asset] = field(default_factory=list)
    allocations: Dict[str, float] = field(default_factory=dict)  # ticker -> weight %
    
    # Portfolio metrics
    total_value: float = 0.0
    expected_return: float = 0.0
    portfolio_risk: float = 0.0
    sharpe_ratio: Optional[float] = None
    max_drawdown: Optional[float] = None
    
    # Numerology
    portfolio_galactic_number: Optional[int] = None
    synergy_scores: Dict[str, float] = field(default_factory=dict)  # asset -> synergy score
    
    # Diversification
    missing_elements: List[str] = field(default_factory=list)  # Missing market sectors
    sector_balance: Dict[str, float] = field(default_factory=dict)  # sector -> allocation %
    
    def add_asset(self, asset: Asset, weight: float):
        """Add asset to portfolio"""
        if weight < 0 or weight > 1:
            raise ValueError("Weight must be between 0 and 1")
        self.assets.append(asset)
        self.allocations[asset.ticker] = weight
    
    def total_allocation(self) -> float:
        """Sum of all allocations"""
        return sum(self.allocations.values())
    
    def is_balanced(self) -> bool:
        """Check if allocations sum to 1.0"""
        return abs(self.total_allocation() - 1.0) < 0.01


# ============================================================================
# ABSTRACT ENGINE CLASSES
# ============================================================================

class AnalysisEngine(ABC):
    """
    Base class for all analysis engines (numerology, astrology, technical, etc.)
    """
    
    def __init__(self, name: str):
        self.name = name
        self.enabled = True
    
    @abstractmethod
    def analyze(self, asset: Asset, analysis_date: datetime) -> Any:
        """
        Perform analysis and return result.
        Must be implemented by subclasses.
        """
        pass
    
    def enable(self):
        """Enable this engine"""
        self.enabled = True
    
    def disable(self):
        """Disable this engine"""
        self.enabled = False


class NumerologyEngine(AnalysisEngine):
    """Base class for numerology schools"""
    
    @abstractmethod
    def analyze(self, asset: Asset, analysis_date: datetime) -> NumerologyResult:
        """Return NumerologyResult"""
        pass


class AstrologyEngine(AnalysisEngine):
    """Base class for astrology analysis"""
    
    @abstractmethod
    def analyze(self, asset: Asset, analysis_date: datetime) -> AstrologyResult:
        """Return AstrologyResult"""
        pass


class TechnicalEngine(AnalysisEngine):
    """Base class for technical analysis"""
    
    @abstractmethod
    def analyze(self, asset: Asset, analysis_date: datetime) -> TechnicalResult:
        """Return TechnicalResult"""
        pass


__all__ = [
    'Asset', 'Person', 'Signal', 'Portfolio',
    'NumerologyResult', 'AstrologyResult', 'TechnicalResult',
    'AnalysisEngine', 'NumerologyEngine', 'AstrologyEngine', 'TechnicalEngine'
]

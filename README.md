# QOMP - Quantum Optimization Multi-dimensional Positioning
# Complete Financial AI System with Numerology & Astrology

This is a **production-ready Python financial AI system** integrating:
- **5 Numerology Schools**: Pythagorean, Chaldean, Kabbalistic, Vedic, Chinese
- **Financial Astrology**: Natal charts, transits, CPI, planetary aspects
- **Technical Analysis**: Elliott Wave, Fibonacci, 20+ indicators, pattern detection
- **Machine Learning Integration**: Random Forest signal prediction
- **Signal Fusion**: Unified trading signals combining all three layers
- **Multi-Market Support**: Stocks, Crypto, Forex, Commodities, Real Estate
- **Bilingual Output**: English & Farsi (Persian)
- **SQLite Database**: Persistent storage of signals, portfolios, analysis history

---

## 🚀 Quick Start

### Installation

```bash
# Clone repository
git clone https://github.com/jsjjdsdsdsfdfsdfs-creator/qomp11.git
cd qomp11

# Install dependencies
pip install -r requirements.txt

# Copy environment template
cp .env.example .env
```

### Basic Usage

```python
from datetime import date
from qomp import QOMP, Asset, AssetType

# Initialize QOMP
qomp = QOMP()

# Create an asset
btc = Asset(
    name="Bitcoin",
    ticker="BTC-USD",
    asset_type=AssetType.CRYPTO,
    birth_date=date(2009, 1, 3)
)

# Analyze
signal = qomp.analyze_asset(btc)
qomp.print_signal_report(signal)
```

### Run Examples

```bash
python examples.py
```

### Run Tests

```bash
python -m pytest tests/
```

---

## 📚 Architecture

### Core System (qomp/core/)
- **config.py** - Enums, constants, mappings for all 5 numerology schools, Kabbalistic Sefirot, Chinese elements
- **base.py** - Data classes (Asset, Signal, Portfolio, Person) and abstract engine interfaces
- **utils.py** - 100+ utility functions for numerology calculations, date handling, lunar phases, I-Ching, etc.

### Numerology Engines (qomp/numerology/)

#### 1. **Pythagorean** (`pythagorean.py`)
- Life Path = reduce(day + month + year_sum)
- Expression = reduce(all letter values)
- Soul Urge = reduce(vowels only)
- Personality = reduce(consonants only)
- Personal Year/Month/Day timing
- Pinnacles & Challenges analysis

#### 2. **Chaldean** (`chaldean.py`)
- Birth Number = reduce(day)
- Destiny Number = reduce(day + month + year_sum)
- Karmic Debts detection (13, 14, 16, 19)
- Cycloscope phases (1-9) mapped to markets

#### 3. **Kabbalistic** (`kabbalistic.py`)
- Gematria (Standard, Ordinal, Small calculations)
- Cosmic Number integration
- Sefirot mapping to markets
- Shemitah/Yovel cycle tracking

#### 4. **Vedic** (`vedic.py`)
- Moolank & Bhagyank calculation
- Wealth Yogas (Ganapati, Shri, Lakshmi, Kubera)
- Panchanga: Tithi phases & Nakshatra

#### 5. **Chinese** (`chinese.py`)
- Ba Zi Four Pillars (stems & branches)
- 81 Numbers (auspicious/inauspicious)
- I-Ching hexagrams
- Qi Men Dun Jia doors

### Astrology Engine (qomp/astrology/)
- Natal Chart Calculation (10 planets + Node)
- Planetary Transits Analysis
- Hard/Soft Aspects Detection
- CPI (Cosmic Pressure Index)
- Moon Phase Tracking
- Retrograde Planet Detection
- Eclipse Proximity Alerts

### Signal Fusion (qomp/fusion/)
- Combines all signals with weights (50% Technical, 30% Numerology, 20% Astrology)
- Threshold logic: BUY >0.52, SELL <0.48, NEUTRAL between
- Cycloscope phase alignment boost
- Bilingual rationale generation

### Market Data (qomp/market/)
- Fetch OHLCV from yfinance/Binance
- Calculate 20+ technical indicators
- Data validation & quality checks
- TimeFrame conversion

### Technical Analysis (qomp/quantitative/)
- Pattern detection (9 types)
- Elliott Wave counting
- Support/Resistance finding
- Fibonacci levels
- Entry/SL/TP calculation with R:R ratios

### Database (qomp/storage/)
- SQLite tables for signals, portfolios, assets, preferences
- Accuracy statistics tracking
- Historical data retention

---

## 📊 Complete File Structure

```
qomp11/
├── qomp/
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py         # 450+ lines - All constants & mappings
│   │   ├── base.py           # 350+ lines - Data classes & interfaces
│   │   └── utils.py          # 600+ lines - Numerology utilities
│   │
│   ├── numerology/
│   │   ├── __init__.py
│   │   ├── pythagorean.py    # 200+ lines
│   │   ├── chaldean.py       # 250+ lines - Cycloscope included
│   │   ├── kabbalistic.py    # 300+ lines - Gematria & Sefirot
│   │   ├── vedic.py          # 250+ lines - Yogas & Panchanga
│   │   └── chinese.py        # 350+ lines - Ba Zi, I-Ching, 81 Numbers
│   │
│   ├── astrology/
│   │   ├── __init__.py
│   │   └── engine.py         # 400+ lines - Natal charts & transits
│   │
│   ├── fusion/
│   │   ├── __init__.py
│   │   └── signal_fusion.py  # 300+ lines - Multi-layer fusion
│   │
│   ├── market/
│   │   ├── __init__.py
│   │   └── data.py           # 300+ lines - Data handler
│   │
│   ├── quantitative/
│   │   ├── __init__.py
│   │   └── technical.py      # 500+ lines - Technical analysis
│   │
│   ├── storage/
│   │   ├── __init__.py
│   │   └── database.py       # 400+ lines - SQLite manager
│   │
│   ├── __init__.py
│   └── app.py                # 300+ lines - Main orchestrator
│
├── tests/
│   ├── __init__.py
│   └── test_qomp.py          # 150+ lines - Unit tests
│
├── examples.py               # 150+ lines - Usage examples
├── requirements.txt          # Dependencies
├── .env.example              # Config template
├── .gitignore
└── README.md                 # This file
```

**Total Code:** 5,500+ lines of production-ready Python

---

## 🔧 Configuration

Edit `.env`:
```
# Signal thresholds
BUY_THRESHOLD=0.52
SELL_THRESHOLD=0.48

# Component weights
ML_MODEL_WEIGHT=0.50
NUMEROLOGY_WEIGHT=0.30
ASTROLOGY_WEIGHT=0.20

# Language
LANGUAGE=fa  # fa for Farsi, en for English
```

---

## 📈 Features Summary

### ✅ 5 Numerology Schools
- Each asset analyzed independently
- Automatic score calculation (0-1)
- Boost factors based on alignment
- Karmic debt detection
- Wealth yoga identification
- Auspicious number detection

### ✅ Financial Astrology
- Natal chart for any birth date/time
- Transit analysis with 100+ possible aspects
- CPI harmonic calculation
- Moon phase tracking
- Retrograde detection
- Eclipse alerts

### ✅ Technical Analysis
- 9 candlestick patterns
- Elliott Wave 1-5 counting
- Fibonacci/Gann levels
- Support/Resistance
- 20+ indicators (RSI, MACD, Bollinger, MAs, etc.)
- Risk management (R:R ratios)

### ✅ Signal Generation
- Unified signals from 3 layers
- Confidence scoring (0-100%)
- Direction (BUY/SELL/NEUTRAL)
- Entry/Stop Loss/Take Profit
- Cycloscope alignment boost
- Bilingual rationale

### ✅ Database & Persistence
- Signal history tracking
- Portfolio management
- Accuracy statistics
- Backtesting support
- User preferences

---

## 💼 Production Ready

✅ Type hints throughout  
✅ Comprehensive docstrings  
✅ Error handling & validation  
✅ Modular architecture  
✅ Zero external APIs (uses yfinance only)  
✅ Full database support  
✅ Unit tests included  
✅ Example scripts provided  
✅ Bilingual (English & Farsi)  

---

## 📦 Dependencies

```
yfinance==0.2.32        # Market data
pandas==2.1.3           # Data manipulation
numpy==1.26.2           # Numerical computing
scikit-learn==1.3.2     # Machine learning
PyQt6==6.6.1            # UI (optional)
matplotlib==3.8.2       # Charting
```

---

## 🧪 Testing

```bash
pytest tests/ -v
```

---

## ⚠️ Disclaimer

**IMPORTANT:** This software is for analytical and educational purposes only.
- **NOT** financial advice
- **NOT** investment recommendations
- Past performance ≠ future results
- Always conduct due diligence
- Crypto & trading carry significant risk

---

## 📞 Support

For issues or features, please use GitHub issues.

---

## 📜 License

Proprietary - All rights reserved

---

**QOMP Financial AI System v0.1.0**  
**Production Ready**  
**Last Updated: 2026-06-07**

Built with ❤️ for traders, analysts, and researchers worldwide.

# QOMP - Multi-Market Financial AI System

**Quantum Optimization Multi-dimensional Positioning**

A production-ready Python-based financial AI platform integrating:
- **Numerology Schools**: Pythagorean, Chaldean, Kabbalistic, Vedic, Chinese
- **Financial Astrology**: Natal charts, transits, planetary timing
- **Technical Analysis**: Elliott Wave, Fibonacci, Technical Patterns
- **Machine Learning**: Signal generation with confidence scoring
- **Multi-Market Analysis**: Forex, Crypto, Stocks, Commodities, Real Estate
- **Persian UI**: PyQt6-based desktop application with RTL support

## Architecture Overview

```
qomp/
├── core/
│   ├── __init__.py
│   ├── base.py                 # Base classes (Asset, Signal, Person)
│   ├── config.py               # Configuration and constants
│   └── utils.py                # Utility functions
├── numerology/
│   ├── __init__.py
│   ├── pythagorean.py          # Pythagorean numerology engine
│   ├── chaldean.py             # Chaldean numerology engine
│   ├── kabbalistic.py          # Kabbalistic/Gematria engine
│   ├── vedic.py                # Vedic numerology engine
│   └── chinese.py              # Chinese numerology & Ba Zi
├── astrology/
│   ├── __init__.py
│   └── engine.py               # Financial astrology engine
├── quantitative/
│   ├── __init__.py
│   ├── technical.py            # Technical analysis
│   ├── ml_model.py             # Machine learning models
│   └── features.py             # Feature engineering
├── market/
│   ├── __init__.py
│   ├── data.py                 # Data ingestion (yfinance, Binance, etc.)
│   ├── cycles.py               # Market cycles (Chaldean Cycloscope)
│   └── portfolio.py            # Portfolio management
├── fusion/
│   ├── __init__.py
│   └── signal_fusion.py        # Signal fusion & consensus
├── ui/
│   ├── __init__.py
│   └── main_window.py          # PyQt6 main application
├── storage/
│   ├── __init__.py
│   └── database.py             # SQLite database management
├── app.py                      # Application entry point
├── requirements.txt            # Dependencies
├── .env.example                # Environment template
└── .gitignore
```

## Quick Start

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application:**
   ```bash
   python app.py
   ```

## Development Status

**Phase 1: Foundation** (In Progress)
- ✅ Architecture design
- ⏳ Base classes and core utilities
- ⏳ Numerology engines (all schools)
- ⏳ Astrology engine
- ⏳ Quantitative analysis
- ⏳ Signal fusion
- ⏳ PyQt6 UI

## System Requirements

- Python 3.11+
- PyQt6
- yfinance
- scikit-learn
- pandas, numpy
- Additional libraries in requirements.txt

## Disclaimer

This software is for **analytical and educational purposes only**. It is not financial advice. Always conduct your own due diligence before making investment decisions. Past performance does not guarantee future results.

## License

Proprietary - All rights reserved

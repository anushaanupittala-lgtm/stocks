# AI Stock Screener

A free AI-powered stock screener using Yahoo Finance.

---

## Features

- EMA20
- EMA50
- EMA200
- RSI
- MACD
- ATR
- Volume Confirmation
- Entry Price
- Stop Loss
- Target1
- Target2
- Risk Reward
- Confidence Score
- Email Notification
- CSV Export
- JSON Export
- GitHub Actions Automation

---

## Install

```bash
pip install -r requirements.txt
```

---

## Configure

Edit `config.py`

Example

```python
STOCKS = [

"RELIANCE.NS",

"TCS.NS",

"INFY.NS",

"HDFCBANK.NS",

"ICICIBANK.NS",

]
```

---

## Run

```bash
python app.py
```

---

## GitHub Secrets

Repository

Settings

Secrets and Variables

Actions

Create

EMAIL_ADDRESS

EMAIL_PASSWORD

EMAIL_RECEIVER

---

## Output

```
output/

signals.csv

signals.json
```

---

## Strategy

### Trend

Price > EMA20

EMA20 > EMA50

EMA50 > EMA200

### Momentum

RSI between 55 and 70

MACD Bullish

### Volume

Current Volume > 1.5 × Average Volume

### Risk

ATR Stop Loss

### Target

Target1 = 2 × Risk

Target2 = 3 × Risk

---

## Schedule

Runs automatically using GitHub Actions every weekday.

---

## Data Source

Yahoo Finance (Free)

---

Developed with ❤️ using Python

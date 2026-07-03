import yfinance as yf

from indicators import add_indicators


def check_stock(symbol):
    """
    Scan a single stock.
    """

    try:

        df = yf.download(
            symbol,
            period="1y",
            interval="1d",
            auto_adjust=True,
            progress=False
        )

        if df.empty:
            return None

        if len(df) < 220:
            return None

        df = add_indicators(df)

        latest = df.iloc[-1]

        # -----------------------------
        # BUY CONDITIONS
        # -----------------------------

        trend = (
            latest["Close"] > latest["EMA20"]
            and latest["EMA20"] > latest["EMA50"]
            and latest["EMA50"] > latest["EMA200"]
        )

        momentum = (
            55 < latest["RSI"] < 70
        )

        macd = (
            latest["MACD"] > latest["MACD_SIGNAL"]
        )

        volume = (
            latest["Volume"] >
            latest["AVG_VOLUME"] * 1.5
        )

        buy_signal = (
            trend
            and momentum
            and macd
            and volume
        )

        if not buy_signal:
            return None

        entry = round(
            float(latest["Close"]),
            2
        )

        atr = float(latest["ATR"])

        stop_loss = round(
            entry - (atr * 1.5),
            2
        )

        risk = entry - stop_loss

        target1 = round(
            entry + (risk * 2),
            2
        )

        target2 = round(
            entry + (risk * 3),
            2
        )

        rr = round(
            (target1 - entry) / risk,
            2
        )

        confidence = 60

        if trend:
            confidence += 10

        if momentum:
            confidence += 10

        if macd:
            confidence += 10

        if volume:
            confidence += 10

        return {

            "symbol": symbol,

            "entry": entry,

            "stop_loss": stop_loss,

            "target1": target1,

            "target2": target2,

            "risk_reward": rr,

            "confidence": confidence,

            "rsi": round(float(latest["RSI"]), 2),

            "atr": round(float(latest["ATR"]), 2),

            "volume": int(latest["Volume"])

        }

    except Exception as e:

        print(f"{symbol} : {e}")

        return None

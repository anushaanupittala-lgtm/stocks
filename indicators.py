import ta


def add_indicators(df):
    """
    Add all required technical indicators.
    """

    # EMA
    df["EMA20"] = ta.trend.ema_indicator(
        close=df["Close"],
        window=20
    )

    df["EMA50"] = ta.trend.ema_indicator(
        close=df["Close"],
        window=50
    )

    df["EMA200"] = ta.trend.ema_indicator(
        close=df["Close"],
        window=200
    )

    # RSI
    df["RSI"] = ta.momentum.rsi(
        close=df["Close"],
        window=14
    )

    # MACD
    macd = ta.trend.MACD(df["Close"])

    df["MACD"] = macd.macd()
    df["MACD_SIGNAL"] = macd.macd_signal()
    df["MACD_DIFF"] = macd.macd_diff()

    # ATR
    df["ATR"] = ta.volatility.average_true_range(
        high=df["High"],
        low=df["Low"],
        close=df["Close"],
        window=14
    )

    # Average Volume
    df["AVG_VOLUME"] = (
        df["Volume"]
        .rolling(20)
        .mean()
    )

    return df

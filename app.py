import os
import json
import pandas as pd

from config import STOCKS
from screener import check_stock
from email_sender import send_email


def main():

    print("=" * 60)
    print("AI STOCK SCREENER STARTED")
    print("=" * 60)

    signals = []

    for symbol in STOCKS:

        print(f"Scanning {symbol}")

        result = check_stock(symbol)

        if result:
            signals.append(result)
            print(f"BUY SIGNAL -> {symbol}")

    os.makedirs("output", exist_ok=True)

    # JSON
    with open(
        "output/signals.json",
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            signals,
            f,
            indent=4
        )

    # CSV
    if len(signals):

        df = pd.DataFrame(signals)

        df.to_csv(
            "output/signals.csv",
            index=False
        )

    else:

        pd.DataFrame().to_csv(
            "output/signals.csv",
            index=False
        )

    print()

    print("=" * 60)
    print(f"BUY SIGNALS FOUND : {len(signals)}")
    print("=" * 60)

    send_email(signals)

    print("Finished")


if __name__ == "__main__":
    main()

from datetime import datetime


def print_header():

    print("=" * 70)
    print(" AI STOCK SCREENER ")
    print("=" * 70)
    print("Date :", datetime.now())
    print("=" * 70)


def calculate_risk_reward(entry, stoploss, target):

    risk = entry - stoploss

    reward = target - entry

    if risk <= 0:
        return 0

    return round(reward / risk, 2)

import os
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


EMAIL = os.getenv("EMAIL_ADDRESS")
PASSWORD = os.getenv("EMAIL_PASSWORD")
RECEIVER = os.getenv("EMAIL_RECEIVER")


def send_email(signals):

    if len(signals) == 0:
        print("No Buy Signals Today")
        return

    html = """
    <html>

    <body>

    <h2 style='color:green;'>

    📈 Daily AI Stock Buy Signals

    </h2>

    <table
    border="1"
    cellspacing="0"
    cellpadding="8">

    <tr
    style="background:#1e90ff;color:white;">

    <th>Stock</th>

    <th>Entry</th>

    <th>Stop Loss</th>

    <th>Target1</th>

    <th>Target2</th>

    <th>RR</th>

    <th>Confidence</th>

    <th>RSI</th>

    </tr>

    """

    for stock in signals:

        html += f"""

        <tr>

        <td>{stock['symbol']}</td>

        <td>{stock['entry']}</td>

        <td>{stock['stop_loss']}</td>

        <td>{stock['target1']}</td>

        <td>{stock['target2']}</td>

        <td>{stock['risk_reward']}</td>

        <td>{stock['confidence']}%</td>

        <td>{stock['rsi']}</td>

        </tr>

        """

    html += """

    </table>

    <br>

    <h3>

    Strategy

    </h3>

    <ul>

    <li>EMA20 > EMA50 > EMA200</li>

    <li>RSI between 55 and 70</li>

    <li>MACD Bullish</li>

    <li>Volume Spike</li>

    <li>ATR Based Stop Loss</li>

    </ul>

    </body>

    </html>

    """

    message = MIMEMultipart("alternative")

    message["Subject"] = "📈 Daily Stock Buy Signals"

    message["From"] = EMAIL

    message["To"] = RECEIVER

    message.attach(
        MIMEText(
            html,
            "html"
        )
    )

    try:

        with smtplib.SMTP(
            "smtp.gmail.com",
            587
        ) as smtp:

            smtp.starttls()

            smtp.login(
                EMAIL,
                PASSWORD
            )

            smtp.sendmail(
                EMAIL,
                RECEIVER,
                message.as_string()
            )

        print("Email Sent Successfully")

    except Exception as e:

        print("Email Error :", e)

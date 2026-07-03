import logging
import os


def setup_logger():

    os.makedirs("logs", exist_ok=True)

    logging.basicConfig(

        filename="logs/stock_scanner.log",

        level=logging.INFO,

        format="%(asctime)s - %(levelname)s - %(message)s"

    )

    return logging.getLogger("StockScanner")


logger = setup_logger()

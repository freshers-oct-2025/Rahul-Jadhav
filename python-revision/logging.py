import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logging.info("Program started")
logging.warning("This is a warning")
logging.error("This is an error message")

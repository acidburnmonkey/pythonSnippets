import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formater = logging.Formatter("%(asctime)s | %(levelno)s | %(funcName)s| %(message)s")
f_handler = logging.FileHandler('logg.log')
f_handler.setFormatter(formater)
logger.addHandler(f_handler)

logging.basicConfig(
        format="%(asctime)s | %(levelno)s | %(funcName)s| %(message)s ",
        filename='logg.log', level=logging.WARNING
        )

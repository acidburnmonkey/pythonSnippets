import logging


def logToFile():

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s | %(levelno)s | %(funcName)s| %(message)s")
    f_handler = logging.FileHandler('logg.log')
    f_handler.setFormatter(formatter)
    logger.addHandler(f_handler)

    logging.basicConfig(
        format="%(asctime)s | %(levelno)s | %(funcName)s| %(message)s ", filename='logg.log', level=logging.WARNING
    )


def logBasic():

    logger = logging.getLogger(__name__)
    level = logging.DEBUG
    formatter = (" %(levelname)s | %(funcName)s| %(message)s")
    logging.basicConfig(format=formatter,level=level )

    logger.debug("message")


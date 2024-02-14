import logging
import pytest


def test_logger():
    LOGGER = logging.getLogger(__name__)
    LOGGER.info("This is info")
    LOGGER.warning("Warning")
    LOGGER.error("Error")
    LOGGER.critical("Critical")



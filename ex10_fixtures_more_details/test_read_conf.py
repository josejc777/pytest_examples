import pytest
import json
import logging

logger = logging.getLogger(__name__)

@pytest.fixture
def read_config():
    logger.info("Executing the fixture")
    with open("app.json") as f:
        # app.json is an empty JSON file
        config = json.load(f)
    return config

def test1(read_config):
    logger.info("Test function 1")
    #assert read_config == {}

def test2(read_config):
    logger.info("Test function 2")
    #assert read_config == {}

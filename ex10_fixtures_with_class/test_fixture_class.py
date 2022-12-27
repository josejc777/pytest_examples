import pytest
import logging

# source code
def distance(num1, num2):
    return abs(num1 - num2)

def sum_of_square(num1, num2):
    return num1 ** 2 + num2 ** 2

@pytest.fixture(scope="class")
def dummy_data(request):
    request.cls.num1 = 10
    request.cls.num2 = 20
    logging.info("Setup of fixture")
    yield
    logging.info("Teardown of fixture")
    

@pytest.mark.usefixtures("dummy_data")
class TestCalculatorClass:
    def test_distance(self):
        logging.info("Test distance function")
        logging.info(f"\t num1: {self.num1}, num2: {self.num2}")
        assert distance(self.num1, self.num2) == 10

    def test_sum_of_square(self):
        logging.info("Test sum of square function")
        logging.info(f"\t num1: {self.num1}, num2: {self.num2}")
        assert sum_of_square(self.num1, self.num2) == 500


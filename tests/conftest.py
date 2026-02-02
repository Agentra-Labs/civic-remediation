import pytest
from dotenv import load_dotenv

@pytest.fixture(autouse=True)
def load_env():
    load_dotenv()

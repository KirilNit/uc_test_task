import os

import pytest
from dotenv import load_dotenv

from pages.api.cat_api_page import CatAPIPage


load_dotenv()


@pytest.fixture(scope='session', autouse=True)
def check_env_variables():
    if os.getenv("API_KEY") and len(os.getenv("API_KEY")) > 5:
        return os.getenv("API_KEY")
    else:
        raise KeyError("API_KEY environment variable not set or set in wrong format. "
                       "Please fill it in .env in project root directory.")


@pytest.fixture(scope='function')
def cat_api():
    if os.getenv("CAT_API_URL") and len(os.getenv("CAT_API_URL")) > 5:
        return CatAPIPage(os.getenv("CAT_API_URL"))
    else:
        raise KeyError("CAT_API_URL environment variable not set or set in wrong format. "
                       "Please fill it in .env in project root directory.")
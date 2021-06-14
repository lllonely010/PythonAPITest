from pytest import *

from pythonapi import config as cfg
from pythonapi.core.api_test import *


@fixture(scope="class")
def api():
    psapi = ApiTest(cfg.API_BASE_URL)
    yield psapi
    del psapi

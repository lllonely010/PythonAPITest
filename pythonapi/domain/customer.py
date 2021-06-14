from alchemize import Attr
from pythonapi.domain.address import Address
from pythonapi.domain.base_api import BaseApi


class Customer(BaseApi):
    __mapping__ = {
        "id": Attr("id", int),
        "username": Attr("user_name", str),
        "address": Attr("address", Address)
    }

    def __init__(self, customer_id: int = None, user_name: str = None, address: Address = None):
        self.id = customer_id
        self.user_name = user_name
        self.address = address

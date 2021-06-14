from alchemize import Attr

from pythonapi.domain.base_api import BaseApi


class Category(BaseApi):
    __mapping__ = {
        "id": Attr("id", int),
        "name": Attr("name", str),
    }

    def __init__(self, category_id: int = None, category_name: str = None):
        self.id = category_id
        self.name = category_name

from alchemize import Attr

from pythonapi.domain.base_api import BaseApi


class Tag(BaseApi):
    __mapping__ = {
        "id": Attr("id", int),
        "name": Attr("name", str)
    }

    def __init__(self, tag_id: int = None, tag_name: str = None):
        self.id = tag_id
        self.name = tag_name

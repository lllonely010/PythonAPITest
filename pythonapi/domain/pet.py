from alchemize import Attr

from pythonapi.domain.base_api import BaseApi
from pythonapi.domain.category import Category
from pythonapi.domain.domain_types import PetStatus
from pythonapi.domain.tag import Tag


class Pet(BaseApi):
    __mapping__ = {
        "id": Attr("id", int),
        "name": Attr("name", str),
        "category": Attr("category", Category),
        "photoUrls": Attr("photo_urls", [str]),
        "tags": Attr("tags", [Tag]),
        "status": Attr("status", PetStatus),
    }

    def __init__(self, pet_id: int = None, name: str = None, category: Category = None,
                 photo_urls: [] = None, tags: [Tag] = None, status: PetStatus = None):
        self.id = pet_id
        self.name = name
        self.category = category
        self.photo_urls = photo_urls
        self.tags = tags
        self.status = status

from alchemize import JsonTransmuter
from pytest import mark
import allure

from pythonapi.core.api_response import ApiResponseType
from pythonapi.domain.pet import Pet
from pythonapi.domain.tag import Tag

@allure.feature("Test Pet endpoint")
class TestPet:

    @allure.testcase("Test Pet Add")
    @mark.order(1)
    def test_pet_add(self, api, dp_pet_add, logger):
        _pet = JsonTransmuter.transmute_from(dp_pet_add[0], Pet)
        logger.info(f"Test case for adding pet with ID={_pet.id}")
        response = api.pet_add(_pet)
        assert response.code == dp_pet_add[1]
        assert response.type == ApiResponseType.ok
        assert _pet == response.message
        logger.info(f"Pet with ID={_pet.id} was added.")
    
    @allure.testcase("Test Pet Update")
    @mark.order(2)
    def test_pet_update(self, api, dp_pet_update, logger):
        _pet = JsonTransmuter.transmute_from(dp_pet_update[0], Pet)
        logger.info("Test case for updating pet to the store")
        response = api.pet_update(_pet)
        assert response.code == dp_pet_update[1]
        assert response.type == ApiResponseType.ok
        assert _pet == response.message
        logger.info(f"Pet with ID={_pet.id} was updated.")

    @allure.testcase("Test Pet Find by Status")
    @mark.order(3)
    def test_pet_find_by_status(self, api, logger, dp_pet_status):
        logger.info(f"Test case for finding pet by status [{dp_pet_status[0].value}]")
        response = api.pet_find_by_status(dp_pet_status[0])
        assert response.code == dp_pet_status[1]
        assert response.type == ApiResponseType.ok
        assert all(lambda x: x.status == dp_pet_status[0] for x in response.message)
        logger.info("Test Find Pet by Status PASSED")

    @allure.testcase("Test Pet Find by tags")
    @mark.order(4)
    def test_pet_find_by_tags(self, api, logger, dp_pet_tag):
        logger.info("Test case for finding pet by tags list")
        tag_list = list(map(lambda x: JsonTransmuter.transmute_from(x, Tag), dp_pet_tag[0]))
        response = api.pet_find_by_tags(tag_list)
        assert response.code == dp_pet_tag[1]
        assert response.type == ApiResponseType.ok
        logger.info("Test Find Pet by Tag PASSED")

    @allure.testcase("Test Pet Delete")
    @mark.order(5)
    def test_pet_delete(self, api, logger, dp_pet_delete):
        logger.info(f"Test case for deleting pet ID={dp_pet_delete[0]}")
        response = api.pet_delete(dp_pet_delete[0], dp_pet_delete[1])
        assert response.code == dp_pet_delete[2]
        assert response.type == ApiResponseType.ok
        assert response.message == "Pet deleted"
        logger.info(f"Pet with ID={dp_pet_delete[0]} was deleted")

if __name__ == "__main__":
    pass

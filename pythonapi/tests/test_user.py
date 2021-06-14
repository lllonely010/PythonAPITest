from alchemize import JsonTransmuter
from pytest import mark

from pythonapi.core.api_response import ApiResponseType
from pythonapi.domain.user import User


class TestUser:

    @mark.order(1)
    def test_user_create(self, api, logger, dp_user_add):
        _user = JsonTransmuter.transmute_from(dp_user_add[0], User)
        logger.info(f"Test case for adding user with ID={_user.id}")
        response = api.user_create(_user)
        assert response.code == dp_user_add[1]
        assert response.type == ApiResponseType.ok
        logger.info(f"User with ID={_user.id} was created.")

    @mark.order(2)
    def test_user_login(self, api, logger, dp_user_login):
        logger.info(f"Test case for logging with user name={dp_user_login[0]}")
        response = api.user_login(dp_user_login[0], dp_user_login[1])
        assert response.code == dp_user_login[2]
        assert response.type == ApiResponseType.ok
        logger.info(f"User {dp_user_login[0]} was logged.")
        logger.info("Test User Login PASSED")

    @mark.order(3)
    def test_user_logout(self, api, logger):
        logger.info("Test case for logging out from system")
        response = api.user_logout()
        assert response.code == 200
        assert response.type == ApiResponseType.ok
        assert response.message == "ok"
        logger.info(f"User was logged out.")
        logger.info("Test User Logout PASSED")

    @mark.order(4)
    def test_user_find_by_name(self, api, logger, dp_user_find):
        _user = JsonTransmuter.transmute_from(dp_user_find[0], User)
        logger.info(f"Test case for finding user with name={_user.user_name}")
        response = api.user_find_by_name(_user.user_name)
        assert response.code == dp_user_find[1]
        logger.info("Test User Find by Name PASSED")

    @mark.order(5)
    def test_user_update(self, api, logger, dp_user_update):
        _user = JsonTransmuter.transmute_from(dp_user_update[1], User)
        logger.info(f"Test case for updating user with name={dp_user_update[0]}")
        response = api.user_update(dp_user_update[0], _user)
        assert response.code == dp_user_update[2]
        assert response.type == ApiResponseType.ok
        logger.info(f"User {dp_user_update[0]} was updated")
        response = api.user_find_by_name(_user)
        assert response.code == 200
        logger.info("Test User Update PASSED")

    @mark.order(6)
    def test_user_delete(self, api, logger, dp_user_delete):
        logger.info(f"Test case for deleting user {dp_user_delete[0]}")
        response = api.user_delete(dp_user_delete[0])
        assert response.code == dp_user_delete[1]
        logger.info(f'User {dp_user_delete[0]} was deleted')
        response = api.user_find_by_name(dp_user_delete[0])
        assert response.code == 404
        assert response.type == ApiResponseType.error
        logger.info("Test User Delete PASSED")


if __name__ == "__main__":
    pass

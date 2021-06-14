from alchemize import JsonTransmuter
from pytest import mark

from pythonapi.core.api_response import ApiResponseType
from pythonapi.domain.order import Order


class TestStore:

    @mark.order(1)
    def test_store_inventory(self, api, logger):
        logger.info(f"Test case for store inventory")
        response = api.store_inventory()
        assert response.code == 200
        assert response.type == ApiResponseType.ok
        logger.info("Test Store Inventory PASSED")

    @mark.order(2)
    def test_store_place_order(self, api, logger, dp_order_place):
        _order = JsonTransmuter.transmute_from(dp_order_place[0], Order)
        logger.info(f"Test case for placing an order, ID={_order.id}")
        response = api.store_place_order(_order)
        assert response.code == dp_order_place[1]
        logger.info(f"Order with ID={_order.id} was placed")
        response = api.store_find_order_by_id(_order.id)
        assert response.code == 200
        assert response.type == ApiResponseType.ok
        logger.info("Test Store Place Order PASSED")

    @mark.order(3)
    def test_store_find_order_by_id(self, api, logger, dp_order_find):
        _order = JsonTransmuter.transmute_from(dp_order_find[0], Order)
        logger.info(f"Test case for finding an order, ID={_order.id}")
        response = api.store_find_order_by_id(_order.id)
        assert response.code == dp_order_find[1]
        logger.info("Test Store Find Order By ID PASSED")

    @mark.order(4)
    def test_store_delete_order(self, api, logger, dp_order_delete):
        logger.info(f"Test case for deleting an order, ID={dp_order_delete[0]}")
        response = api.store_delete_order(dp_order_delete[0])
        assert response.code == dp_order_delete[1]
        logger.info(f"Order ID={dp_order_delete[0]} was deleted")
        response = api.store_find_order_by_id(dp_order_delete[0])
        assert response.code == 404
        assert response.type == ApiResponseType.error
        logger.info("Test Store Delete Order PASSED")


if __name__ == "__main__":
    pass

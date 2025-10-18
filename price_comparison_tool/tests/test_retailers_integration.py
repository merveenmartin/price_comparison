from typing import Tuple, Callable, Optional, Any
from compare_prices import search_lowest_price
from retailer.base_retailer import Retailer
from retailer.stock_price_location_parser import (
    dollar_price_parser,
    microcents_price_parser,
    boolean_stock_parser,
    array_stock_parser,
    numeric_stock_parser
)

class MockRetailer(Retailer):
    def __init__(
            self,
            name: str, 
            base_url: str, 
            price_parser: Callable[[dict[str, Any]], float],
            stock_parser: Callable[[dict[str, Any]], bool],
            location_parser: Optional[Callable[[dict[str, Any]], str]]
        ):

        super().__init__(name, base_url, price_parser, stock_parser, location_parser)
        self.name = name
        self.price = price_parser
        self.in_stock = stock_parser
        self.location = location_parser
        self.base_url = base_url

    def get_stock_price_and_location(self) -> Tuple[float, bool, str, str]:
        # overridden method to bypass the live api calls.
        return self.price, self.in_stock, self.base_url, self.location
        
def test_search_lowest_price_dollar_price():

    retailers = [
        MockRetailer("DollarPriceRetailer", "url1", dollar_price_parser({"price": "$3.99"}), boolean_stock_parser({"available": True}), "1001"),
        MockRetailer("MicrocentsRetailer", "url2", microcents_price_parser({"p": 250000000}), boolean_stock_parser({"available": False}), "2002"),
        MockRetailer("BooleanStockRetailer", "url3", dollar_price_parser({"price": "4.50"}), boolean_stock_parser({"available": True}), "3003")
    ]

    result = search_lowest_price(retailers)
    assert result == (3.99, 'url1', '1001')

def test_search_lowest_price_numeric_dollar_price():

    retailers = [
        MockRetailer("DollarPriceRetailer", "url1", dollar_price_parser({"price": "$3.99"}), boolean_stock_parser({"available": True}), "1001"),
        MockRetailer("MicrocentsRetailer", "url2", microcents_price_parser({"p": 250000000}), boolean_stock_parser({"available": False}), "2002"),
        MockRetailer("BooleanStockRetailer", "url3", dollar_price_parser({"price": "3.50"}), boolean_stock_parser({"available": True}), "3003")
    ]

    result = search_lowest_price(retailers)
    assert result == (3.50, 'url3', '3003')

def test_search_lowest_price_microcents_price():

    retailers = [
        MockRetailer("DollarPriceRetailer", "url1", dollar_price_parser({"price": "$3.49"}), boolean_stock_parser({"available": True}), "1001"),
        MockRetailer("MicrocentsRetailer", "url2", microcents_price_parser({"p": 250000000}), boolean_stock_parser({"available": True}), "2002"),
        MockRetailer("BooleanStockRetailer", "url3", dollar_price_parser({"price": "3.50"}), boolean_stock_parser({"available": True}), "3003")
    ]

    result = search_lowest_price(retailers)
    assert result == (2.50, 'url2', '2002')

def test_search_lowest_price_boolean_stock():

    retailers = [
        MockRetailer("DollarPriceRetailer", "url1", dollar_price_parser({"price": "$3.49"}), boolean_stock_parser({"available": False}), "1001"),
        MockRetailer("MicrocentsRetailer", "url2", microcents_price_parser({"p": 250000000}), boolean_stock_parser({"available": False}), "2002"),
        MockRetailer("BooleanStockRetailer", "url3", dollar_price_parser({"price": "5.50"}), boolean_stock_parser({"available": True}), "3003")
    ]

    result = search_lowest_price(retailers)
    assert result == (5.50, 'url3', '3003')

def test_search_lowest_price_numeric_stock():

    retailers = [
        MockRetailer("DollarPriceRetailer", "url1", dollar_price_parser({"price": "$2.49"}), numeric_stock_parser({"stock": 10}), "1001"),
        MockRetailer("MicrocentsRetailer", "url2", microcents_price_parser({"p": 250000000}), boolean_stock_parser({"available": True}), "2002"),
        MockRetailer("BooleanStockRetailer", "url3", dollar_price_parser({"price": "5.50"}), boolean_stock_parser({"available": True}), "3003")
    ]

    result = search_lowest_price(retailers)
    assert result == (2.49, 'url1', '1001')

def test_search_lowest_price_array_stock():

    retailers = [
        MockRetailer("DollarPriceRetailer", "url1", dollar_price_parser({"price": "$2.49"}), array_stock_parser({"a": [{"q": 2, "l": "4004"}]}), "1001"),
        MockRetailer("MicrocentsRetailer", "url2", microcents_price_parser({"p": 250000000}), boolean_stock_parser({"available": True}), "2002"),
        MockRetailer("BooleanStockRetailer", "url3", dollar_price_parser({"price": "5.50"}), boolean_stock_parser({"available": True}), "3003")
    ]

    result = search_lowest_price(retailers)
    assert result == (2.49, 'url1', '1001')
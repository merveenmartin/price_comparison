from compare_prices import search_lowest_price

class MockRetailers:
    def __init__(self, name: str, price: float, in_stock: bool, base_url: str, location: str):
        self.name = name
        self.price = price
        self.in_stock = in_stock
        self.base_url = base_url
        self.location = location

    def get_stock_price_and_location(self):
        return self.price, self.in_stock, self.base_url, self.location

def test_search_lowest_price_single_in_stock():
    retailers = [
        MockRetailers("Retailer1", 4.5, True, "url1", "11111"),
        MockRetailers("Retailer2", 4.2, True, "url2", "22222"),
        MockRetailers("Retailer3", 5.0, False, "url3", "33333")
    ]

    result = search_lowest_price(retailers)
    assert result == (4.2, "url2", "22222")

def test_search_lowest_price_multiple_in_stock():
    retailers = [
        MockRetailers("Retailer1", 4.5, True, "url1", "11111"),
        MockRetailers("Retailer2", 4.5, True, "url2", "22222"),
        MockRetailers("Retailer3", 5.0, True, "url3", "33333")
    ]

    result = search_lowest_price(retailers)
    assert result == (4.5, "url1", "11111")

def test_search_lowest_price_no_stock():
    retailers = [
        MockRetailers("Retailer1", 4.5, False, "url1", "11111"),
        MockRetailers("Retailer2", 4.2, False, "url2", "22222"),
        MockRetailers("Retailer3", 5.0, False, "url3", "33333")
    ]

    result = search_lowest_price(retailers)
    assert result == None
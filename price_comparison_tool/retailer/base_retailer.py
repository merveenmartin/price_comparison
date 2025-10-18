import requests
from typing import Any, Tuple, Callable, Optional

class Retailer:
    def __init__(
        self,
        name: str,
        base_url: str,
        price_parser: Callable[[dict[str, Any]], float],
        stock_parser: Callable[[dict[str, Any]], bool],
        location_parser: Optional[Callable[[dict[str, Any]], str]] = None
    ):
    
        self.name = name
        self.base_url = base_url
        self.price_parser = price_parser
        self.stock_parser = stock_parser
        self.location_parser = location_parser
    
    def get_stock_price_and_location(self) -> Tuple[float, bool, str, str]:
        url = self.base_url
        api_response = requests.get(url).json()
        print("Name:", self.name, "URL:", self.base_url, "API Response:", api_response)
        price = self.price_parser(api_response)
        in_stock = self.stock_parser(api_response)
        location = self.location_parser(api_response) if self.location_parser else None
        return price, in_stock, url, str(location)
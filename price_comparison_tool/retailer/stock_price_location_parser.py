from typing import Any, Dict, List

def dollar_price_parser(resp: Dict[str, Any], key: str = "price") -> float:
    """
    function to get the price from the api response and return a float vault
    """
    price = resp.get(key)
    if not price:
        raise ValueError(f"No key {key} in response")
    
    return float(str(price).replace("$", "").strip())

def microcents_price_parser(resp: Dict[str, Any], key: str = "p") -> float:
    """
    function get and convert the microcents to dollars
    """
    price = resp.get(key)
    if not price:
       raise ValueError(f"No key {key} in response")
    microcents = price / 100_000_000

    return microcents

def numeric_stock_parser(resp: Dict[str, Any], key: str = "stock") -> bool:
    """
    function to get the stock which is in numeric value
    """
    stock = resp.get(key)
    if not stock:
        raise ValueError(f"No key {key} in response")
    
    return int(stock) > 0

def boolean_stock_parser(resp: Dict[str, Any], key: str = "available") -> bool:
    """
    function to check if the stock is available or not
    """
    return bool(resp.get(key, False))

def array_stock_parser(resp: Dict[str, Any], key: str = "a") -> bool:
    """
    function to iterate the response array to find if stock > 0
    """
    arr: List[Dict[str, Any]] = resp.get(key, [])

    return bool((item.get("q", 0) or 0) for item in arr)

def available_location(resp: Dict[str, Any], key: str = "a") -> str:
    """
    function to get all the locations 
    """
    arr: List[Dict[str, Any]] = resp.get(key, [])
    get_available_location = [item["l"] for item in arr if item.get("q", 0) > 0]

    stock_location: str = ""
    if get_available_location:
        stock_location = ", ". join(str(loc) for loc in get_available_location)

    return stock_location

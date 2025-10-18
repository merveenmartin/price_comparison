from typing import List, Tuple, Optional, Any

def search_lowest_price(retailers: List[Any]) -> Optional[Tuple[float, str, str]]:
    """
    function to iterate all the retailers and find the lowest price when stock is available
    """
    results: List[Tuple[float, str, str]] = []
    for retailer in retailers:
        try:
            price, in_stock, url, location = retailer.get_stock_price_and_location()
            if in_stock:
                results.append((price, url, location))  
        except Exception as e:
            print(f"Error fetching {retailer.name}: {e}")

    return min(results) if results else None
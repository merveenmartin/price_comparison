from retailer.stock_price_location_parser import dollar_price_parser, array_stock_parser, available_location, boolean_stock_parser, microcents_price_parser, numeric_stock_parser
from retailer.base_retailer import Retailer
from compare_prices import search_lowest_price
from typing import List, Any

UPC = 101

APPEDIA_URL = f"https://appedia.heb-platform-interview.hebdigital-prd.com/api/v1/itemdata?upc={UPC}"
MICRO_URL = f"https://micromazon.heb-platform-interview.hebdigital-prd.com/{UPC}/productinfo"
GOOG_URL = f"https://googdit.heb-platform-interview.hebdigital-prd.com/{UPC}"

retailers: List[Any] = [
    Retailer("Appedia", APPEDIA_URL, dollar_price_parser, numeric_stock_parser),
    Retailer("Micromazon", MICRO_URL, dollar_price_parser, boolean_stock_parser),
    Retailer("Googdit", GOOG_URL, microcents_price_parser, array_stock_parser, available_location)
]

def main():
    result = search_lowest_price(retailers)

    if result:
        price, url, location = result
        print(f"\nLowest price is ${price:.2f} from the retailer {url}. Location {location}")
    else:
        print("\nSorry!! No retailer has item in stock")

if __name__ == "__main__":
    main()

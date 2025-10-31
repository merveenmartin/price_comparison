Price Comparison Tool Problem This will be a multi-part question and the expectation is you likely won’t complete it in the 2-hour time allotment. Be sure that you have provided your GitHub username to your recruiter. You will receive an invite to a code repository on the HEB-Recruiting GitHub account at https://github.com/heb-recruiting where you will submit your code for review. If you find any issues with the files we have sent or have other questions don’t hesitate to reach out to your recruiter or the H-E-B Partner that you met with during the 15-min Q&A session.
Build a price comparison tool that will get pricing and availability data from these sources:
URL
https://appedia.heb-platform-interview.hebdigital-prd.com/api/v1/itemdata?upc=101 Response
{
"price": "$4.77",
"stock": 7
} Description
Price is returned as a string
Availability(‘stock’) returned as an integer value, 0 meaning out of stock.
URL
https://micromazon.heb-platform-interview.hebdigital-prd.com/101/productinfo Response
{
"available": true,
"price": 5.67
} Description Price is returned as a double Availability(‘available’) returned as a boolean value
URL
https://googdit.heb-platform-interview.hebdigital-prd.com/101 Response
{
"a": [
{
"l": 8839,
"q": 4
},
{
"l": 1292,
"q": 0
}
],
"p": 478000000
} Description Price is returned as microcents (ie 234000000 == $2.34) Availability(‘a’) is returned as an array of objects with quantity(‘q’) available at location(‘l’)
Requirements
• Return the URL that has the lowest price and has the item in stock at any location. • Make it easy to swap item UPC. • Make it easy to add additional merchant URLs to query for price comparison. • Write unit/integration tests.
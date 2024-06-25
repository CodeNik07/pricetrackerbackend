from bs4 import BeautifulSoup as bs
import requests as req


class ProductScrapper:

    def gemScrapper(self, gemUrl):
        data = req.get(gemUrl)
        web_content = bs(data.text, 'html.parser')
        title = web_content.findAll("div", {"id": "title"})[0].text.strip().split("   ")[0]
        imgLink = web_content.findAll("noscript")[1].next.get("src")
        price = web_content.findAll("span", {"class": "m-w"})[0].text.split('₹')[1]
        gemDetails = {
            "gemUrl": gemUrl,
            "gemTitle": title,
            "gemImg": imgLink,
            "gemPrice": price
        }
        return gemDetails


    def flipkartScrapper(self, flipUrl):
        data = req.get(flipUrl)
        web_content = bs(data.text, "html.parser")
        flipkartPrice = web_content.findAll("div", {"class": "Nx9bqj CxhGGd"})[0].text.split('₹')[1]
        flipkartTitle = web_content.findAll("span", {"class": "VU-ZEz"})[0].text
        flipkartDetails = {
            "flipUrl": flipUrl,
            "flipTitle": flipkartTitle,
            "flipPrice": flipkartPrice
        }

        return flipkartDetails


# obj1 = ProductScrapper()
# gemUrl = "https://mkp.gem.gov.in/laptop-notebook/acer-amd-ryzen-5-15-6-inch-laptop/p-5116877-87147402538-cat.html#variant_id=5116877-87147402538"
# # obj1.gemScrapper(gemUrl)
# flipkart = "https://www.flipkart.com/pilot-v5-pen-pack-2-blue-roller-ball/p/itmd6mzxham7h4gf"
# obj1.flipkartScrapper(flipkart)


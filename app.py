from flask import Flask, jsonify, request
from scraper import ProductScrapper
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

app = Flask(__name__)
ps = ProductScrapper()
uri = "mongodb+srv://depricetracker:N1dJecxP8A9UbNKd@cluster0.bqmd2zc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri, server_api=ServerApi('1'))
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client.e_Market_Products
collection = db.product

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/product", methods=['POST'])
def products():
    productUrl = request.json.get("product")
    dbID = productUrl.split('#')[1].split('=')[1]
    data = collection.find_one({"_id": dbID})
    gemUrl = data["gem"]
    flipkart = data["flipkart"]
    gemData = ps.gemScrapper(gemUrl)
    flipkartData = ps.flipkartScrapper(flipkart)

    return jsonify({
        "gemData": gemData,
        "flipkartData": flipkartData
    })


@app.route("/demo", methods=['GET', 'POST'])
def testDemo():
    productUrl = request.json.get("product")
    # dbID = productUrl.split('#')[1].split('=')[1]
    # data = collection.find_one({"_id": dbID})
    print(productUrl)
    # return data["gem"]
    return "okay"



if __name__ == "__main__":
    app.run(debug=True)

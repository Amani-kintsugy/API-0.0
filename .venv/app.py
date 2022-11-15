
from flask import Flask,request
app = Flask(__name__)
store= [
    {
    "name" : "My first store",
    "items" : [
        {
        "name" : "Chair",
        "price" : 15.99
        }
        ]
    }
]
@app.get("/store") #http://127.0.0.1:5000/store
def get_stores():
    return{"store": store}


@app.post("/store") #http://127.0.0.1:5000/store
def create_stores():
    request_data = request.get_json()
    new_store={"name":request_data["name"], "items":[]}
    store.append(new_store)
    return new_store, 201
@app.post("/store/<string:name>/item")
def create_item(name):
    request_data = request.get_json()
    for store in store: 
        if store['name']==name:
            new_item={"name":request_data["name"], "price":request_data["name"]}
            store["items"].append(new_item)
            return new_item, 201
        return {"message": "store not found"}, 404

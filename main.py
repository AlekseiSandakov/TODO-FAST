from fastapi import FastAPI, HTTPException
import json

PRODUCT = {
    1: "Meat",
    2: "Bread",
    3: "Cheese",
}

app = FastAPI()


@app.get("/products")
def read_items():
    products_as_list = [
        {"id": product_id, "product": product}
        for product_id, product in PRODUCT.items()
    ]
    text = json.dumps(products_as_list)

    return text


@app.get("/products/{product_id}")
def read_item(product_id: str):
    try:
        product_id = int(product_id)
        product = PRODUCT[product_id]
    except (ValueError, KeyError):
        return HTTPException(status_code=404, detail={"message": "not found"})
    else:
        result = {"id": product_id, "product": product}
    text = json.dumps(result)

    return text

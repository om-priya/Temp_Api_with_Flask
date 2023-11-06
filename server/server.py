from flask import Flask, request
from database import DatabaseConnection

app = Flask(__name__)


@app.route("/products")
def show_all_products():
    try:
        with DatabaseConnection("products.db") as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM product"
            cursor.execute(query)
            products = cursor.fetchall()
    except Exception:
        products = "No Product Exists"
    return products


@app.route("/product/<int:pId>")
def show_product(pId):
    try:
        with DatabaseConnection("products.db") as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM product WHERE pId = ?"
            params = (pId,)
            cursor.execute(query, params)
            product = cursor.fetchone()
    except Exception:
        product = f"No Product with Id {pId}"
    return list(product)


@app.route("/product/add", methods=["POST"])
def add_product():
    try:
        pId = request.form["pId"]
        pname = request.form["pname"]

        with DatabaseConnection("products.db") as connection:
            cursor = connection.cursor()
            cursor.execute(
                """CREATE TABLE IF NOT EXISTS product(
                                pId TEXT,
                                pname TEXT
                    )"""
            )
            query = """INSERT INTO product
                                (pId, pname)
                                VALUES
                                (?,?)"""
            params = (pId, pname)
            cursor.execute(query, params)
    except Exception:
        message = "Something Wrong Happend"
    else:
        message = "Product Added Successfully"

    return message


@app.route("/product/delete/<int:pId>", methods=["DELETE"])
def delete_product(pId):
    try:
        with DatabaseConnection("products.db") as connection:
            cursor = connection.cursor()
            query = "DELETE FROM product WHERE pId = (?)"
            params = (pId,)
            cursor.execute(query, params)
    except Exception:
        message = "Something Went Wrong"
    else:
        message = "Product Deleted Successfully"

    return message


@app.route("/product/update/<int:pId>", methods=["PATCH"])
def update_product(pId):
    try:
        updated_name = request.form["pname"]

        with DatabaseConnection("products.db") as connection:
            cursor = connection.cursor()
            query = "UPDATE product SET pname = (?) WHERE pId = (?)"
            params = (updated_name, pId)
            cursor.execute(query, params)
    except Exception:
        message = "Something went wrong"
    else:
        message = "Product Updated Successfully"
    return message


if __name__ == "__main__":
    app.run(debug=True)

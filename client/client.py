import requests
from pprint import pprint


def show_all_product():
    products = requests.get("http://127.0.0.1:5000/products")
    products = products.json()
    pprint(products)


def show_product():
    pId = int(input("Enter the pId: "))
    product = requests.get(f"http://127.0.0.1:5000/product/{pId}")
    product = product.json()
    pprint(product)


def add_product():
    pId = int(input("Enter the pId: "))
    pname = input("Enter the name of product: ")
    values = {"pId": pId, "pname": pname}
    message = requests.post("http://127.0.0.1:5000/product/add", data=values)
    message = message.text
    pprint(message)


def delete_product():
    pId = int(input("Enter the pId: "))
    message = requests.delete(f"http://127.0.0.1:5000/product/delete/{pId}")
    message = message.text
    pprint(message)


def update_product():
    pId = int(input("Enter the pId of the updated product: "))
    pname = input("Enter new name for product: ")
    values = {"pname": pname}
    message = requests.patch(f"http://127.0.0.1:5000/product/update/{pId}", data=values)
    message = message.text
    pprint(message)


while True:
    user_req = input(
        """What do You Want?
                     1> Show all product
                     2> Show product with Id
                     3> Add product
                     4> Delete product
                     5> Update product
                     Enter Your Query: """
    )
    try:
        match user_req:
            case "1":
                show_all_product()
            case "2":
                show_product()
            case "3":
                add_product()
            case "4":
                delete_product()
            case "5":
                update_product()
            case "_":
                print("Invalid Requests")
    except Exception:
        print("Something Went Wrong Try Again")

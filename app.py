from flask import Flask, render_template, request
app = Flask(__name__)

# Define a dictionary to store items and prices
items = {
    "Apple": 10,
    "Banana": 5,
    "Milk": 20,
    "Bread": 15,
    "Eggs": 30,
    "Chicken": 50,
    "Rice": 25,
    "Sugar": 18,
    "Coffee": 20,
    "Tea": 15,
    "Oil": 30,
    "Onion": 8,
    "Potato": 10,
    "Carrot": 12,
    "Beef": 60,
    "Fish": 40,
    "Soap": 10,
    "Shampoo": 20,
    "Toothpaste": 15
}

@app.route("/")
def index():
    return render_template("index.html", items=items)

@app.route("/generate_bill", methods=["POST"])
def generate_bill():
    bill = []
    total = 0
    for item, quantity in request.form.items():
        if item != "csrf_token":
            price = items[item]
            bill.append({"item": item, "quantity": quantity, "price": price * int(quantity)})
            total += price * int(quantity)
    return render_template("bill.html", bill=bill, total=total)

if __name__ == "__main__":
    app.run(debug=True)
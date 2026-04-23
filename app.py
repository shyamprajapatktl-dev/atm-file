from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

class BankAccount:
    def __init__(self, name, pin, balance=0):
        self.name = name
        self.__pin = pin
        self.__balance = balance

    def verify_pin(self, pin):
        return self.__pin == pin

    def deposit(self, amount, pin):
        if not self.verify_pin(pin):
            return {"status": "error", "msg": "Wrong PIN"}

        if amount > 0:
            self.__balance += amount
            return {"status": "success", "balance": self.__balance}

        return {"status": "error", "msg": "Invalid amount"}

    def withdraw(self, amount, pin):
        if not self.verify_pin(pin):
            return {"status": "error", "msg": "Wrong PIN"}

        if amount <= self.__balance:
            self.__balance -= amount
            return {"status": "success", "balance": self.__balance}

        return {"status": "error", "msg": "Insufficient balance"}

    def get_balance(self, pin):
        if not self.verify_pin(pin):
            return {"status": "error", "msg": "Wrong PIN"}

        return {"status": "success", "balance": self.__balance}


user = BankAccount("Shyam", 1234, 1000)

@app.route("/")
def home():
    return "ATM Backend Running ✅"

@app.route("/deposit", methods=["POST"])
def deposit():
    data = request.json
    return jsonify(user.deposit(data["amount"], data["pin"]))

@app.route("/withdraw", methods=["POST"])
def withdraw():
    data = request.json
    return jsonify(user.withdraw(data["amount"], data["pin"]))

@app.route("/balance", methods=["POST"])
def balance():
    data = request.json
    return jsonify(user.get_balance(data["pin"]))


if __name__ == "__main__":
    app.run(debug=True)
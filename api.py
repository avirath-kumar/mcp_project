from flask import Flask, jsonify

app = Flask(__name__)

# Mock data
MOCK_TRANSACTION = {
    "id": 1,
    "amount": 100.50,
    "description": "Coffee and snacks",
    "date": "2024-04-03",
    "type": "debit",
    "category": "Food & Beverages"
}

MOCK_TRANSACTIONS = [
    {
        "id": 1,
        "amount": 100.50,
        "description": "Coffee and snacks",
        "date": "2024-04-03",
        "type": "debit",
        "category": "Food & Beverages"
    },
    {
        "id": 2,
        "amount": 1500.00,
        "description": "Monthly salary",
        "date": "2024-04-01",
        "type": "credit",
        "category": "Income"
    },
    {
        "id": 3,
        "amount": 50.00,
        "description": "Book purchase",
        "date": "2024-04-02",
        "type": "debit",
        "category": "Entertainment"
    }
]

@app.route('/transaction', methods=['GET'])
def get_transaction():
    return jsonify(MOCK_TRANSACTION)

@app.route('/transactions', methods=['GET'])
def get_transactions():
    return jsonify(MOCK_TRANSACTIONS)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True) 
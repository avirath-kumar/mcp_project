from mcp.server.fastmcp import FastMCP
import requests

# create a fastmcp server
mcp = FastMCP("transaction_mcp_demo")

# Tool #1: call GET /transaction api endpoint
@mcp.tool()
def get_transaction() -> dict:
    '''This provides the most recent credit card transaction of the user
    
    Returns:
        dict: A single transaction record
    '''
    response = requests.get("http://localhost:8081/transaction")
    transaction = response.json()
    return transaction

@mcp.tool()
def get_transactions() -> list:
    '''This provides all the credit card transactions of the user
    
    Returns:
        list: List of transaction records
    '''
    response = requests.get("http://localhost:8081/transactions")
    transactions = response.json()
    return transactions

if __name__ == "__main__":
    mcp.run()
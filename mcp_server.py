from mcp.server.fastmcp import FastMCP
import requests

# create a fastmcp server
mcp = FastMCP("Demo")

# Tool #1: call GET /transaction api endpoint
@mcp.tool()
def get_transaction() -> dict:
    '''This provides the most recent credit card transaction of the user
    
    Args:
        None
    
    Returns:
        dict: A single transaction record
    '''
    response = requests.get("http://localhost:8081/transaction")
    transaction = response.json()
    return transaction

@mcp.tool()
def get_transactions() -> list:
    '''This provides all the credit card transactions of the user
    
    Args:
        None
    
    Returns:
        list: List of transaction records
    '''
    response = requests.get("http://localhost:8081/transactions")
    transactions = response.json()
    return transactions

# Add print statement outside the if block to see if the file is being loaded
print("MCP server file loaded")

if __name__ == "__main__":
    print("Starting MCP server...")
    mcp.run()
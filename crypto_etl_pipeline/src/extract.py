import requests
import dotenv
import os

dotenv.load_dotenv()

def extract_crypto_data():
    """
    Extracts the top 10 cryptocurrencies from the CoinCap API.

    This function authenticates using a Bearer token (API Key) to ensure
    higher rate limits and a stable connection suitable for production environments.

    Returns:
        list: A list of dictionaries containing raw cryptocurrency data.
        None: If the HTTP request fails or the connection drops.
    """
    url = "https://rest.coincap.io/v3/assets"
    
    params = {
        "limit": 10
    }
    
    api_key = os.getenv('api_key_token')
    if not api_key:
        print("Critical Error: 'api_key_token' not found in .env file.")
        return None
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Accept-Encoding": "gzip"
    }
    
    print("Starting data extraction from CoinCap API...")
    
    try:
        response = requests.get(url, params=params, headers=headers, timeout=10)
        response.raise_for_status() 
        
        raw_data = response.json()["data"]
        
        print(f"Success: {len(raw_data)} records extracted securely.")
        return raw_data
        
    except requests.exceptions.RequestException as e:
        print(f"Critical extraction failure: {e}")
        return None
    
    
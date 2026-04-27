import pandas as pd
from datetime import datetime

def transform_crypto_data(raw_data):
    """
    Transforms the raw JSON data from CoinCap into a structured Pandas DataFrame.
    
    Args:
        raw_data (list): A list of dictionaries containing raw crypto data.
        
    Returns:
        pd.DataFrame: A cleaned DataFrame ready for loading, or None if input is empty.
    """
    if not raw_data:
        print("Error: No data to transform.")
        return None
        
    print("Starting data transformation with Pandas (CoinCap schema)...")
    df = pd.DataFrame(raw_data)
    
    key_columns = ['id', 'symbol', 'name', 'priceUsd', 'marketCapUsd', 'volumeUsd24Hr']
    
    df_clean = df[key_columns].copy()
    
    numeric_columns = ['priceUsd', 'marketCapUsd', 'volumeUsd24Hr']
    for col in numeric_columns:
        df_clean[col] = pd.to_numeric(df_clean[col], errors='coerce')
        
    df_clean['last_updated'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    print(f"Transformation successful. Final structure: {df_clean.shape[0]} rows, {df_clean.shape[1]} columns.")
    return df_clean
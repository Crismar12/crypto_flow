import os

def load_crypto_data(df, filepath="data/crypto_historical.csv"):
    """
    Loads a transformed Pandas DataFrame into a local CSV file.

    This function ensures that historical data is preserved by appending
    new rows to the existing file in 'append' mode, rather than overwriting it.
    It dynamically handles the CSV headers depending on file existence.

    Args:
        df (pd.DataFrame): The cleaned DataFrame containing cryptocurrency data.
        filepath (str, optional): The destination path for the CSV file. 
            Defaults to "data/crypto_historical.csv".

    Returns:
        bool: True if the load was successful, False if the input DataFrame is empty or invalid.
    """
    if df is None or df.empty:
        print("Error: No data to load. Aborting.")
        return False
    
    print("Starting data load to local disk...")
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    
    file_exists = os.path.isfile(filepath)
    
    df.to_csv(
        filepath, 
        mode='a' if file_exists else 'w', 
        header=not file_exists, 
        index=False
    )
    
    print(f"Load successful. File saved at: {filepath}")
    return True
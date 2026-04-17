import requests
import pandas as pd

def extract_crypto_data():
    """
    Se conecta a la API pública de CoinGecko y extrae el top 10 de criptomonedas.
    """
    url = "https://api.coingecko.com/api/v3/coins/markets"
    
    # Parámetros exactos de la consulta (Dólares, ordenado por mercado, top 10)
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 10,
        "page": 1,
        "sparkline": False
    }
    
    print("Iniciando extracción de datos desde CoinGecko...")
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status() # Detiene el código si hay error HTTP (ej. 404, 500)
        
        raw_data = response.json()
        print(f"Éxito. {len(raw_data)} registros extraídos.")
        
        # Imprimimos el primer registro (Bitcoin) para validar visualmente la estructura
        print("\nMuestra del primer registro crudo:")
        print(raw_data[0])
        
        return raw_data
        
    except requests.exceptions.RequestException as e:
        print(f"Fallo crítico en la extracción: {e}")
        return None

if __name__ == "__main__":
    # Prueba de fuego local
    data = extract_crypto_data()
import pandas as pd

def transform_crypto_data(raw_data):
    """
    Recibe el JSON crudo de CoinGecko, lo convierte en un DataFrame de Pandas,
    filtra las columnas necesarias y limpia los datos.
    """
    if not raw_data:
        print("No hay datos para transformar.")
        return None
    
    print("Iniciando transformación de datos con Pandas...")
    
    # 1. Convertir el JSON crudo a un DataFrame tabular
    df = pd.DataFrame(raw_data)
    
    # 2. Filtrar solo las columnas que aportan valor de negocio
    columnas_clave = [
        'id', 'symbol', 'name', 'current_price', 
        'market_cap', 'total_volume', 'last_updated'
    ]
    df_clean = df[columnas_clave]
    
    # 3. Normalizar formatos (Asegurar que la fecha sea un formato de tiempo real)
    df_clean['last_updated'] = pd.to_datetime(df_clean['last_updated'])
    
    print(f"Transformación exitosa. Estructura final: {df_clean.shape[0]} filas, {df_clean.shape[1]} columnas.")
    
    # Mostramos las primeras 3 líneas de la tabla limpia en la terminal
    print("\nMuestra de los datos transformados:")
    print(df_clean.head(3))
    
    return df_clean

if __name__ == "__main__":
    # Importamos la función de extracción solo para probar este archivo localmente
    from extract import extract_crypto_data
    
    # Simulamos el flujo E -> T
    datos_crudos = extract_crypto_data()
    datos_limpios = transform_crypto_data(datos_crudos)
from src.extract import extract_crypto_data
from src.transform import transform_crypto_data
from src.load import load_crypto_data

def run_pipeline():
    """
    Orchestrates the full Extract, Transform, Load (ETL) pipeline.

    This function sequentially calls the extraction, transformation, and
    loading modules. It includes basic error handling to halt the pipeline
    if any phase fails, preventing corrupted data from being saved.

    Returns:
        None
    """
    print("=== STARTING DATA PIPELINE (ETL) ===")
    
    raw_data = extract_crypto_data()
    if not raw_data:
        print("Pipeline stopped: Extraction failed.")
        return
        
    clean_data = transform_crypto_data(raw_data)
    if clean_data is None or clean_data.empty:
        print("Pipeline stopped: Transformation failed.")
        return

    success = load_crypto_data(clean_data)
    
    if success:
        print("=== PIPELINE EXECUTED SUCCESSFULLY ===")
    else:
        print("=== ERROR WHEN FINISHING THE PIPELINE ===")

if __name__ == "__main__":
    run_pipeline()
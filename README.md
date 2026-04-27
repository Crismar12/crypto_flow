# Crypto ETL Pipeline 🚀

A robust, production-ready Data Engineering pipeline that automates the daily extraction, transformation, and loading (ETL) of cryptocurrency market data.

## 📌 Overview

This project implements a modular ETL architecture to track historical cryptocurrency prices. It connects to the **CoinCap API v3**, processes the data using **Pandas**, and maintains a time-series dataset in CSV format. The entire process is fully automated using **GitHub Actions**.



## 🏗️ Architecture

The pipeline is divided into three decoupled stages to ensure maintainability and scalability:

1.  **Extract (`extract.py`)**: Fetches raw JSON data from the CoinCap API (V3) using secure Bearer Token authentication.
2.  **Transform (`transform.py`)**: Cleans the data, handles data type conversions (Strings to Floats), filters key columns, and injects timestamps.
3.  **Load (`load.py`)**: Persists data into a local/remote CSV file using an "append-only" logic to build a historical record without overwriting previous data.

## 🛠️ Tech Stack

* **Language:** Python 3.11+
* **Data Analysis:** Pandas
* **API Requests:** Requests
* **Environment Management:** Python-dotenv
* **Automation:** GitHub Actions
* **Security:** OS Environment Variables (Secrets)

## 🤖 Automation

The pipeline is orchestrated via **GitHub Actions**. 
* **Schedule:** Runs automatically every day at 00:00 UTC.
* **Persistence:** The virtual runner performs a secure `git push` to update the historical dataset directly in the repository.
* **Security:** API credentials are encrypted using GitHub Repository Secrets.

## 🚀 How to Run Locally

### 1. Clone the repository
```bash
git clone [https://github.com/Crismar12/crypto_flow.git](https://github.com/Crismar12/crypto_flow.git)
cd crypto_flow
```
### 2. Install dependencies
It is recommended to use a virtual environment to keep your global Python installation clean.
```bash
cd crypto_etl_pipeline
pip install -r requirements.txt
```
### 3. Configure Environment Variables
Create a .env file inside the crypto_etl_pipeline directory and add your API key. This ensures your credentials are never exposed in the source code.
```bash
api_key_token=your_coincap_api_key_here
```
### 4. Run the pipeline
Execute the main orchestrator to start the ETL process.
```bash
python main.py
```
## 📊 Data Output
The processed data is stored in crypto_etl_pipeline/data/crypto_historical.csv.

### Each execution appends new records using the following schema:

id: Unique identifier for the asset.

symbol: Ticker symbol (e.g., BTC, ETH).

name: Full asset name.

priceUsd: Current price in US Dollars.

marketCapUsd: Total market capitalization.

volumeUsd24Hr: Trading volume in the last 24 hours.

last_updated: Timestamp of the transformation process.

#### Developed as part of a professional portfolio

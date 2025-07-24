# binance-data-visualizer/binance-data-visualizer/backend/README.md

# Binance Data Visualizer Backend

This is the backend component of the Binance Data Visualizer project, which provides a FastAPI application for fetching historical Binance data.

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd binance-data-visualizer/backend
   ```

2. **Create a virtual environment (optional but recommended):**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Set up your environment variables:**
   Create a `.env` file in the backend directory and add your Binance API credentials:
   ```
   API_KEY=your_api_key
   API_SECRET=your_api_secret
   ```

## Usage

To run the FastAPI application, execute the following command:
```
uvicorn app:app --reload
```

The application will be available at `http://127.0.0.1:8000`.

## API Endpoints

### Get Historical Klines

- **Endpoint:** `/klines`
- **Method:** `GET`
- **Parameters:**
  - `symbol`: The trading pair symbol (e.g., BTCUSDT).
  - `interval`: The time interval for the klines (e.g., 1d, 1h).
  - `start_str`: The start date for fetching data (e.g., "2024-07-23").
  - `end_str`: The end date for fetching data (optional).

**Example Request:**
```
GET /klines?symbol=BTCUSDT&interval=1d&start_str=2024-07-23&end_str=2025-07-24
```

**Response:**
Returns a JSON array of historical kline data.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
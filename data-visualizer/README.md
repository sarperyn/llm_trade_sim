# binance-data-visualizer/binance-data-visualizer/README.md

# Binance Data Visualizer

This project is a web application that allows users to fetch and visualize historical cryptocurrency data from the Binance API. It consists of a FastAPI backend that serves the data and a JavaScript frontend that displays the data using Lightweight Charts.

## Project Structure

```
binance-data-visualizer
├── backend
│   ├── app.py               # FastAPI application with API endpoints
│   ├── binance_client.py     # Client for interacting with the Binance API
│   ├── requirements.txt      # Python dependencies for the backend
│   └── README.md             # Documentation for the backend
├── frontend
│   ├── public
│   │   └── index.html        # Main HTML file for the frontend
│   ├── src
│   │   ├── app.js            # JavaScript code for fetching and plotting data
│   │   └── styles.css        # CSS styles for the frontend
│   ├── package.json          # npm configuration for the frontend
│   └── README.md             # Documentation for the frontend
└── README.md                 # Overview of the entire project
```

## Backend Setup

1. Navigate to the `backend` directory:
   ```
   cd backend
   ```

2. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```

3. Run the FastAPI application:
   ```
   uvicorn app:app --reload
   ```

4. Access the API documentation at `http://127.0.0.1:8000/docs`.

## Frontend Setup

1. Navigate to the `frontend` directory:
   ```
   cd frontend
   ```

2. Install the required npm packages:
   ```
   npm install
   ```

3. Start the frontend application:
   ```
   npm start
   ```

4. Open your browser and go to `http://localhost:3000` to view the application.

## Usage

- Use the frontend interface to input the cryptocurrency symbol, interval, and date range to fetch historical data.
- The data will be visualized using Lightweight Charts.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.
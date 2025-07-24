from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
from binance_client import BinanceDataClient

app = FastAPI()

class KlineRequest(BaseModel):
    symbol: str
    interval: str
    start_str: str
    end_str: Optional[str] = None

@app.get("/klines", response_model=List[dict])
def get_klines(request: KlineRequest):
    """
    Fetch historical klines (candlestick data) from Binance API.
    """
    client = BinanceDataClient()
    df = client.get_historical_klines(
        symbol=request.symbol,
        interval=request.interval,
        start_str=request.start_str,
        end_str=request.end_str
    )
    
    # Convert DataFrame to list of dictionaries for response
    return df.reset_index().to_dict(orient='records')
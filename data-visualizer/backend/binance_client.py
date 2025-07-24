from dotenv import load_dotenv
import os
import pandas as pd
from binance.client import Client

load_dotenv()

class BinanceDataClient:
    def __init__(self, api_key: str = None, api_secret: str = None):
        self.api_key = api_key or os.getenv("API_KEY")
        self.api_secret = api_secret or os.getenv("API_SECRET")
        if not (self.api_key and self.api_secret):
            raise EnvironmentError("Missing API_KEY or API_SECRET in environment")
        self.client = Client(self.api_key, self.api_secret)

    def __create_ema(self, df: pd.DataFrame, period: int) -> pd.Series:
        return df['close'].ewm(span=period, adjust=False).mean()

    def get_historical_klines(
        self,
        symbol: str,
        interval: str,
        start_str: str,
        end_str: str = None,
        limit: int = 1000,
    ) -> pd.DataFrame:
        raw = self.client.get_historical_klines(
            symbol=symbol,
            interval=interval,
            start_str=start_str,
            end_str=end_str,
            limit=limit
        )

        df = pd.DataFrame(raw, columns=[
            "open_time", "open", "high", "low", "close", "volume",
            "close_time", "quote_asset_volume", "num_trades",
            "taker_buy_base_asset_volume", "taker_buy_quote_asset_volume", "ignore"
        ])
        df = df[["open_time", "open", "high", "low", "close", "volume"]]
        df["open_time"] = pd.to_datetime(df["open_time"], unit="ms")
        df.set_index("open_time", inplace=True)

        for period in [20, 50, 100, 200]:
            df[f"EMA_{period}"] = self.__create_ema(df, period)

        # Create a csv file with the DataFrame
        df.to_csv(f"{symbol}_{interval}_data.csv")
        
        return df.astype(float)
import pandas as pd
from typing import Dict, Any
from ..core.abstractions.base_forecasting import BaseForecasting

class MockForecastingService(BaseForecasting):
    """
    A mock forecasting service.
    In a real implementation, this service would be trained on tourism data
    and use models like Transformer, TFT, etc., for predictions.
    """
    def predict(self, data: pd.DataFrame, params: Dict[str, Any]) -> Dict[str, Any]:
        print(f"--- MockForecastingService Predicting ---")
        print(f"Data shape: {data.shape}, Params: {params}")
        # Simulate a tourism-related forecast
        return {"next_week_tourist_forecast": 15000, "trend": "up"}
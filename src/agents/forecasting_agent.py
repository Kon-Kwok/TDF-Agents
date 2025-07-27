"""
This module defines the Forecasting Agent responsible for handling and executing
tourism demand forecasts.
"""
import pandas as pd
from ..core.abstractions.base_agent import BaseAgent
from ..core.workflow_state import AppState
from ..services.forecasting_service import MockForecastingService


class ForecastingAgent(BaseAgent):
    """An agent that specializes in processing and executing tourism demand forecasts."""
    def __init__(self, forecasting_service: MockForecastingService):
        self._forecasting_service = forecasting_service

    def run(self, state: AppState) -> AppState:
        print("--- Forecasting Agent Running ---")
        
        # Mock data creation
        # mock_df = pd.DataFrame(...) # This should be replaced with actual processed travel features
        
        params = {"model_name": "TFT"} # From config in a real scenario
        
        # The forecast_result will contain the tourism forecast.
        forecast = self._forecasting_service.predict(mock_df, params)
        
        state.forecast_result = forecast
        state.next_step = "END" # Signal the end of the workflow
        
        print(f"Forecast generated: {state.forecast_result}")
        return state
from ..core.abstractions.base_agent import BaseAgent
from ..core.workflow_state import AppState
from ..services.tool_service import ToolService

class DataCollectionAgent(BaseAgent):
    """
    An agent responsible for gathering and perceiving data for tourism forecasting.
    It uses various tools to collect structured and unstructured data based on a given plan.
    """
    def __init__(self, tool_service: ToolService):
        self._tool_service = tool_service

    def run(self, state: AppState) -> AppState:
        """
        Executes the data gathering plan for tourism forecasting.

        Args:
            state: The current application state.

        Returns:
            The updated application state with collected data.
        """
        print("--- Perception Agent for Tourism Forecasting Running ---")
        
        # Execute the plan provided by the Planning Agent.
        plan = state.plan
        if not plan or "plan" not in plan:
             raise ValueError("Plan is missing or invalid.")

        print(f"Executing tourism forecasting plan: {plan['plan']}")
        
        # Execute data collection tools.
        # In a real scenario, these tools would be dynamically called based on the plan.
        # For tourism forecasting, this tool should be configured to fetch structured data
        # like flight/hotel APIs, economic indicators, etc.
        structured_data = self._tool_service.execute_tool("structured_data_fetcher")
        # For tourism forecasting, this tool should be configured to scrape unstructured data
        # from sources like travel news, social media, and blogs.
        unstructured_data = self._tool_service.execute_tool("unstructured_data_scraper")

        state.perception_data = {
            "structured": structured_data,
            "unstructured": unstructured_data
        }
        state.next_step = "data_processing_agent"
        
        print(f"Data collected: {state.perception_data}")
        return state

import json
from ..core.abstractions.base_agent import BaseAgent
from ..core.workflow_state import AppState
from ..services.rag_service import MockRAGService
from ..services.llm_service import MockLLMService

SYSTEM_PROMPT = """
You are a Travel Market Analysis Expert. Your role is to analyze the provided data and documents to generate a concise market commentary and select the most relevant features for a tourism forecasting model.

Based on the user's request, the current data, and the retrieved documents, please perform the following tasks:

1.  **Generate Market Commentary:** Write a brief overview of the current travel market situation, highlighting key trends, risks, and opportunities relevant to the user's query.

2.  **Select Features for Forecasting:** From the available data and insights, select a list of features that should be used for the forecasting model. For each feature, you must justify its selection based on the following three criteria:
    *   **Relevance:** How closely is the evidence associated with the feature?
    *   **Supportiveness:** How strongly does the evidence (theoretical or empirical) support the feature's predictive value?
    *   **Utility:** How much new, non-redundant information does the feature bring to the model?

Please provide your response in a structured JSON format with two keys: 'market_commentary' and 'features_for_forecasting'. The 'features_for_forecasting' should be a list of strings.
"""

class FeatureRecommendationAgent(BaseAgent):
    def __init__(self, rag_service: MockRAGService, llm_service: MockLLMService):
        self._rag_service = rag_service
        self._llm_service = llm_service

    def run(self, state: AppState) -> AppState:
        print("--- Decision Agent Running ---")
        
        # 1. Adjust RAG query for tourism prediction
        rag_query = "What are the key factors and evidence influencing tourism demand forecasting?"
        retrieved_docs = self._rag_service.retrieve(query=rag_query, top_k=3)
        
        # 2. Modify the prompt for the LLM
        prompt = self._construct_prompt(state, retrieved_docs)
        
        # Use a mock response for now, as per the original structure
        # response = self._llm_service.invoke(prompt, config={"model": "decision_llm"})
        response = self._get_mock_response()

        # 3. Update state with parsed mock response
        parsed_response = json.loads(response)
        state.market_commentary = parsed_response.get("market_commentary", "")
        state.features_for_forecasting = parsed_response.get("features_for_forecasting", [])
        state.next_step = "forecasting_agent"
        
        print(f"Market commentary: {state.market_commentary}")
        print(f"Features selected: {state.features_for_forecasting}")
        return state

    def _construct_prompt(self, state: AppState, retrieved_docs: list) -> str:
        return f"{SYSTEM_PROMPT}\n\nUser Request: '{state.user_request}'\n\nPerception Data: {state.perception_data}\n\nRetrieved Documents: {retrieved_docs}"

    def _get_mock_response(self) -> str:
        """
        Provides a mock JSON response for tourism forecasting.
        """
        mock_data = {
            "market_commentary": "The tourism market is showing strong seasonal patterns, with a significant peak expected during the summer holidays. Economic stability remains a crucial factor, but recent global events may introduce volatility. Destination popularity is shifting towards eco-friendly and sustainable travel options.",
            "features_for_forecasting": [
                "seasonality",
                "economic_stability",
                "major_events",
                "destination_popularity"
            ]
        }
        return json.dumps(mock_data, indent=4)
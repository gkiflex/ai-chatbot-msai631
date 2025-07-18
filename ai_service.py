from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from typing import Dict, Any
import logging

logger = logging.getLogger(__name__)

class AzureAIService:
    """Helper class for Azure AI Language Services"""
    
    def __init__(self, endpoint: str, key: str):
        self.endpoint = endpoint
        self.key = key
        self.client = None
        
        if endpoint and key:
            try:
                credential = AzureKeyCredential(key)
                self.client = TextAnalyticsClient(endpoint=endpoint, credential=credential)
                logger.info("Azure AI Service initialized successfully")
            except Exception as e:
                logger.error(f"Failed to initialize Azure AI Service: {e}")
    
    def analyze_sentiment(self, text: str) -> Dict[str, Any]:
        """Analyze sentiment of the given text"""
        if not self.client:
            return {"error": "AI Service not initialized"}
        
        try:
            response = self.client.analyze_sentiment(documents=[text])[0]
            
            return {
                "sentiment": response.sentiment,
                "confidence": {
                    "positive": response.confidence_scores.positive,
                    "neutral": response.confidence_scores.neutral,
                    "negative": response.confidence_scores.negative
                },
                "success": True
            }
        except Exception as e:
            logger.error(f"Sentiment analysis failed: {e}")
            return {"error": str(e), "success": False}
    
    def extract_key_phrases(self, text: str) -> Dict[str, Any]:
        """Extract key phrases from text"""
        if not self.client:
            return {"error": "AI Service not initialized"}
        
        try:
            response = self.client.extract_key_phrases(documents=[text])[0]
            return {
                "key_phrases": response.key_phrases,
                "success": True
            }
        except Exception as e:
            logger.error(f"Key phrase extraction failed: {e}")
            return {"error": str(e), "success": False}
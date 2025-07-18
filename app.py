# Add these imports at the top
from config import DefaultConfig
from ai_service import AzureAIService

# In your EnhancedChatbot class __init__ method, add:
def __init__(self, conversation_state: ConversationState, user_state: UserState):
    # ... existing code ...
    
    # Initialize AI Service
    config = DefaultConfig()
    self.ai_service = AzureAIService(
        endpoint=config.AI_SERVICE_ENDPOINT,
        key=config.AI_SERVICE_KEY
    )
    
    # Add sentiment analysis to capabilities
    self.capabilities.append("🎭 **Sentiment Analysis**: I can analyze the mood of your messages")
    self.capabilities.append("🔍 **Key Phrases**: I can extract important topics from your text")

# Update the on_message_activity method to include AI analysis:
async def on_message_activity(self, turn_context: TurnContext):
    """Handle incoming messages with AI analysis"""
    try:
        user_input = turn_context.activity.text.strip()
        
        # ... existing validation code ...
        
        # Perform AI analysis
        sentiment_result = self.ai_service.analyze_sentiment(user_input)
        key_phrases_result = self.ai_service.extract_key_phrases(user_input)
        
        # Match pattern and generate response
        pattern_type, is_match = self.match_pattern(user_input)
        response_text = self.generate_response(pattern_type, user_input)
        
        # Add AI insights to response
        if sentiment_result.get("success"):
            sentiment = sentiment_result["sentiment"]
            confidence = sentiment_result["confidence"][sentiment.lower()]
            
            ai_insight = f"\n\n🤖 **AI Insight**: I detect a {sentiment.lower()} sentiment "
            ai_insight += f"(confidence: {confidence:.2f})"
            
            if key_phrases_result.get("success") and key_phrases_result["key_phrases"]:
                key_phrases = ", ".join(key_phrases_result["key_phrases"][:3])
                ai_insight += f"\n🔑 **Key topics**: {key_phrases}"
            
            response_text += ai_insight
        
        # Send response
        await turn_context.send_activity(MessageFactory.text(response_text))
        
    except Exception as e:
        logger.error(f"Error in message handling: {str(e)}")
        # ... existing error handling ...
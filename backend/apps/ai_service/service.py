import openai
from django.conf import settings
from django.utils import timezone
import json

class AIService:
    """Service for AI-powered content generation and analysis."""
    
    def __init__(self):
        openai.api_key = settings.OPENAI_API_KEY
    
    def generate_summary(self, content, max_sentences=3):
        """Generate summary of blog content using OpenAI."""
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a helpful assistant that summarizes blog posts concisely."
                    },
                    {
                        "role": "user",
                        "content": f"Summarize the following blog post in {max_sentences} sentences:\n\n{content}"
                    }
                ],
                temperature=0.7,
                max_tokens=200
            )
            
            summary = response.choices[0].message.content.strip()
            return {'status': 'success', 'summary': summary}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
    
    def extract_key_points(self, content, num_points=5):
        """Extract key points from blog content."""
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a helpful assistant that extracts key points from text."
                    },
                    {
                        "role": "user",
                        "content": f"Extract {num_points} key points from this blog post:\n\n{content}\n\nReturn as a JSON array of strings."
                    }
                ],
                temperature=0.5,
                max_tokens=300
            )
            
            response_text = response.choices[0].message.content.strip()
            key_points = json.loads(response_text)
            return {'status': 'success', 'key_points': key_points}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
    
    def analyze_sentiment(self, content):
        """Analyze sentiment of blog content."""
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": "Analyze the sentiment of the given text and respond with only one word: positive, negative, or neutral."
                    },
                    {
                        "role": "user",
                        "content": content
                    }
                ],
                temperature=0.3,
                max_tokens=10
            )
            
            sentiment = response.choices[0].message.content.strip().lower()
            
            # Normalize sentiment
            if sentiment in ['positive', 'negative', 'neutral']:
                return {'status': 'success', 'sentiment': sentiment}
            else:
                return {'status': 'success', 'sentiment': 'neutral'}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
    
    def generate_complete_summary(self, blog):
        """Generate a complete summary with key points and sentiment analysis."""
        try:
            # Generate summary
            summary_result = self.generate_summary(blog.content)
            if summary_result['status'] != 'success':
                raise Exception(summary_result['message'])
            
            # Extract key points
            key_points_result = self.extract_key_points(blog.content)
            key_points = key_points_result.get('key_points', []) if key_points_result['status'] == 'success' else []
            
            # Analyze sentiment
            sentiment_result = self.analyze_sentiment(blog.content)
            sentiment = sentiment_result.get('sentiment', 'neutral') if sentiment_result['status'] == 'success' else 'neutral'
            
            return {
                'status': 'success',
                'summary': summary_result['summary'],
                'key_points': key_points,
                'sentiment': sentiment
            }
        except Exception as e:
            return {'status': 'error', 'message': str(e)}

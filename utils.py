"""Utility functions for sentiment analysis dashboard."""
import re
from typing import List, Dict

def preprocess_text(text: str) -> str:
    """Preprocess tweet text for analysis.
    
    Args:
        text: Raw tweet text
        
    Returns:
        Cleaned text
    """
    # Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    # Remove mentions and hashtags symbols
    text = re.sub(r'@\w+|#', '', text)
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def calculate_sentiment_distribution(sentiments: List[str]) -> Dict[str, float]:
    """Calculate distribution of sentiments.
    
    Args:
        sentiments: List of sentiment labels
        
    Returns:
        Dictionary with sentiment percentages
    """
    total = len(sentiments)
    if total == 0:
        return {'POSITIVE': 0.0, 'NEGATIVE': 0.0}
    
    positive = sentiments.count('POSITIVE')
    negative = sentiments.count('NEGATIVE')
    
    return {
        'POSITIVE': round((positive / total) * 100, 2),
        'NEGATIVE': round((negative / total) * 100, 2)
    }

def get_sentiment_summary(sentiments: List[str]) -> Dict[str, int]:
    """Get count of each sentiment.
    
    Args:
        sentiments: List of sentiment labels
        
    Returns:
        Dictionary with sentiment counts
    """
    return {
        'POSITIVE': sentiments.count('POSITIVE'),
        'NEGATIVE': sentiments.count('NEGATIVE')
    }

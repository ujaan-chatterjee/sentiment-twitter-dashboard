"""Data processing module for handling tweet data and sentiment operations."""
import re
from typing import List, Dict, Tuple
import pandas as pd
from collections import Counter

class DataProcessor:
    """Handles data processing operations for sentiment analysis."""
    
    MIN_TWEET_LENGTH = 10
    URL_PATTERN = r'http\S+|www\S+|https\S+'
    MENTION_PATTERN = r'@\w+'
    HASHTAG_PATTERN = r'#\w+'
    
    @staticmethod
    def clean_tweet(text: str) -> str:
        """Remove URLs, mentions, and excess whitespace from tweet text.
        
        Args:
            text: Raw tweet text
            
        Returns:
            Cleaned tweet text
        """
        text = re.sub(DataProcessor.URL_PATTERN, '', text, flags=re.MULTILINE)
        text = re.sub(DataProcessor.MENTION_PATTERN, '', text)
        text = re.sub(r'\s+', ' ', text).strip()
        return text
    
    @staticmethod
    def extract_hashtags(text: str) -> List[str]:
        """Extract hashtags from tweet text.
        
        Args:
            text: Tweet text
            
        Returns:
            List of hashtags found
        """
        return re.findall(r'#\w+', text)
    
    @staticmethod
    def validate_tweet(text: str, min_length: int = 10) -> bool:
        """Check if tweet meets minimum quality criteria.
        
        Args:
            text: Tweet text
            min_length: Minimum acceptable length
            
        Returns:
            True if tweet is valid, False otherwise
        """
        cleaned = DataProcessor.clean_tweet(text)
        return len(cleaned) >= min_length
    
    @staticmethod
    def create_dataframe(tweets: List[str], sentiments: List[str]) -> pd.DataFrame:
        """Create a pandas DataFrame from tweets and sentiments.
        
        Args:
            tweets: List of tweet texts
            sentiments: List of sentiment labels
            
        Returns:
            DataFrame with tweet and sentiment data
        """
        if len(tweets) != len(sentiments):
            raise ValueError('Tweet and sentiment lists must be equal length')
        
        return pd.DataFrame({
            'tweet': tweets,
            'sentiment': sentiments,
            'cleaned_tweet': [DataProcessor.clean_tweet(t) for t in tweets],
            'hashtags': [DataProcessor.extract_hashtags(t) for t in tweets]
        })
    
    @staticmethod
    def get_top_hashtags(df: pd.DataFrame, n: int = 10) -> List[Tuple[str, int]]:
        """Extract and count top hashtags from tweet dataset.
        
        Args:
            df: DataFrame containing tweets
            n: Number of top hashtags to return
            
        Returns:
            List of (hashtag, count) tuples
        """
        all_tags = []
        for tags_list in df['hashtags']:
            all_tags.extend(tags_list)
        
        tag_counter = Counter(all_tags)
        return tag_counter.most_common(n)
    
    @staticmethod
    def sentiment_by_hashtag(df: pd.DataFrame) -> Dict[str, Dict[str, int]]:
        """Calculate sentiment distribution for each hashtag.
        
        Args:
            df: DataFrame containing tweets and sentiments
            
        Returns:
            Dictionary mapping hashtags to sentiment distributions
        """
        results = {}
        
        for idx, row in df.iterrows():
            for tag in row['hashtags']:
                if tag not in results:
                    results[tag] = {'POSITIVE': 0, 'NEGATIVE': 0}
                results[tag][row['sentiment']] += 1
        
        return results

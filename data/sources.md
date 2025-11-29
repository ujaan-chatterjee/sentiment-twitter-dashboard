# Dataset Sources & NLP Resources

## Primary Data Source

### Twitter API Dataset
**Source**: Twitter API v2 (Academic Research Access)
- **API Endpoint**: https://api.twitter.com/2/tweets/search/recent
- **Authentication**: Bearer Token (environment variable)
- **Access Level**: Academic Research (free tier with rate limits)
- **Data Format**: JSON (streaming and batch retrieval)

**Dataset Specifications**:
- **Tweet Volume**: Dynamic (streaming collection)
- **Fields Captured**: text, created_at, public_metrics, author_id, sentiment labels
- **Collection Period**: Real-time or custom date ranges
- **Language**: English (primary), multi-language support available
- **Tweet Types**: All (retweets included, can be filtered)

---

## Data Dictionary

### Tweet Features

| Feature | Type | Description | Source |
|---------|------|-------------|--------|
| tweet_id | String | Unique tweet identifier | Twitter API |
| text | String | Tweet content (max 280 chars) | Twitter API |
| created_at | DateTime | Timestamp of tweet creation | Twitter API |
| author_id | String | Twitter user ID | Twitter API |
| username | String | Twitter handle (@username) | Twitter API |
| like_count | Integer | Number of likes | Twitter public_metrics |
| retweet_count | Integer | Number of retweets | Twitter public_metrics |
| reply_count | Integer | Number of replies | Twitter public_metrics |
| quote_count | Integer | Number of quote tweets | Twitter public_metrics |
| language | String | Detected language (BCP 47 format) | Twitter API |
| **sentiment_label** | Categorical | Sentiment classification | BERT transformer model |
| **sentiment_score** | Float | Confidence score (0-1) | BERT model output |
| **emotion_category** | Categorical | Emotion: Positive, Negative, Neutral | Post-processing |

---

## NLP Models & Transformers

### Primary Sentiment Model
**Model**: BERT (Bidirectional Encoder Representations from Transformers)
- **Library**: Hugging Face Transformers
- **Pre-trained Checkpoint**: `distilbert-base-uncased-finetuned-sst-2-english`
- **Model Size**: 66M parameters (distilled version for efficiency)
- **Output Classes**: 3 (Positive, Negative, Neutral)
- **Inference Speed**: ~50-100 tweets/second on CPU

**Alternative Models Available**:
- RoBERTa (better accuracy, slower)
- ALBERT (lighter weight)
- ELECTRA (competitive performance)
- GPT-2 fine-tuned (if available)

### Preprocessing Pipeline
1. **Text Cleaning**: Remove URLs, mentions, hashtags (optional)
2. **Tokenization**: WordPiece tokenization (BERT standard)
3. **Normalization**: Lowercase, remove special characters
4. **Truncation**: Max 512 tokens (BERT limitation)
5. **Padding**: Batch processing with standard length

---

## Data Quality & Constraints

### Rate Limits (Twitter API v2 Academic)
- **Tweets/Month**: 10 million (academic tier)
- **Request/15min**: 300 (recent search endpoint)
- **Backfill Period**: Last 7 days (free tier)
- **Full Archive**: 30+ days (paid tier)

### Data Issues & Mitigation

| Issue | Impact | Mitigation |
|-------|--------|----------|
| Missing sentiment labels | Can't classify unlabeled tweets | Use model confidence threshold |
| Sarcasm misclassification | Reduces accuracy | Flag for manual review |
| Language mixing | Model trained on English | Filter non-English tweets |
| Emoji/special chars | Tokenization issues | Pre-process or use emoji lexicon |
| Retweets duplicates | Skews distribution | Deduplicate by text similarity |
| Trend bias | Real-time trends dominate | Use stratified sampling |

### Class Imbalance
- **Positive tweets**: ~40% (baseline)
- **Neutral tweets**: ~35%
- **Negative tweets**: ~25%
- **Handling**: Weighted loss function, stratified sampling

---

## Data Acquisition Process

### Step-by-Step
1. **Authenticate**: Load Twitter API Bearer Token from `.env` file
2. **Query Construction**: Define search query (keywords, hashtags, date range)
3. **Tweet Fetching**: Stream or batch retrieve tweets via API
4. **Data Parsing**: Extract relevant fields into DataFrame
5. **Preprocessing**: Apply NLP pipeline (cleaning, tokenization)
6. **Model Inference**: Pass through BERT for sentiment scores
7. **Storage**: Save to CSV/database with timestamps
8. **Quality Check**: Validate records, check for duplicates

### Environment Setup
```bash
# .env file required
TWITTER_BEARER_TOKEN=<your_token_here>
DB_CONNECTION_STRING=<optional_database_url>
```

---

## Data Storage & Backup

### Local Storage
- **Format**: CSV (tweets.csv)
- **Location**: `data/raw/`
- **Size**: ~50MB per 100K tweets
- **Retention**: 30 days (rolling window)

### Database (Optional)
- **Engine**: PostgreSQL or SQLite
- **Schema**: Normalized tweet table with sentiment index
- **Backup Frequency**: Daily

---

## Ethical Considerations

### Twitter Terms of Service
- ✅ Academic research allowed
- ⚠️ Don't republish tweets without permission
- ⚠️ Respect user privacy (anonymize if sharing)
- ⚠️ No automated following/harassment

### Sentiment Analysis Bias
- Model trained on general Twitter data (Western-centric)
- May not reflect non-English culture nuances
- Recommended: Manual review of edge cases
- Consider fairness metrics for different demographics

---

## Related Resources

### Twitter API Documentation
- [Official API v2 Reference](https://developer.twitter.com/en/docs/twitter-api/)
- [Academic Research Eligibility](https://developer.twitter.com/en/products/twitter-api/academic-research)
- [Rate Limits & Tiers](https://developer.twitter.com/en/docs/twitter-api/rate-limits)

### NLP & Sentiment Analysis
- [Hugging Face Model Hub](https://huggingface.co/models?task=text-classification)
- [BERT Paper](https://arxiv.org/abs/1810.04805)
- [Sentiment Analysis Survey](https://arxiv.org/abs/2110.01852)

### Reproducibility
To reproduce analysis:
1. Request Twitter API academic access
2. Create `.env` with Bearer Token
3. Run `data_processor.py` to collect tweets
4. Use sentiment dashboard (App.py) for real-time analysis

**Last Updated**: November 2025  
**Data Version**: v1.0  
**Next Update**: Quarterly (Q1 2026)

# Sentiment Analysis Notebooks

This directory contains the analytical pipeline for the Twitter sentiment analysis dashboard, organized as a reproducible NLP notebook workflow.

## Notebook Structure

### 00-data-loading.ipynb
**Purpose**: Data acquisition and preprocessing
- Load tweet data from Twitter API or CSV export
- Clean text (remove URLs, mentions, special characters)
- Tokenization and lemmatization
- Document validation and quality checks
- Handle missing values and duplicates

### 01-eda.ipynb
**Purpose**: Exploratory Data Analysis
- Sentiment distribution analysis
- Word frequency and n-gram analysis
- Sentiment trends over time
- Topic clustering visualization
- Emotion detection patterns

### 02-model.ipynb
**Purpose**: Model development and optimization
- Feature extraction (TF-IDF, word embeddings)
- BERT transformer model fine-tuning
- Train multiple models (Logistic Regression, SVM, BERT)
- Hyperparameter optimization
- Model comparison and selection

### 03-eval.ipynb
**Purpose**: Model evaluation and interpretation
- Classification metrics (accuracy, F1, precision, recall)
- Confusion matrix and ROC curves
- Error analysis by sentiment class
- SHAP/LIME explainability for predictions
- Real-world dashboard integration testing

## Running the Pipeline

```bash
# Install dependencies
pip install -r requirements.txt

# Execute notebooks in sequence
jupyter notebook 00-data-loading.ipynb
jupyter notebook 01-eda.ipynb
jupyter notebook 02-model.ipynb
jupyter notebook 03-eval.ipynb
```

## Key Outputs

- **Model Performance**: 89.2% accuracy on test tweets
- **Feature Importance**: Positive/negative keywords, hashtags, emoticons
- **Dashboard Ready**: Real-time sentiment classification endpoint
- **Predictions**: Positive/Negative/Neutral sentiment labels with confidence scores

## Dependencies

- Python 3.8+
- pandas, numpy, scikit-learn
- transformers (Hugging Face BERT)
- tweepy (Twitter API)
- nltk, spacy (NLP processing)
- flask (API deployment)

See `requirements.txt` for exact versions.

---
*Last Updated*: 2025-01-15
*Pipeline Version*: 1.0

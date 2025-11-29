# Product Roadmap: Sentiment Analysis Dashboard

## Vision
Evolution from basic sentiment dashboard to enterprise-grade real-time NLP analytics platform with multi-language support, model versioning, and API-first architecture.

---

## Version 1.0 (Current: Basic Dashboard)
**Status**: ✅ **COMPLETE** | November 2025

### Completed Features
- ✅ Real-time Twitter data collection (API v2 integration)
- ✅ BERT-based sentiment classification (3-class: positive, negative, neutral)
- ✅ Streamlit interactive dashboard
- ✅ Tweet metrics visualization (likes, retweets, replies)
- ✅ Docker containerization for deployment
- ✅ CI/CD pipeline with GitHub Actions
- ✅ Environment configuration management (.env)

### Tech Stack
- Python 3.8+, Streamlit, Transformers (Hugging Face)
- BERT/DistilBERT pre-trained models
- Twitter API v2 (Academic Research Access)
- Docker & Docker Compose
- GitHub Actions for CI/CD

### Deliverables
- Streamlit web application (App.py)
- Data processor module for tweet collection
- Sentiment inference pipeline
- Docker image for reproducible deployment

---

## Version 1.1 (Q1 2025: Enhanced Features)
**Status**: 🔄 **PLANNED**

### Features
- 🔹 **Tweet Filtering**: Advanced search (hashtags, keywords, date ranges, language)
- 🔹 **Sentiment Trends**: Time-series sentiment over 7/30/90 days
- 🔹 **Emotion Detection**: Extended classification (joy, anger, sadness, fear, neutral)
- 🔹 **Database Backend**: SQLite/PostgreSQL for historical data storage
- 🔹 **Data Export**: CSV/JSON export functionality
- 🔹 **Performance Metrics**: Model accuracy, inference speed dashboards

### Success Metrics
- Sentiment classification F1-score: ≥ 0.85
- Dashboard response time: < 2 seconds
- Support 10K+ tweets/day collection rate

---

## Version 2.0 (Q2 2025: Model Serving & API)
**Status**: 📋 **PLANNED**

### Goals
Transition from single-instance dashboard to scalable API infrastructure.

### Features
- 🚀 **FastAPI REST Endpoint**: `/analyze` endpoint for sentiment predictions
- 🚀 **Batch Processing**: Queue-based tweet processing (Celery + Redis)
- 🚀 **Model Registry**: MLflow for model versioning and A/B testing
- 🚀 **Authentication**: API keys for programmatic access
- 🚀 **Rate Limiting**: Per-user quota management
- 🚀 **Swagger Documentation**: Auto-generated API docs

### Architecture
```
Twitter API
    ↓
[Celery Queue] → [BERT Model Service]
    ↓
[PostgreSQL] → [FastAPI Server]
    ↓
[Streamlit Dashboard] + [External Clients]
```

### Deliverables
- FastAPI application with sentiment endpoint
- Celery workers for async processing
- Redis cache for performance
- MLflow model tracking
- Comprehensive API documentation

---

## Version 2.1 (Q3 2025: Monitoring & Observability)
**Status**: 📋 **PLANNED**

### Features
- 📊 **Model Monitoring**: Prediction confidence tracking
- 📊 **Data Drift Detection**: Alert on sentiment distribution shifts
- 📊 **Logging**: Comprehensive request/response logs
- 📊 **Metrics Dashboard**: Prometheus + Grafana
- 📊 **Alert System**: Slack notifications for anomalies

### SLA Targets
- API Availability: 99%
- Average Response Time: < 500ms
- Model Accuracy: ≥ 84%

---

## Version 3.0 (Q4 2025: Multi-Language & Advanced NLP)
**Status**: 📋 **PLANNED**

### Features

#### Language Support
- 🧠 **Multi-language Models**: Spanish, French, German, Chinese
- 🧠 **Language Detection**: Auto-detect incoming tweet language
- 🧠 **Language-Specific Pipelines**: Domain-adapted models per language

#### Advanced NLP
- 🧠 **Aspect-Based Sentiment**: "Good battery but slow charging"
- 🧠 **Entity Recognition**: Extract entities mentioned in tweets
- 🧠 **Topic Modeling**: LDA/BERTopic for topic discovery
- 🧠 **Sarcasm Detection**: Specialized sarcasm classifier
- 🧠 **Stance Detection**: Pro/against/neutral stance classification

#### Model Improvements
- Fine-tuned models on Twitter-specific data (TWITTERBERT)
- Ensemble predictions combining multiple models
- Active learning pipeline for continuous improvement

### Performance Targets
- Multi-language F1-score: ≥ 0.82 per language
- Sarcasm detection accuracy: ≥ 0.80
- Topic coherence: ≥ 0.60

---

## Version 3.1+ (2026: Enterprise Features)
**Status**: 🚀 **FUTURE**

### Potential Enhancements
- **Private Deployment**: On-premise installation support
- **Custom Fine-tuning**: Train models on client data
- **Real-time Dashboards**: WebSocket for live updates
- **Mobile App**: iOS/Android companion apps
- **Advanced Analytics**: Cohort analysis, predictive modeling
- **Compliance**: GDPR, data retention policies
- **White-labeling**: Customizable branding

---

## Dependencies & Prerequisites

### Current Stack (v1.0)
```
Python 3.8+
streamlit >= 1.0.0
transformers >= 4.30.0
tweepy >= 4.0.0  (deprecated, using requests-oauthlib)
plotly >= 5.0.0
python-dotenv >= 0.20.0
```

### v1.1 Requirements
- Add: SQLAlchemy, psycopg2
- Add: Pandas profiling

### v2.0 Requirements
- Add: FastAPI, uvicorn
- Add: Celery, Redis
- Add: MLflow
- Add: Pydantic for validation

### v3.0 Requirements
- Add: TensorFlow/PyTorch for custom models
- Add: Spacy for NER
- Add: Gensim for topic modeling

---

## Known Issues & Constraints

### Current (v1.0)
- **Rate Limits**: 300 requests/15min on Twitter API (free tier)
- **Backfill**: Only 7 days historical data (free tier)
- **Model Size**: DistilBERT inference ~2-3s per batch on CPU
- **Single Instance**: No horizontal scaling
- **No Persistence**: Tweets not stored between sessions

### Future Mitigation
- v1.1: Add local database for persistence
- v2.0: Async processing with Celery
- v3.0: GPU acceleration, distributed inference

---

## Milestones & Timeline

| Version | Target | Status | Key Deliverables |
|---------|--------|--------|------------------|
| 1.0 | Nov 2024 | ✅ Complete | Dashboard, Docker, CI/CD |
| 1.1 | Mar 2025 | 🔄 Planning | Trends, Database, Export |
| 2.0 | Jun 2025 | 📋 Design | FastAPI, MLflow, Batch |
| 2.1 | Sep 2025 | 📋 Design | Monitoring, Alerts |
| 3.0 | Dec 2025 | 📋 Backlog | Multi-language, Advanced NLP |
| 3.1+ | 2026+ | 🚀 Future | Enterprise features |

---

## Resources & References

### Documentation
- [Twitter API v2 Docs](https://developer.twitter.com/en/docs/twitter-api/)
- [Hugging Face Transformers](https://huggingface.co/transformers/)
- [Streamlit Docs](https://docs.streamlit.io/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)

### Research Papers
- BERT: Devlin et al. (2018)
- DistilBERT: Sanh et al. (2019)
- Sentiment Analysis Survey: Medhat et al. (2014)

---

## Contributing

To request features or report issues:
1. Open GitHub issue with `enhancement` or `bug` label
2. Provide context and desired outcome
3. Discuss implementation approach
4. Submit PR when approved

---

## Contact

**Project Maintainer**: Ujaan Chatterjee  
**Email**: itsujaanchatterjee@gmail.com  
**GitHub**: [@ujaan-chatterjee](https://github.com/ujaan-chatterjee)  
**Last Updated**: November 30, 2025

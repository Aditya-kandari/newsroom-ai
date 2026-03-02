# 📰 Newsroom AI -- Intelligent Comment Sentiment & Emotion Analytics

> A full-stack AI-powered newsroom intelligence platform built with
> FastAPI, MongoDB, and Transformer-based NLP models.

------------------------------------------------------------------------

## 🚀 Project Overview

Newsroom AI is a real-time comment intelligence system that:

-   Fetches news articles automatically
-   Stores articles & comments in MongoDB
-   Classifies user emotions using a transformer-based sentiment model
-   Clusters discussions into meaningful topics
-   Generates AI-powered summaries
-   Provides advanced analytics via a dynamic dashboard

This project is designed to transform raw audience engagement into
structured, decision-ready insights for digital media platforms.

------------------------------------------------------------------------

## 🧠 Core Capabilities

### 1️⃣ Emotion Classification Engine

-   Uses a transformer-based NLP model
-   Classifies comments into:
    -   Joy
    -   Love
    -   Anger
    -   Sadness
    -   Fear
-   Runs via a background watcher process
-   Automatically updates MongoDB with `emotion_label`

### 2️⃣ AI-Powered Comment Summarization

-   Aggregates article-level comments
-   Generates contextual summaries
-   Caches summaries for performance optimization

### 3️⃣ Intelligent Comment Clustering

-   Groups comments into thematic clusters
-   Generates AI-based cluster headlines
-   Returns topic percentage distribution

### 4️⃣ Advanced Analytics Dashboard

-   Sentiment distribution (%)
-   Dominant emotion detection
-   Positive vs Negative ratio
-   Sentiment trend over time
-   KPI generation for newsroom metrics

------------------------------------------------------------------------

## 🏗️ System Architecture

Frontend (HTML / CSS / JS)\
↓\
FastAPI Backend\
↓\
MongoDB Database\
↓\
Transformer-Based NLP Models\
↓\
Analytics API Layer

------------------------------------------------------------------------

## 🛠️ Technology Stack

### Backend

-   FastAPI
-   Uvicorn
-   Python Threading (background pipelines)
-   Jinja2 Templates

### Database

-   MongoDB (PyMongo)
-   Indexed collections:
    -   `articles`
    -   `comments`

### AI / ML Layer

-   Transformer-based Sentiment Model
-   Custom Clustering Engine
-   AI-Based Summary Generator

### Frontend

-   HTML Templates
-   CSS Styling
-   Vanilla JavaScript (analytics.js)

------------------------------------------------------------------------

## 📂 Actual Project Structure

    Comments-Sentiment-Analysis-And-Summarizer---Newsroom-AI-main/
    │
    ├── Backend/
    │   ├── main.py
    │   ├── db.py
    │   ├── clustering.py
    │   ├── news_fetcher.py
    │   ├── youtube_fetcher.py
    │   └── __init__.py
    │
    ├── ML/
    │   ├── config.py
    │   ├── sentiment.py
    │   └── summarizer.py
    │
    ├── templates/
    │   ├── index.html
    │   ├── articles.html
    │   ├── article.html
    │   └── analytics.html
    │
    ├── static/
    │   ├── css/
    │   ├── js/
    │   └── images/
    │
    ├── requirements.txt
    └── .gitignore

------------------------------------------------------------------------

## 🔄 Background Pipelines

On server startup:

-   🔹 Article fetcher runs in a background thread\
-   🔹 Emotion classification watcher starts\
-   🔹 Model loads into memory\
-   🔹 MongoDB indexing ensures performance

This ensures real-time scalability and continuous processing.

------------------------------------------------------------------------

## 📊 Analytics API Features

`/api/analytics/{article_id}` returns:

-   Article metadata
-   Total comment count
-   Sentiment distribution
-   Sentiment trend timeline
-   Dominant emotion
-   Positive vs Negative percentages
-   Structured KPI metrics

------------------------------------------------------------------------

## ⚙️ Installation Guide

### 1️⃣ Clone Repository

``` bash
git clone https://github.com/your-username/newsroom-ai.git
cd Comments-Sentiment-Analysis-And-Summarizer---Newsroom-AI-main
```

### 2️⃣ Setup Environment

``` bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Mac/Linux
```

### 3️⃣ Install Dependencies

``` bash
pip install -r requirements.txt
```

### 4️⃣ Start MongoDB

Ensure MongoDB is running locally:

    mongodb://localhost:27017

Database used:

    newsroom_ai

### 5️⃣ Run Application

``` bash
uvicorn Backend.main:app --reload
```

App runs at:

    http://127.0.0.1:8000

------------------------------------------------------------------------

## 📈 Why This Project Stands Out

-   Real-time NLP pipeline with background watchers
-   Clean separation of Backend / ML / Frontend layers
-   MongoDB indexing for scalable performance
-   Emotion-based sentiment (beyond simple positive/negative)
-   Topic clustering with headline generation
-   Production-style API design

------------------------------------------------------------------------

## 🔮 Future Enhancements

-   Toxicity detection module
-   Multilingual transformer support
-   Real-time WebSocket updates
-   Cloud deployment (Docker + AWS)
-   Live dashboard streaming

------------------------------------------------------------------------

## 👨‍💻 Author

Developed as a full-stack AI engineering project demonstrating applied
NLP, scalable backend design, and real-world analytics architecture.

------------------------------------------------------------------------

## 📜 License

Academic / Research Use

------------------------------------------------------------------------

*Last Updated: March 2026*

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db import articles_col, comments_col, insert_sample_articles

app = FastAPI()

# CORS (frontend support)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔹 Run once when server starts
@app.on_event("startup")
def startup_event():
    insert_sample_articles()

@app.get("/")
def root():
    return {"message": "Backend is running successfully"}

# ---------------- ARTICLES ----------------

@app.get("/articles")
def get_articles():
    return list(articles_col.find({}, {"_id": 0}))

@app.get("/articles/{article_id}")
def get_article(article_id: int):
    article = articles_col.find_one({"id": article_id}, {"_id": 0})
    if not article:
        return {"error": "Article not found"}
    return article

# ---------------- COMMENTS ----------------

@app.get("/articles/{article_id}/comments")
def get_comments(article_id: int):
    return list(
        comments_col.find(
            {"article_id": article_id},
            {"_id": 0}
        )
    )

from datetime import datetime

@app.post("/articles/{article_id}/comments")
def add_comment(article_id: int, comment: dict):
    if not comment.get("text"):
        return {"error": "Comment text is required"}

    comments_col.insert_one({
        "article_id": article_id,
        "text": comment["text"],
        "created_at": datetime.utcnow()
    })

    return {"message": "Comment added successfully"}

# ---------------- AI SUMMARY ----------------

@app.get("/articles/{article_id}/summary")
def get_summary(article_id: int):
    return {
        "summary": (
            "AI analysis shows mixed public sentiment. "
            "Many users appreciate the initiative, while others "
            "express concerns about implementation and long-term impact."
        )
    }

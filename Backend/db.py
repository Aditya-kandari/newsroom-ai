from pymongo import MongoClient
from datetime import datetime

MONGO_URI = "mongodb://localhost:27017"

client = MongoClient(MONGO_URI)
db = client["newsroom_ai"]

articles_col = db["articles"]
comments_col = db["comments"]

SEED_VERSION = 3  # 🔼 increment this whenever you change seed data
meta_col = db["meta"]

def insert_sample_articles():
    meta = meta_col.find_one({"_id": "seed_version"})
    current_version = meta["version"] if meta else 0

    if current_version < SEED_VERSION:
        articles_col.delete_many({})

        articles_col.insert_many([
            {
                "id": 1,
                "title": "Elon Musk's Starlink entry in Pakistan delayed over data security concerns",
                "summary": "Pakistan delays Starlink approval citing data security and geopolitical concerns.",
                "content": [
                    "Pakistan's decision on granting a licence to Starlink to operate in its satellite internet market has been delayed amid data security concerns, geopolitical sensitivities and competition from Chinese firms, local media reported on Sunday.",

                    "Starlink, owned by tech billionaire Elon Musk, is among five companies seeking approval to provide satellite-based internet services in Pakistan. However, officials say unresolved security considerations and broader geopolitical factors have slowed the clearance process.",

                    "According to the Express Tribune, the government has raised concerns that Starlink's services could allow certain data transmissions to bypass Pakistan's monitoring, regulatory and safety checks. A senior government official said authorities cannot allow a license without ensuring consumer data safety.",

                    "Sources cited by the newspaper said authorities had tested scenarios in which Starlink was expected to pick up sensitive data while providing satellite-based internet services.",

                    "Officials added that the government is working to address these issues, which have delayed the approval process.",

                    "The report also cited the fallout between US President Donald Trump and Elon Musk as a factor being weighed by the Pakistani establishment.",

                    "At present, Pakistan maintains control over internet data traffic largely through Pakistan Telecommunication Company Limited, which holds a majority stake in the country's undersea cable infrastructure.",

                    "Satellite internet services are expected to focus primarily on remote and underserved regions, including Balochistan, where conventional broadband infrastructure remains limited.",

                    "The Pakistan Space Activities Regulatory Board confirmed that five companies, including Starlink and Chinese firms, have shown interest in entering the satellite internet market.",

                    "While consultations with stakeholders have been completed, the licensing framework has not yet been finalised."
                ]
            },
            {
                "id": 2,
                "title": "Economic Slowdown Raises Concerns",
                "summary": "Experts warn about economic indicators.",
                "content": [
                    "India’s economic growth has shown signs of slowing down amid global uncertainty.",
                    "Experts point to inflation, reduced consumption, and tightening monetary policy as key reasons.",
                    "Analysts suggest targeted fiscal measures may be required to revive momentum."
                ]
            }
        ])

        meta_col.update_one(
            {"_id": "seed_version"},
            {"$set": {"version": SEED_VERSION}},
            upsert=True
        )

def insert_sample_comments():
    meta = meta_col.find_one({"_id": "seed_version"})
    current_version = meta["version"] if meta else 0

    if current_version < SEED_VERSION:
        comments_col.delete_many({})

        comments_col.insert_many([
            # -------- Article 1 comments --------
            {
                "article_id": 1,
                "text": "This raises serious concerns about national data security.",
                "sentiment": "negative",
                "created_at": datetime.utcnow()
            },
            {
                "article_id": 1,
                "text": "Satellite internet is necessary for remote regions like Balochistan.",
                "sentiment": "positive",
                "created_at": datetime.utcnow()
            },
            {
                "article_id": 1,
                "text": "The government should clearly define regulations before approval.",
                "sentiment": "neutral",
                "created_at": datetime.utcnow()
            },

            # -------- Article 2 comments --------
            {
                "article_id": 2,
                "text": "Inflation is making economic recovery difficult.",
                "sentiment": "negative",
                "created_at": datetime.utcnow()
            },
            {
                "article_id": 2,
                "text": "Economic cycles like this are expected after global slowdowns.",
                "sentiment": "neutral",
                "created_at": datetime.utcnow()
            },
            {
                "article_id": 2,
                "text": "Government stimulus may help revive growth.",
                "sentiment": "positive",
                "created_at": datetime.utcnow()
            }
        ])

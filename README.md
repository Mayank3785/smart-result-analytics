# Smart Result Analytics Backend 🚀

A production-ready backend system for analyzing university result data and generating
branch-wise and overall Top-10 CGPA rankings.

## 🔧 Tech Stack
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pandas
- Render (Cloud Deployment)

## ✨ Features
- CSV result ingestion into PostgreSQL
- Branch-wise Top 10 CGPA analytics
- University-wide Top 10 CGPA ranking
- Clean REST APIs with Swagger UI
- Cloud deployment with environment variables

## 📊 API Endpoints
- `GET /analytics/branch-top10?branch=CSE`
- `GET /analytics/all-branches-top10`
- `GET /analytics/university-top10`
- `POST /results/upload`

## 🚀 Deployment
Hosted on Render (Free Tier)

## 🧠 What I Learned
- Backend architecture with FastAPI
- SQL-based analytics using PostgreSQL
- CSV data processing using Pandas
- Cloud deployment and environment management

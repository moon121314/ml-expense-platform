# ML Expense Platform

An end-to-end ML system that predicts expense categories from text descriptions.

## Live Demo
Coming soon (Render deployment)

## Tech Stack
- **FastAPI** — model serving API
- **scikit-learn** — TF-IDF + Logistic Regression
- **MLflow** — experiment tracking
- **Docker** — containerization
- **Kubernetes** — orchestration
- **Prometheus + Grafana** — monitoring
- **Evidently** — drift detection

## Features
- Text classification: "Starbucks latte" → food
- Model loaded once at startup (fast inference)
- Pydantic validation on input
- Prometheus metrics (prediction count, latency)
- Grafana dashboard
- Data drift detection with Evidently

## Project Structure

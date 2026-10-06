# ML Expense Platform

An ML pipeline that classifies expense descriptions into `food`, `transport`, `utilities`, or `shopping`.

## Task

Given an expense description such as `"Starbucks latte"`, predict its category using machine learning.

## Model

* **Vectorizer:** TF-IDF (unigrams + bigrams)
* **Classifier:** Logistic Regression
* **Pipeline:** `sklearn.pipeline.Pipeline`
* **Tracking:** MLflow

## Project Structure

```text
ml-expense-platform/
├── data/
│   └── expenses.csv
├── ml/
│   ├── training/
│   │   └── train.py
│   └── predict.py
├── mlruns/
├── mlflow.db
├── requirements.txt
└── README.md
```

## Setup

```bash
git clone <repository-url>
cd ml-expense-platform
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Train Model

```bash
python ml/training/train.py
```

The training pipeline logs parameters, metrics, and the trained model to MLflow.

## View Experiments

```bash
mlflow server --host 127.0.0.1 --port 5000 --allowed-hosts "*"
```

Open:

```text
http://127.0.0.1:5000
```

## Example

```text
Input:  Starbucks latte
Output: food

Input:  Uber ride
Output: transport
```

## Results

| Metric   |      Value |
| -------- | ---------: |
| Accuracy | See MLflow |
| F1 Score | See MLflow |

## Tech Stack

* Python
* Pandas
* Scikit-learn
* TF-IDF
* Logistic Regression
* MLflow
* SQLite

## What It Demonstrates

* Text classification
* ML pipeline development
* Model evaluation
* Experiment tracking with MLflow
* Model prediction
* Foundation for production MLOps

## Future

FastAPI → Docker → Kubernetes → Monitoring → Model/Data Drift → CI/CD

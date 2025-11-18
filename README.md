# data_science_evng

This repository contains code, notebooks, and course notes for a hands-on data science curriculum. It is intended as a companion for learning core data-science concepts and for organizing reproducible example projects.

## High-level curriculum
- Python & data-science tooling (venv, pip, Jupyter)
- Exploratory Data Analysis (Pandas, NumPy)
- Statistics & probability fundamentals
- Data cleaning & feature engineering
- Data visualization (Matplotlib, Seaborn, Plotly)
- Supervised learning (regression, classification)
- Unsupervised learning (clustering, dimensionality reduction)
- Model evaluation, validation and selection
- Introduction to deep learning (PyTorch/TensorFlow basics)
- Model deployment & reproducibility (Docker, ML pipelines)

## Repository layout
- notebooks/ — interactive Jupyter notebooks for lectures and experiments
- src/ — reusable modules and scripts
- data/ — dataset placeholders (do not commit large raw data)
- notes/ — concise text notes and summaries
- models/ — saved model artifacts
- requirements.txt — Python dependencies

## How to use this repo
1. Clone: git clone <repo-url>
2. Create environment:
    - python -m venv .venv && source .venv/bin/activate
    - pip install -r requirements.txt
3. Open notebooks with Jupyter Lab/Notebook: jupyter lab
4. Place raw datasets in data/raw/ (add small sample data for demos if needed)
5. Run reusable code from src/ or execute example scripts in notebooks/
6. Follow notebook cells sequentially; use notes/ for quick reference
7. Tests/examples: run any scripts in src/tests/ or CI if provided

## Contributing & notes
- Keep notebooks runnable and small; move reusable code to src/
- Document dataset sources and preprocessing steps
- Use git for versioning; avoid committing large datasets or secrets

## Connect
- Follow me on LinkedIn: https://www.linkedin.com/in/rahul-tiwari-120897/



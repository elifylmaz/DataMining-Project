# Sentiment Analysis on Movie Reviews

## Project Overview
This project focuses on sentiment analysis of movie reviews for the film **"Parasite" (2019)**, using data collected from the Letterboxd website. Two approaches are implemented:
1. **Supervised Learning**: Utilizing labeled datasets for training models.
2. **Zero-Shot Learning**: Employing pre-trained models without labeled data for flexible analysis.

## Objectives
- To classify movie reviews as **positive**, **neutral**, or **negative**.
- To compare the performance of supervised learning and zero-shot learning methods.

---

## Features
- **Data Collection**: Automated scraping of reviews using Selenium.
- **Data Preprocessing**: Includes cleaning, tokenization, stop-word removal, lemmatization, and vectorization (TF-IDF).
- **Data Labeling**: Manual and automated sentiment labeling with SMOTE for class balancing.
- **Machine Learning Models**:
  - Support Vector Machine (SVM)
  - Logistic Regression
- **Zero-Shot Learning**: Leveraging Hugging Face’s `nlptown/bert-base-multilingual-uncased-sentiment` model for classification.
- **Performance Evaluation**: Comparing models using accuracy, F1-score, and confusion matrices.

---

## Technologies Used
- **Programming Language**: Python
- **Libraries**:
  - `Selenium`: Web scraping
  - `NLTK`: Natural Language Processing
  - `Scikit-learn`: Machine learning and data preprocessing
  - `Hugging Face Transformers`: Zero-shot sentiment analysis
  - `SMOTE`: Data balancing for imbalanced datasets
  - `Matplotlib` & `Seaborn`: Data visualization
- **Other Tools**:
  - `Pandas`: Data manipulation
  - `Torch`: GPU support for zero-shot models

---

### Results
- Accuracy and F1-scores are displayed in the terminal.
- Confusion matrices and classification reports are saved as visualizations.

---

## Results & Analysis
- **Supervised Learning**:
  - **SVM**:
    - Accuracy: 92.85%
    - F1-Score: 0.9268
  - **Logistic Regression**:
    - Accuracy: 93.72%
    - F1-Score: 0.9360
- **Zero-Shot Learning**:
  - Accuracy: 62.34%
  - F1-Score: 0.4910

**Conclusion**: While supervised learning methods perform significantly better in accuracy and F1-score, zero-shot learning provides a flexible solution for projects with limited labeled data.

---

## Spam SMS Classifier
A machine learning mini-project that classifies SMS messages as Spam or Ham (Not Spam). It uses the SMS Spam Collection Dataset and applies CountVectorizer to convert text into numerical features, followed by a Logistic Regression model to accurately detect unwanted spam messages.

This folder contains a Jupyter notebook, `spam_sms_classifier.ipynb`, that walks through building a supervised learning model to detect spam sms-s.

- **Dataset**: `spam.csv`, a labeled collection of sms messages tagged as spam or not spam.
- **Objective**: Explore the dataset, engineer features from sms text, and train a classifier that distinguishes spam from legitimate sms-s.

### Running the Notebook

1. Launch Jupyter Lab or Jupyter Notebook in the repository root:
   ```
   jupyter lab
   ```
   or
   ```
   jupyter notebook
   ```
2. Open `supervised_learning/spam_sms_classifier.ipynb`.
3. Run the cells sequentially. The notebook includes data loading, preprocessing, model training, and evaluation steps.

### Requirements

- Python environment with typical data science libraries (`pandas`, `scikit-learn`).
- Jupyter environment (Notebook or Lab).



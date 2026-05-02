# Financial Fraud Detection System

**Live App:** [https://fraud-detection-m.streamlit.app/](https://fraud-detection-m.streamlit.app/)

A real-time fraud detection web application built with **Streamlit** and **Scikit-Learn**. This system uses machine learning to analyze financial transactions and identify potential fraudulent activity based on patterns such as account draining and transaction types.

## 🚀 Features
- **Real-time Prediction**: Input transaction details manually to get an instant fraud assessment.
- **Machine Learning Powered**: Uses a Random Forest model trained on the PaySim financial dataset.
- **Clean UI**: Simple and intuitive interface built with Streamlit.
- **Model Pipeline**: Includes automated preprocessing for categorical and numerical features.

## 🛠️ Tech Stack
- **Frontend**: Streamlit
- **Machine Learning**: Scikit-Learn, Pandas, NumPy
- **Deployment**: Prepared for Streamlit Cloud / GitHub

## 📂 Project Structure
- `fraud_detection.py`: The main Streamlit application script.
- `frauddetection.ipynb`: Jupyter Notebook containing Exploratory Data Analysis (EDA) and model training.
- `fraud_detection_pipeline.pkl`: Serialized machine learning model and preprocessing pipeline.
- `requirements.txt`: List of Python dependencies required for the project.
- `.gitignore`: Configured to exclude large datasets and virtual environments.

## ⚙️ Installation & Local Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/saisushanthmoturi/frauddetection.git
   cd frauddetection
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   streamlit run fraud_detection.py
   ```

## 📊 How to Test for Fraud
To see the model in action, try the following "Fraud" patterns:
- **Type**: `TRANSFER`
- **Amount**: Same as the `Old Balance (Sender)` (e.g., 500,000)
- **New Balance (Sender)**: `0`
- **Receiver Balances**: `0`

## 📝 Dataset
The model is trained on the **PaySim** dataset, which simulates mobile money transactions based on a sample of real financial logs. It focuses on detecting `TRANSFER` and `CASH_OUT` fraud.

---
Developed by [Sai Sushanth Moturi](https://github.com/saisushanthmoturi)

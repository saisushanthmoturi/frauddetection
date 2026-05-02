import streamlit as st
import pandas as pd
import joblib
import os

# Load the model
model = joblib.load("fraud_detection_pipeline.pkl")

st.title("Fraud Detection")
st.markdown("Please enter the transaction details and click the button to predict fraud.")
st.divider()

# Input fields
transaction_type = st.selectbox("Transaction Type", ["CASH_IN", "CASH_OUT", "DEBIT", "TRANSFER", "PAYMENT"])
amount = st.number_input("Amount", min_value=0.0, step=0.01)
oldbalanceOrg = st.number_input("Old Balance (Sender)", min_value=0.0, step=0.01)
newbalanceOrig = st.number_input("New Balance (Sender)", min_value=0.0, step=0.01)
oldbalanceDest = st.number_input("Old Balance (Receiver)", min_value=0.0, step=0.01)
newbalanceDest = st.number_input("New Balance (Receiver)", min_value=0.0, step=0.01)

if st.button("Predict"):
    # Create input DataFrame
    input_data = pd.DataFrame([{
        "type" : transaction_type,
        "amount" : amount,
        "oldbalanceOrg": oldbalanceOrg,
        "newbalanceOrig": newbalanceOrig,
        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest": newbalanceDest
    }])

    # Perform prediction
    prediction = model.predict(input_data)[0]

    # Display prediction result
    st.subheader(f"Prediction : '{int(prediction)}'")

    if prediction == 1:
        st.error("This transaction can be fraud")
    else:
        st.success("This transaction looks like it is not a fraud")

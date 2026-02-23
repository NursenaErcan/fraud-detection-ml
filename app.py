import streamlit as st
import joblib
import pandas as pd

# Load the trained model
model = joblib.load('model/fraud_detection_model.pkl')
st.title("Credit Card Fraud Detection")
st.markdown("Enter the details of the transaction to predict if it's fraudulent or not.")

st.divider()

trandaction_amount = st.selectbox("Transaction Type", ["PAYMENT", "TRANSFER", "CASH_OUT", "DEBIT", "CASH_IN"])
amount = st.number_input("Transaction Amount", min_value=0.0, value=1000.0,)
oldbalanceOrg = st.number_input("Old Balance Sender", min_value=0.0, value=10000.0)
newbalanceOrig = st.number_input("New Balance sender", min_value=0.0, value=9000.0)

oldbalanceDest = st.number_input("Old Balance Receiver", min_value=0.0)
newbalanceDest = st.number_input("New Balance Receiver", min_value=0.0)


if st.button("Predict"):
    input_data = pd.DataFrame({
        'type': [trandaction_amount],
        'amount': [amount],
        'oldbalanceOrg': [oldbalanceOrg],
        'newbalanceOrig': [newbalanceOrig],
        'oldbalanceDest': [oldbalanceDest],
        'newbalanceDest': [newbalanceDest]
    })
    
    prediction = model.predict(input_data)[0]

    st.subheader(f"Prediction Result: {int(prediction)}")
    
    if int(prediction) == 1:
        st.error("The transaction is predicted to be FRAUDULENT.")
    else:
        st.success("The transaction is predicted to be LEGITIMATE.")
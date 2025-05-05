import streamlit as st
import joblib
import numpy as np

# Load model and scaler
model = joblib.load('gb_model.pkl')
scaler = joblib.load('scaler.pkl')
columns = joblib.load('feature_columns.pkl')

st.title("🏡 House Price Prediction App")
st.markdown("Enter the house features below:")

# User Inputs
area = st.number_input('Area (sq ft)', min_value=100)
bedrooms = st.selectbox('Bedrooms', [1, 2, 3, 4, 5])
bathrooms = st.selectbox('Bathrooms', [1, 2, 3, 4])
stories = st.selectbox('Stories', [1, 2, 3, 4])
mainroad = st.selectbox('Main Road', ['yes', 'no'])
guestroom = st.selectbox('Guest Room', ['yes', 'no'])
basement = st.selectbox('Basement', ['yes', 'no'])
hotwaterheating = st.selectbox('Hot Water Heating', ['yes', 'no'])
airconditioning = st.selectbox('Air Conditioning', ['yes', 'no'])
parking = st.selectbox('Parking Spaces', [0, 1, 2, 3])
prefarea = st.selectbox('Preferred Area', ['yes', 'no'])
furnishingstatus = st.selectbox('Furnishing Status', ['furnished', 'semi-furnished', 'unfurnished'])

# Manual Encoding
input_dict = {
    'area': area,
    'bedrooms': bedrooms,
    'bathrooms': bathrooms,
    'stories': stories,
    'mainroad': 1 if mainroad == 'yes' else 0,
    'guestroom': 1 if guestroom == 'yes' else 0,
    'basement': 1 if basement == 'yes' else 0,
    'hotwaterheating': 1 if hotwaterheating == 'yes' else 0,
    'airconditioning': 1 if airconditioning == 'yes' else 0,
    'parking': parking,
    'prefarea': 1 if prefarea == 'yes' else 0,
    'furnishingstatus_semi-furnished': 1 if furnishingstatus == 'semi-furnished' else 0,
    'furnishingstatus_unfurnished': 1 if furnishingstatus == 'unfurnished' else 0
}

# Align input with feature columns
input_data = np.array([input_dict.get(col, 0) for col in columns]).reshape(1, -1)
input_scaled = scaler.transform(input_data)

# Predict
if st.button("Predict Price"):
    prediction = model.predict(input_scaled)[0]
    st.success(f"🏠 Estimated House Price: RS: {int(prediction):,} Rupees")
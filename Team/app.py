import streamlit as st
import pickle
import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt
from io import StringIO

# Load the pre-trained model
with open('best_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Set custom CSS for design improvements
st.markdown("""
    <style>
        /* Gradient Background with smooth animation */
        body {
            background: linear-gradient(135deg, #6a11cb, #2575fc, #56ccf2);
            background-size: 400% 400%;
            animation: gradientBG 10s ease infinite;
            color: #ffffff;
            font-family: 'Arial', sans-serif;
        }

        /* Gradient animation */
        @keyframes gradientBG {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        /* Button styling */
        .stButton>button {
            background-color: #3b9c9c;
            color: white;
            font-size: 20px;
            padding: 15px 35px;
            border-radius: 25px;
            font-weight: bold;
            transition: transform 0.3s ease;
        }
        .stButton>button:hover {
            background-color: #2f7878;
            transform: scale(1.1);
        }

        /* Input Field Styling */
        .stNumberInput>div, .stSelectbox>div, .stSlider>div {
            background-color: rgba(255, 255, 255, 0.1);
            border-radius: 10px;
            padding: 8px;
            color: #56ccf2;
        }

        /* Title and Header styling */
        .stTitle, .stHeader {
            color: #56ccf2;
            font-size: 32px;
            font-weight: bold;
        }

        /* Adjusting header section */
        .stMarkdown {
            text-align: center;
        }

        /* Custom Scrollbar */
        ::-webkit-scrollbar {
            width: 10px;
        }
        ::-webkit-scrollbar-thumb {
            background-color: #3b9c9c;
            border-radius: 10px;
        }

    </style>
""", unsafe_allow_html=True)

# Sidebar for input features
st.sidebar.title("🌟 Customer Churn Prediction 🌟")
st.sidebar.write("Please provide the customer information below to predict the likelihood of churn:")

# Interactive input fields
account_length = st.sidebar.slider("Account Length (months)", min_value=1, max_value=500, value=100, help="Account length in months.")
voice_mail_plan = st.sidebar.selectbox("Voice Mail Plan", options=[0, 1], help="0: No plan, 1: Plan")
voice_mail_messages = st.sidebar.slider("Voice Mail Messages", min_value=0, max_value=100, value=5, help="Number of voice mail messages.")
day_mins = st.sidebar.slider("Day Minutes", min_value=0.0, max_value=500.0, value=100.0, help="Minutes spent on calls during the day.")
evening_mins = st.sidebar.slider("Evening Minutes", min_value=0.0, max_value=500.0, value=50.0, help="Minutes spent on calls during the evening.")
night_mins = st.sidebar.slider("Night Minutes", min_value=0.0, max_value=500.0, value=20.0, help="Minutes spent on calls at night.")
international_mins = st.sidebar.slider("International Minutes", min_value=0.0, max_value=100.0, value=5.0, help="Minutes spent on international calls.")
customer_service_calls = st.sidebar.slider("Customer Service Calls", min_value=0, max_value=10, value=2, help="Number of customer service calls.")
international_plan = st.sidebar.selectbox("International Plan", options=[0, 1], help="0: No plan, 1: Plan")
day_calls = st.sidebar.slider("Day Calls", min_value=0, max_value=200, value=50, help="Number of calls made during the day.")
day_charge = st.sidebar.slider("Day Charge", min_value=0.0, max_value=100.0, value=25.0, help="Charge for the day calls.")
evening_calls = st.sidebar.slider("Evening Calls", min_value=0, max_value=200, value=30, help="Number of evening calls.")
evening_charge = st.sidebar.slider("Evening Charge", min_value=0.0, max_value=100.0, value=15.0, help="Charge for evening calls.")
night_calls = st.sidebar.slider("Night Calls", min_value=0, max_value=200, value=10, help="Number of night calls.")
night_charge = st.sidebar.slider("Night Charge", min_value=0.0, max_value=50.0, value=5.0, help="Charge for night calls.")
international_calls = st.sidebar.slider("International Calls", min_value=0, max_value=20, value=3, help="Number of international calls.")
international_charge = st.sidebar.slider("International Charge", min_value=0.0, max_value=50.0, value=5.0, help="Charge for international calls.")
total_charge = st.sidebar.slider("Total Charge", min_value=0.0, max_value=500.0, value=100.0, help="Total accumulated charge.")

# Prepare the input data for prediction
user_input = np.array([account_length, voice_mail_plan, voice_mail_messages, day_mins, evening_mins, night_mins,
                       international_mins, customer_service_calls, international_plan, day_calls, day_charge, 
                       evening_calls, evening_charge, night_calls, night_charge, international_calls, international_charge, 
                       total_charge]).reshape(1, -1)

# Prediction button with engaging animation
predict_button = st.sidebar.button("🔮 Predict Churn 🔮")

if predict_button:
    # Show loading spinner during prediction
    with st.spinner('🔄 Making prediction...'):
        time.sleep(2)  # Simulate prediction delay
        prediction = model.predict(user_input)

    # Display result with fun animations and effects
    if prediction == 1:
        st.sidebar.success("🚨 **The customer is likely to churn!** 🚨")
        st.balloons()  # Fun balloons effect on churn prediction
    else:
        st.sidebar.success("🎉 **The customer is unlikely to churn!** 🎉")
        st.snow()  # Fun snow effect on no churn prediction

    # Motivation message after prediction
    st.sidebar.markdown("""
        <h3 style='color: #56ccf2;'>Keep going, you're making great predictions!</h3>
        <p style='color: #56ccf2;'>Whether the customer churns or not, your predictions help businesses improve their services and retain customers. Great job!</p>
    """, unsafe_allow_html=True)

    # Visualization: Create a colorful bar chart to represent input data
    input_data_df = pd.DataFrame({
        'Feature': [
            'Account Length', 'Voice Mail Plan', 'Voice Mail Messages', 'Day Minutes', 'Evening Minutes', 'Night Minutes', 
            'International Minutes', 'Customer Service Calls', 'International Plan', 'Day Calls', 'Day Charge', 
            'Evening Calls', 'Evening Charge', 'Night Calls', 'Night Charge', 'International Calls', 'International Charge', 
            'Total Charge'
        ],
        'Value': [
            account_length, voice_mail_plan, voice_mail_messages, day_mins, evening_mins, night_mins, international_mins, 
            customer_service_calls, international_plan, day_calls, day_charge, evening_calls, evening_charge, night_calls, 
            night_charge, international_calls, international_charge, total_charge
        ]
    })

    st.sidebar.subheader("Customer Data Visualization")
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.barh(input_data_df['Feature'], input_data_df['Value'], color=plt.cm.viridis(np.linspace(0, 1, len(input_data_df))))
    ax.set_xlabel('Values')
    ax.set_title('Customer Input Data')

    # Add labels for each bar
    for bar in bars:
        width = bar.get_width()
        ax.text(width + 3, bar.get_y() + bar.get_height()/2, f'{width:.1f}', va='center', color='white', fontweight='bold')

    st.pyplot(fig)

    # Prepare data for CSV download
    prediction_result = 'Churn Prediction: ' + ('Likely to Churn' if prediction == 1 else 'Unlikely to Churn')
    input_data_df['Prediction'] = prediction_result

    # Convert dataframe to CSV
    csv = input_data_df.to_csv(index=False)
    st.sidebar.download_button(
        label="Download Prediction and Data as CSV",
        data=csv,
        file_name="customer_data_with_prediction.csv",
        mime="text/csv"
    )

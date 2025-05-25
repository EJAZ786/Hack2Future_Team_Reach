import pandas as pd
import streamlit as st
import google.generativeai as genai

# Load dummy CSV data
data =  pd.read_csv(r"D:\Health_Hackathon\dummy_health_data_bot.csv")

# Configure Gemini API
API_KEY = "AIzaSyCg5fuZpt16k0wyQabRyqgVVm3CxFsyZmA"  # Replace with your actual Gemini API key
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")  # Replace with your desired model

def generate_response(user_query):
    try:
        # Convert entire dataframe to string without indices
        health_data_text = data.to_string(index=False)

        # Build prompt combining data and user query
        prompt = f"""
        You are a medical assistant chatbot. Your task is to interact with the user 
        to understand their symptoms or disease and provide recommendations. 
        You must rely only on the data provided below and not generate anything that 
        is not available in the dataset.
        Health Data:\n{health_data_text}
        You must:
        - Try to identify the disease based on the symptoms from the data provided.
        - Recommend medications and a doctor if available in the dataset.
        - If the disease or symptoms are not in the data, respond with:
        I have no data regarding this disease, please consult a nearby doctor.
        
        user query = {user_input}"""

        # Generate content using Gemini API
        response = model.generate_content(prompt)

        # Extract the generated answer text
        answer = response.text.strip()

        return answer
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Streamlit UI
st.title("Target Reach-AI Based Health Chatbot")
st.markdown("""
💬 *Hi! I'm your helpful health assistant.*  
I'm here to guide you through today’s patient data and answer any questions you might have.  
Whether you're looking for patterns, prescriptions, or just curious about common symptoms — I'm ready when you are. Just type your question below. 🩺📊
""")


user_input = st.text_input("Enter your question:")

if user_input:
    reply = generate_response(user_input)
    st.write("Chatbot response:")
    st.write(reply)
🧠 Target Reach – AI-Based Health Chatbot
An intelligent, interactive healthcare assistant built to help users receive guidance based on their health symptoms using structured medical data. Developed as part of a healthcare hackathon, this AI-powered chatbot mimics a digital health consultant by understanding symptoms and suggesting medications—only from verified, structured datasets.

🧑‍💻 System Requirements
Operating System: Windows, macOS, or Linux
Python: Version 3.8 to 3.11
Internet Connection: Required to connect to Gemini API

**Steps to follow:**
1. clone the git repository
2. Create your own virtual environment and install required packages from requirements.txt
3. py -3.11 -m venv venv
4. .\venv\Scripts\activate
5. pip install streamlit pandas requests google.generativeai
6. run "streamlit run health.py" inside terminal (it will rediret to the streamlit interface where we can ask the required medication details to the Bot)
7.Create your own gemini API Key and replace it with the exisisting one in the code Line 9 if it is showing error related to API Key when you are running "streamlit run health.py"

🎯 Objective
The goal of this project is to build a conversational health assistant that:

Accepts user-reported symptoms

Interacts conversationally to understand the user's condition better

Matches symptoms to a disease using real-world medical data

Suggests medications and a doctor, if available in the dataset

Advises seeing a physician if symptoms are unrecognized

This solution is designed to help patients at home with limited access to medical professionals, by giving them basic medical suggestions based on pre-verified data.

🛠 Features
✅ Conversational interface powered by Google Gemini AI

✅ Reads and interprets a structured medical dataset (.csv) with:

Disease names

Symptoms

Medications (tablets, syrups, etc.)

Doctor names and designations

✅ Suggests possible treatments for known diseases

✅ Politely advises visiting a doctor if the condition is not in dataset

✅ Built with Streamlit for a clean and accessible user interface

🧰 Tech Stack
Tech	Purpose
Streamlit	Frontend UI for chatbot interaction
Gemini (Google AI)	Language model for understanding and response
Pandas	Data handling from CSV file
Azure App Service (optional)	Hosting and deployment

📂 How It Works
User Input: The user types in their symptoms (e.g., "I have a mild fever and dry cough").

Chatbot Analysis:

The app searches the CSV data for relevant disease & symptom matches.

It then identifies if there's a matching condition and provides:

Medications (if listed)

Doctor name and designation (if listed)

Fallback: If symptoms or diseases are not in the dataset, the bot will respond:

"I have no data regarding this disease, please consult a nearby doctor."

🧪 Sample Use Cases
Input:

vbnet
Copy
Edit
I'm having high fever and sore throat.
Bot Response:

csharp
Copy
Edit
Based on your symptoms, the probable disease is Flu.
Suggested Medications:
- Dolo 650 (for fever)
- Cofsils syrup (for sore throat)
Please consult Dr. Shalini Verma, General Physician, if symptoms persist.
🚀 How to Run Locally
Clone the repository:

bash
Copy
Edit
git clone https://github.com/Tarakananda/Health_Hackathon.git
cd Health_Hackathon
Create and activate a virtual environment:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the app:

bash
Copy
Edit
streamlit run app.py
🌐 Live Demo (if deployed)
You can also deploy this using Azure App Service or Streamlit Community Cloud for easy access via web browser.

🙌 Team & Credits
Built with passion and purpose by a team of developers for the [Health Hackathon 2025].

Special thanks to:

Google Gemini API for language understanding

Streamlit for making data apps fast and beautiful

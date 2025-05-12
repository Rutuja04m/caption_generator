# caption_generator
a Python application that takes an image as input and generates a descriptive caption using Google's Gemini API.
This project demonstrates how to integrate and use **Google's Gemini 2.0 Flash** model via the Vertex AI API. It showcases capabilities like fast text generation, prompt completion, and multi-modal (text + image) support.

---

##  Features

- ✅ Gemini 2.0 Flash API integration
- ✅ Fast and cost-effective responses
- ✅ Scalable and modular code
- ✅ Supports both **text** and **image** prompts
- ✅ Simple and clean UI (if frontend used)

---

##  Tech Stack

- Language: **Python / Node.js / JavaScript** (update accordingly)
- API: **Google Vertex AI**
- Model: `gemini-2.0-flash`
- Environment: CLI / Web App / Streamlit / React (based on your usage)

---

##  Setup Instructions

 1. Clone the Repo
  
 2. Create & Activate Virtual Environment (Python only)
 (in terminal)
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
3.Install Dependencies
    pip install -r requirements.txt

4.Set Up Environment Variables
Create a .env file in the root folder and add your API key:
(in terminal)

GOOGLE_API_KEY=your_actual_api_key_here

(my API KEY= AIzaSyBxcj7TRG1GW1N0tbvdnw4XItgIEjUgwfk  or you can create and use yu own API Key)

5. Run the Application
   python main.py  # or npm run dev

## Folder Sturcture

gemini-flash-project/
 ┣ main.py / app.js
 ┣ requirements.txt / package.json
 ┣ README.md
 ┣ utils/
 ┣ templates/ or frontend/
 ┗ assets/


Working Screenshots((1), (2), (3)) are uploaded with other files.

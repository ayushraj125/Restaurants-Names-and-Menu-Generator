# Restaurants-Names-and-Menu-Generator


A simple and fun LLM-powered web application that generates **fancy restaurant names** based on selected cuisines using **LangChain**, **Streamlit**, and **DeepInfra API**.

---

## 🚀 Features

- Choose from 5 cuisines: Indian, Italian, Mexican, Arabic, American.
- Get a unique restaurant name powered by DeepInfra-hosted LLM.
- Modular, beginner-friendly code using LangChain's `LLMChain` and `PromptTemplate`.

---

## 🧠 Tech Stack

- [Streamlit](https://streamlit.io/)
- [LangChain](https://www.langchain.com/)
- [DeepInfra](https://deepinfra.com/) (as an LLM API backend)
- Python

---

## 🛠 Setup Instructions

### 1. Clone the repository

git clone https://github.com/yourusername/restaurant-name-generator
cd restaurant-name-generator

### 2. Install dependencies
pip install streamlit langchain openai

### 3. Add your API key
Create a file named secret_key.py in the root folder and add:
deepinfrapi_key = "your_deepinfra_api_key_here"

### 4. Run the app
streamlit run main.py

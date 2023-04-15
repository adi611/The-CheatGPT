import os
import requests
import streamlit as st

from dotenv import load_dotenv
load_dotenv()

url = "https://openai80.p.rapidapi.com/completions"

headers = {
    "content-type": "application/json",
    "X-RapidAPI-Key": os.getenv("GPT_KEY"),
    "X-RapidAPI-Host": "openai80.p.rapidapi.com"
}

@st.cache_data
def generate_answer(prompt):
    payload = {
        "model": "text-davinci-003",
        "prompt": prompt,
        "max_tokens": 256,
        "temperature": 0,
        "top_p": 1,
        "n": 1,
        "stream": False,
        "logprobs": None,
        "stop": "['END']"
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    resp = response.json()
    print("\n\n", resp, "\n\n")
    respo = resp['choices']
    respon = respo[0]
    return (respon['text']).strip()

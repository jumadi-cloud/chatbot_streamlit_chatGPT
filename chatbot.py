# import library 

import streamlit as st
import openai
from streamlit_chat import message

st.set_page_config(
    page_title="Chatbot - Demo",
    page_icon="👋"
)

# Cara memangil API dan Konfigurasi
openai.api_key = st.secrets["model"]

def generate_response(prompt):
	completions = openai.Completion.create(
		engine = "text-davinci-003", # Untuk menggunakan model 
		prompt = prompt,             # Untuk menghasilkan teks 
		max_tokens = 1024,           # Jumlah maksimum token (kata dan tanda baca)
		n = 1,                       # Jumlah tanggapan
		stop = None,                 # Untuk berhenti menghasilkan teks
		temperature = 0.5,           # Untuk mengontrol teks yang dihasilkan
	)
	message = completions.choices[0].text
	return message


# View ( "Tampilan Chatbot")
st.title("🤖 Chatbot Menggunakan Model ChatGPT👋")

# Menyimpan obrolan chatbot
if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

# Input Penguna 
def get_text():
    input_text = st.text_input("Saya: ","Hello, apa kabar kamu?", key="input")
    return input_text 

# Respone Chatbot
user_input = get_text()
   
if user_input:
    output = generate_response(user_input)
    # Menyimpan output
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

# Untuk menampilkan riwayat obrolan
if st.session_state['generated']:

    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
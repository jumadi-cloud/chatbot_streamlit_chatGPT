# import library

import streamlit as st
import openai
from streamlit_chat import message
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="Mahira - Demo",
    page_icon="🤖"
)

# Navigasi
selected = option_menu(None, ["Mahira", "About"], 
        icons=['house', "list-task"], 
        menu_icon="cast", default_index=0, orientation="horizontal",)

# Awal Content Chatbot 

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
if selected == "Mahira":
 st.markdown("""# 🤖 Mahira
### Tanya Mahira

Hai, aku Mahira👋

Kamu bisa panggil aku Sayang :see_no_evil:

Aku adalah asisten virtual **[Kelas Awan Pintar](https://www.youtube.com/@kelasawanpintar)** yang dibuat menggunakan **Model ChatGPT** yang dilatih oleh **[OpenAI](https://openai.com/blog/chatgpt/)**
Mahira bisa memberikanmu informasi apapun yang saat ini kamu butuhkan dan bisa jadi temen curhat :dancer:
Kamu bisa tau proses pembuatan mahira dan teknologi yang digunakan di **ABOUT**, Pepatah bilang Tak Kenal Maka Ta Sayang :dancer:

Dukung **Channel Youtube [Kelas Awan Pintar](https://www.youtube.com/@kelasawanpintar) dengan cara Subscribe, Like, Share and Comment**

Website kami: https://kelasawanpintar.netlify.app/

""", True)

# Menyimpan obrolan chatbot
 if 'generated' not in st.session_state:
    st.session_state['generated'] = []

 if 'past' not in st.session_state:
    st.session_state['past'] = []

# Input Penguna 
 def get_text():
    input_text = st.text_input("Pertanyaan Saya: ","Hello, apa kabar kamu?", key="input")
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
# Akhir Content Chatbot
# Awal Content About
if selected == "About":
    st.markdown("""# 🤖 Mahira
### Hallo Sahabat Mahira 👋

🤖 Aku Mahira👋

Aku adalah asisten virtual **[Kelas Awan Pintar](https://www.youtube.com/@kelasawanpintar)** yang dibuat menggunakan **Model ChatGPT** yang dilatih oleh **[OpenAI](https://openai.com/blog/chatgpt/)**.
 Mahira bisa memberikanmu informasi apapun yang saat ini kamu butuhkan dan bisa jadi temen curhat :dancer: :dancer:
""", True)
    st.write("---")
    st.markdown("""
    ### Teknologi Yang Ada di Mahira 🤖
    Seperti yang telah disebutkan, **Mahira** merupakan chatbot yang dapat berkomunikasi dalam format percakapan dan dirancang untuk bisa berinteraksi selayaknya interaksi antar manusia🤗.       
    Pondasi dibalik teknologi chatbot sendiri adalah teknologi Artificial Intelligence (AI), 
    cabang ilmu komputer yang berkaitan dengan pemecahan masalah-masalah selayaknya manusia seperti berbicara, 
    memahami, ataupun berpikir🥳.

    Salah satu bidang dalam AI yang membuat chatbot dapat memproses bahasa alami manusia adalah Natural Language Processing (NLP). **Model ChatGPT** ini dapat digunakan tujuan yang beragam, seperti membuat obrolan otomatis di aplikasi percakapan, 
    membantu dalam pembuatan konten, atau bahkan membantu dalam penerjemahan berbagai bahasa dengan tingkat akurasi yang berbeda-beda untuk tiap bahasa.
    **Model ChatGPT** dilatih dengan menggunakan milyaran kalimat dari berbagai sumber, sehingga model ini dapat menangkap berbagai gaya bahasa dan konteks percakapan. 
    Selain itu, **Model ChatGPT** juga dapat dioptimalkan melalui **fine-tunning** dengan cara menambahkan data latih yang spesifik untuk tugas tertentu, sehingga hasilnya lebih akurat.

    **Model ChatGPT** ini masih memiliki batasan-batasan. **Model ChatGPT** tidak selalu dapat memberikan jawaban yang benar untuk pertanyaan yang bersifat subjektif, atau yang memerlukan pengetahuan yang spesifik dan up-to-date. 
    **Model ChatGPT** juga belum mampu memberikan informasi atau memahami konteks dari peristiwa setelah tahun 2021. 
    Selain itu, **Model ChatGPT** juga membutuhkan data latih yang cukup banyak untuk dapat berfungsi dengan baik.[Sumber](https://id.wikipedia.org/wiki/ChatGPT)
    
    """, True)
    st.write("---")

    st.markdown("""
    ### 📑Proses Pembuatan Mahira
    Dalam proses pembuatan Mahira, Tentu Mahira tidak akan jelaskan disini hanya saja Mahira sudah siapkan Playlistnya🥳.                                                                                            
    Supaya sahabat Mahira juga bisa Godain Mahira💃 dan Sahabat Mahira lebih santai untuk mengikuti step by stepnya☕️.                                                                                                                               
    
    Apabila sahabat Mahira berhasil dengan mengikuti step by step, boleh @Mention kami di sosial Media LinkedIn [`Jumadi`](https://www.linkedin.com/in/jumadi-01/) Instagram [`Jumadi`](https://www.instagram.com/jumadijumadi470/) atau `Comment` di video tutorial 
    
    
    """, True)

    st.write("---")
    st.header("📺 Playlist Belajar Membuat Aplikasi Web Dengan Streamlit [Python]")
    
    col1, col2, col3 = st.columns(3)
    with col1:
            st.subheader("01a - Cara Membuat Chatbot Menggunakan Model ChatGPT Dengan Streamlit")
            st.video('https://www.youtube.com/watch?v=MaheNAPbBGU&list=PLm94WimySTnp8oZhsk_9iB_m92_ssgBbS&index=1&t=4s')

    with col2:
            st.subheader("01b - Cara Membuat Chatbot Menggunakan Model ChatGPT Dengan Streamlit")
            st.video('https://www.youtube.com/watch?v=DxWPH34MAx8&list=PLm94WimySTnp8oZhsk_9iB_m92_ssgBbS&index=2')

    with col3:
            st.subheader("01c - Deploy Chatbot Menggunakan Model ChatGPT Dengan Streamlit")
            st.video('https://www.youtube.com/watch?v=dIx4ccvKduU&list=PLm94WimySTnr_AllzUeBTZR-fdvTsw99l&index=3')

    st.write("---")
    st.header("Playlist Belajar Streamlit Bahasa Indonesia [Dasar]")
    col1, col2, col3 = st.columns(3)

    with col1:
            st.subheader("Introduction di Aplikasi Streamlit")
            st.video('https://www.youtube.com/watch?v=0PBpAEGuNHM&list=PLm94WimySTnr_AllzUeBTZR-fdvTsw99l')

    with col2:
            st.subheader("Cara menampilkan teks")
            st.video('https://www.youtube.com/watch?v=tPA0x_wToXQ&list=PLm94WimySTnr_AllzUeBTZR-fdvTsw99l&index=2')

    with col3:
            st.subheader("Cara Menampilkan Data")
            st.video('https://www.youtube.com/watch?v=dIx4ccvKduU&list=PLm94WimySTnr_AllzUeBTZR-fdvTsw99l&index=3')

    st.header("[Daftar Video Playlist Belajar Streamlit Bahasa Indonesia [Dasar]](https://www.youtube.com/c/Avra_b)")

    st.write("---")
    
    st.markdown("""
    ### ⭐ ☕️🤗 Support channel youtube Kelas Awan Pintar !  
    [Kelas Awan Pintar](https://www.youtube.com/@kelasawanpintar)
    -------------
        """, False)
# Akhir Content About

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
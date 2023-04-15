import streamlit as st
from audio_recorder_streamlit import audio_recorder
import speech_recognition as sr
import pytesseract
import PIL.Image
from audio_utils import convert_bytes_to_wav
from audio_utils import text_to_speech
from pinecone_utils import addData
from pinecone_utils import find_match
from pdf_utils import extract_text_from_pdf
from pdf_utils import split_text_into_chunks
from prompt_utils import create_prompt
from request_utils import generate_answer


def update_database():
    uploaded_file = st.file_uploader(
        "Choose a PDF file to train", type="pdf")

    if uploaded_file is not None:

        text = extract_text_from_pdf(uploaded_file)

        # Close the PDF file object
        uploaded_file.close()

        text_chunks = split_text_into_chunks(text, 3000)
        print(text_chunks)
        plain_text_chunks = text_chunks

        addData(plain_text_chunks)


def search_database():
    text_input = ""

    option_in = st.selectbox(
        "Select Input Type", ("Text", "Audio", "Image"))
    if option_in == "Text":
        text_input = st.text_input("Enter your query here:")
    elif option_in == "Audio":
        # st.write("Click the button below to start recording")

        audio_bytes = audio_recorder()
        if audio_bytes:
            # st.audio(audio_bytes, format="audio/wav")
            convert_bytes_to_wav(audio_bytes)

            r = sr.Recognizer()
            # Load the audio file
            with sr.AudioFile("audio.wav") as source:
                audio = r.record(source)

            # Convert audio to text
            audio_text = r.recognize_google(audio)

            st.write("Your query: ", audio_text)
            text_input = audio_text
    else:
        # pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'

        image_file = st.file_uploader(
            "Upload image", type=["png", "jpg", "jpeg"])
        if image_file is not None:
            # Load the image using PIL
            image = PIL.Image.open(image_file)

            # Convert the image to grayscale
            gray_image = image.convert('L')

            # Perform OCR on the grayscale image using Tesseract
            text = pytesseract.image_to_string(gray_image)

            st.write("Your query: ", text)
            text_input = text

    options = ["Short", "Medium", "Long"]
    selected_option = st.selectbox("Select the type of question", options)
    # st.write("Selected option:", selected_option)

    k = 1
    if selected_option == 'Short':
        k = 1
    else:
        k = 2

    if text_input != "":
        query = text_input
        docs, res = find_match(query, k)

        # print(res)

        context = "\n\n".join(res)
        prompt = create_prompt(context, query, selected_option)

        reply = generate_answer(prompt)
        st.write(reply)

        if st.button("Convert to speech"):
            fp = text_to_speech(reply)
            st.audio(fp.getvalue())


def main():

    st.title(" CheatGPT ")

    option = st.radio(
        "Select an option:",
        ("Search database", "Update database")
    )

    if option == "Update database":
        update_database()

    elif option == "Search database":
        search_database()


if __name__ == "__main__":
    main()

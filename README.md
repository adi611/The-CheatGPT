# **CheatGPT**

This project demonstrates the integration of multiple NLP models and databases in a streamlit application. It uses OpenAI's GPT-3 to answer questions based on provided contexts. The contexts are in the form of text extracted from PDF files uploaded by the user. The application utilizes the following libraries:

- **`SentenceTransformer`**: This library is used to encode text input into 384 dimensional embeddings.
- **`Streamlit`**: This is a web framework for creating and sharing data-driven applications.
- **`IPython.display`**: This library is used to display audio files in the streamlit application.
- **`gTTS`**: This library is used to convert text to speech.
- **`audio_recorder_streamlit`**: This library is used to record audio in the streamlit application.
- **`speech_recognition`**: This library is used to transcribe speech.
- **`wave`**: This library is used to save audio files in **`.wav`** format.
- **`io`**: This library is used to load audio files into memory.
- **`Pinecone`**: This library is used to create and query a vector index for text embeddings.
- **`requests`**: This library is used to send HTTP requests.
- **`PyPDF2`**: This library is used to extract text from PDF files.
- **`pytesseract`**: This library is used to OCR (Optical Character Recognition) image files.
- **`Pillow`**: This library is used to load images.

## **Usage**

Before running the application, you will need to create a **`.env`** file in the root directory of the project with the following keys:

- **`PINECONE_KEY`**: API key for Pinecone.
- **`GPT_KEY`**: API key for OpenAI GPT-3.

Once you have created the **`.env`** file, you can run the application by running the following command in your terminal:

1. Clone the repository:

```
git clone https://github.com/adi611/The-CheatGPT.git
```

2. Navigate to the project directory:

```
cd The-CheatGPT
```

3. Install the required dependencies:

```
pip install -r requirements.txt
```

4. Run the Streamlit app:

```
streamlit run app.py
```

Follow the instructions in the Streamlit app to interact with the different features.

## **Features**

### **Text to Speech**

This section allows you to enter text and convert it to speech. The text is converted to an audio file using the **`gTTS`** library and played back using the **`IPython.display`** library.

### **Speech to Text**

This section allows you to record audio and transcribe it to text using the **`speech_recognition`** library. The audio is recorded using the **`audio_recorder_streamlit`** library and saved to a **`.wav`** file using the **`wave`** library. The text is transcribed using the Google Speech Recognition API.

### **OCR**

This section allows you to upload an image file and extract text using OCR. The image file is loaded using the **`Pillow`** library and the text is extracted using the **`pytesseract`** library.

### **Question Answering**

This section allows you to ask a question and receive an answer from a pre-built corpus of text. The corpus is indexed using the **`Pinecone`** library and the embeddings are generated using the **`SentenceTransformer`** library. The question is then answered using the OpenAI GPT-3 API.

### **Database Update**

This section allows you to upload a PDF file and update the pre-built corpus of text. The PDF file is loaded using the **`PyPDF2`** library and the text is extracted from each page. The text is then split into chunks and indexed using the **`Pinecone`** library.

## **Libraries used**

- **[SentenceTransformers](https://github.com/UKPLab/sentence-transformers)**
- **[Streamlit](https://streamlit.io/)**
- **[IPython](https://ipython.org/)**
- **[gTTS](https://gtts.readthedocs.io/en/latest/)**
- **[audio-recorder-streamlit](https://github.com/dvcrn/audio-recorder-streamlit)**
- **[SpeechRecognition](https://github.com/Uberi/speech_recognition)**
- **[PyPDF2](https://github.com/mstamy2/PyPDF2)**
- **[Pillow](https://python-pillow.org/)**
- **[dotenv](https://github.com/theskumar/python-dotenv)**
- **[Pinecone](https://www.pinecone.io/)**
- **[requests](https://requests.readthedocs.io/en/latest/)**
- **[pytesseract](https://github.com/madmaze/pytesseract)**

## **License**

This project is licensed under the MIT License - see the **LICENSE.md** file for details.

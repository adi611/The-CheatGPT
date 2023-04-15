# CheatGPT
This is a Python program that uses OpenAI's GPT-3 to answer questions based on provided contexts. The contexts are in the form of text extracted from PDF files uploaded by the user.

## Prerequisites
Before running the program, make sure to have the following libraries installed:

- os
- streamlit
- PyPDF2
- requests
- pinecone
- sentence_transformers

You also need to have API keys for Pinecone and OpenAI. Set your Pinecone API key as an environment variable with the name "PINECONE_KEY", and OpenAI API key as an environment variable with the name "GPT_KEY".

## How to use
1. Run the program by executing the command streamlit run <filename>.py in the terminal, replacing <filename> with the name of the Python file.
2. Upload a PDF file by clicking on the "Choose a PDF file" button.
3. The program extracts the text from the PDF file and splits it into chunks of 3000 characters.
4. The chunks are then encoded using SentenceTransformer and added to a Pinecone index.
5. Enter your query in the text input box and click on the "Submit" button.
6. The program finds the most relevant chunk of text from the PDF file based on the query using Pinecone's nearest neighbor search.
7. The program then creates a prompt by combining the context with the query, and passes it to OpenAI's GPT-3 to generate a response.
8. The response is displayed on the screen.

Note: If the answer is not contained within the text and requires some latest information to be updated, the program will print "Sorry Not Sufficient context to answer query".

## Libraries Used
- os: Provides a way of using operating system dependent functionality.
- streamlit: A Python library used for creating web apps.
- PyPDF2: A Python library used for working with PDF files.
- requests: A Python library used for sending HTTP requests.
- pinecone: A managed vector database service for building fast and accurate machine learning applications.
- sentence_transformers: A Python library used for encoding text into vectors.

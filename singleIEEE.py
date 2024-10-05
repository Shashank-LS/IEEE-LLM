import fitz  # PyMuPDF
import spacy
import requests
import csv
from sentence_transformers import SentenceTransformer, util
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Load spaCy NLP Model
nlp = spacy.load('en_core_web_sm')


# Function to upload a PDF file
def upload_pdf():
    Tk().withdraw()  # Prevent Tk window from appearing
    filename = askopenfilename(filetypes=[("PDF files", "*.pdf")])  # Open file dialog
    return filename


# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text("text")
    doc.close()
    return text


# Process the extracted text with spaCy
def process_text(text):
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    sentences = [sent.text for sent in doc.sents]
    return entities, sentences


# Function to query LLM Studio API for RAG fallback
def query_llm_studio(prompt, endpoint='http://192.168.247.1:1234/v1/chat/completions'):
    headers = {
        'Content-Type': 'application/json',
    }
    data = {
        "model": "lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF/Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf",
        "messages": [{"role": "user", "content": prompt}],
    }
    response = requests.post(endpoint, json=data, headers=headers)
    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None


# Function to retrieve the most relevant passage for a query
def retrieve_passage(query, sentences, sentence_embeddings):
    query_embedding = embedder.encode(query, convert_to_tensor=True)
    cos_scores = util.pytorch_cos_sim(query_embedding, sentence_embeddings)[0]
    best_idx = cos_scores.argmax()
    return sentences[best_idx], cos_scores[best_idx].item()


# Load sentence transformer model
embedder = SentenceTransformer('all-MiniLM-L6-v2')

# Upload PDF file
pdf_path = upload_pdf()
if pdf_path:
    # Extract text and process it
    text = extract_text_from_pdf(pdf_path)
    entities, sentences = process_text(text)

    # Encode sentences from the document
    sentence_embeddings = embedder.encode(sentences, convert_to_tensor=True)

    # Initialize context for conversation
    context = ""

    # Prepare CSV file for output
    csv_filename = "output.csv"
    with open(csv_filename, mode='w', newline='') as csv_file:
        fieldnames = ['Question', 'LLM Response', 'Verification']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        while True:
            # Ask the user for a query
            query = input("Enter your question about the document (or type 'exit' to quit): ")
            if query.lower() == 'exit':
                break

            # Retrieve the best sentence for context
            best_sentence, score = retrieve_passage(query, sentences, sentence_embeddings)

            # Generate answer using the LLM Studio API
            prompt = f"Document section: '{best_sentence}'. Previous answer: '{context}'. Question: '{query}'. Please answer only what is necessary and nothing more."
            answer = query_llm_studio(prompt)

            # Update context with the latest answer
            context = answer.strip()

            # Print results
            print(f"Best Sentence: {best_sentence}\nScore: {score}")
            print(f"Generated Answer: {answer.strip()}")

            # Write to CSV file
            writer.writerow({'Question': query, 'LLM Response': answer.strip(), 'Verification': ''})

    print(f"Output saved to {csv_filename}.")
else:
    print("No file selected.")

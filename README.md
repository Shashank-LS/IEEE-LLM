# PDF Query Assistant with LLM and Sentence Transformers

This project provides an interactive system that allows users to upload a PDF, ask questions related to its content, and get precise answers from a local instance of LLM Studio. The system retrieves relevant passages from the document using semantic similarity and generates responses using a language model. The questions, answers, and a verification column are saved in a CSV file.

## Features

- Upload and extract text from PDF files.
- Process text with spaCy to extract sentences and named entities.
- Use a pre-trained Sentence Transformer model (`all-MiniLM-L6-v2`) to retrieve the most relevant passages from the document based on user queries.
- Query a local instance of LLM Studio to generate answers based on the extracted content.
- Save questions, responses, and a blank verification field to a CSV file for later review.

## Prerequisites

Before running this project, ensure you have the following installed:

1. **Python 3.6+**
2. **Python Libraries**:
   - `fitz` (PyMuPDF)
   - `spaCy`
   - `requests`
   - `csv` (part of Python standard library)
   - `sentence-transformers`
   - `torch` (if required for `sentence-transformers`)
   - `tkinter` (for file dialog)

3. **LLM Studio**:
   - You need a local instance of [LLM Studio] running on your machine.
   - Ensure it's accessible at `http://192.168.247.1:1234/v1/chat/completions` or update the endpoint in the script accordingly.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/YourUsername/your-repository.git
   cd your-repository

2. Install the required Python libraries:
   ```bash
   pip install pymupdf spacy requests sentence-transformers torch
   
3. Download and set up the spaCy NLP model:
   ```bash
   python -m spacy download en_core_web_sm
   
4. Ensure LLM Studio is set up and running on the local machine.

## Usage

1. Run the script:
   ```bash
   python singleIEEE.py

2. The system will prompt you to upload a PDF file through a file dialog.

3. After uploading the PDF, you can ask questions about the content. The system will:
   1. Retrieve the most relevant section from the document.
   2. Generate a response from the LLM Studio instance.
   3. Save the question, answer, and verification to output.csv.
      
4. Type exit to quit the program.

5. **Check the output:** The extracted features and testing methods will be saved in 'output.csv`.

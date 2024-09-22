# PDF Feature Extraction and Testing Methods

This repository contains a Python script that extracts features and testing methods from technical documents in PDF format using a local language model. The extracted data is saved in a CSV file for easy analysis and reference.

## Features

- Reads text content from PDF documents.
- Queries a local language model API to extract features and their corresponding testing methods.
- Saves the extracted information into a structured CSV file.

## Requirements

To run the script, you'll need:

- Python 3.x
- The following Python packages:
  - `requests`
  - `pdfplumber`
  - `pandas`
  - `tkinter` (included with standard Python installations)

You can install the required packages using pip:

<pre>
pip install requests pdfplumber pandas
</pre>

## Usage

1. **Clone the repository:**
   <pre>
   git clone https://github.com/Shashank-LS/IEEE-LLM.git
   cd IEEE-LLM
   </pre>

2. **Run the script:**
   <pre>
   python RAG-LLaMA.py
   </pre>

3. **Select the PDF document** when prompted. The script will analyze the document.

4. **Check the output:** The extracted features and testing methods will be saved in `features_testing_methods.csv`.

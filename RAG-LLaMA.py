import requests
import pdfplumber
import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Function to read PDF content
def read_pdf(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

# Function to query LM Studio API
def query_lm_studio(prompt, endpoint='http://192.168.247.1:1234/v1/chat/completions'):
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

# Function to extract features and testing methods from the LLM response
def extract_features_and_testing_methods(text):
    features = []
    testing_methods = []

    # Example prompts
    prompts = [
        "Identify and list the operations supported by the APB protocol.",
        "For each operation listed, describe the steps needed to execute it and how to test its correctness."
    ]

    for prompt in prompts:
        response = query_lm_studio(prompt)
        if response:
            # Parsing responses (this might need adjustment based on actual responses)
            lines = response.split('\n')
            if len(lines) > 1:
                for line in lines:
                    parts = line.split(':')
                    if len(parts) == 2:
                        feature = parts[0].strip()
                        testing_method = parts[1].strip()
                        features.append(feature)
                        testing_methods.append(testing_method)

    return features, testing_methods

# Main execution
def main():
    # Create a Tkinter root window (it will not be shown)
    root = Tk()
    root.withdraw()

    # Ask user to select the PDF document
    pdf_path = askopenfilename(title="Select the Technical Document (PDF)", filetypes=[("PDF files", "*.pdf")])
    if not pdf_path:
        print("No file selected. Exiting...")
        return

    # Extract text from PDF
    document_text = read_pdf(pdf_path)

    # Extract features and testing methods from LLM
    features, testing_methods = extract_features_and_testing_methods(document_text)

    # Create DataFrame and save to CSV
    df = pd.DataFrame({
        'Feature Supported': features,
        'Execution Steps': testing_methods,
        'Testing Method': ['Verify' for _ in features]  # Placeholder for additional column
    })
    csv_path = "features_testing_methods.csv"
    df.to_csv(csv_path, index=False)
    print(f"Data successfully saved to {csv_path}")

if __name__ == "__main__":
    main()
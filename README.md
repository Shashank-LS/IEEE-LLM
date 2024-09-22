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

```bash
pip install requests pdfplumber pandas

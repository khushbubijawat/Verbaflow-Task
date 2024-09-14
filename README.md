# Verbaflow-Task

# LinkedIn PDF to HTML Resume Generator

This is a Flask web application that converts a PDF resume downloaded from LinkedIn into a structured HTML resume using OpenAI's GPT-4 API.

## Features
- Upload a PDF file (specifically LinkedIn resume PDFs).
- Extracts text from the PDF using `PyPDF2`.
- Converts the extracted text into a structured HTML resume using OpenAI's GPT-4 API.
- Allows the user to download the generated HTML resume.

## Prerequisites

Before you begin, ensure you have the following installed on your machine:

- Python 3.7+
- Flask
- PyPDF2
- OpenAI Python SDK (`openai`)

You will also need an OpenAI API key to access GPT-4.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/linkedin-pdf-to-html-resume.git
   cd linkedin-pdf-to-html-resume

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

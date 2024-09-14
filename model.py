
# from flask import Flask, request, send_file
# from PyPDF2 import PdfReader
# import openai
# import io
# import os

# app = Flask(__name__)

# # Load OpenAI API key
# openai.api_key = ""

# # # Set your OpenAI API key (recommended to set via environment variable)
# # openai.api_key = os.getenv('OPENAI_API_KEY')

# def extract_text_from_pdf(pdf_file):
#     pdf_text = ""
#     reader = PdfReader(pdf_file)
#     for page in reader.pages:
#         pdf_text += page.extract_text()
#     return pdf_text

# def generate_html_with_gpt(text):
#     # Use GPT-4 to convert extracted text into an HTML resume
#     response = openai.ChatCompletion.create(
#         model="gpt-4",
#         messages=[
#             {
#                 "role": "system",
#                 "content": "You are a helpful assistant that converts LinkedIn resume text into well-structured HTML resumes."
#             },
#             {
#                 "role": "user",
#                 "content": f"Convert the following LinkedIn resume text into a well-structured HTML resume: \n\n{text}"
#             }
#         ],
#         max_tokens=2000,
#         temperature=0.7
#     )
    
#     # Extract the HTML content from the response
#     html_resume = response['choices'][0]['message']['content']
#     return html_resume

# @app.route('/', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         if 'file' not in request.files:
#             return 'No file part'
        
#         file = request.files['file']
#         if file.filename == '':
#             return 'No selected file'
        
#         if file and file.filename.endswith('.pdf'):
#             # Extract text from the uploaded PDF
#             pdf_text = extract_text_from_pdf(file)
#             # Generate HTML resume using GPT-4
#             html_resume = generate_html_with_gpt(pdf_text)
            
#             # Use BytesIO for binary response
#             output_file = io.BytesIO(html_resume.encode('utf-8'))
#             return send_file(
#                 output_file,
#                  download_name='resume.html',
#                 as_attachment=True,
#                 mimetype='text/html'
#             )
    
#     return '''
#     <!doctype html>
#     <title>Upload LinkedIn PDF</title>
#     <h1>Upload LinkedIn PDF</h1>
#     <form action="" method=post enctype=multipart/form-data>
#       <input type=file name=file>
#       <input type=submit value=Upload>
#     </form>
#     '''

# if __name__ == '__main__':
#     app.run(debug=True)



from flask import Flask, request, send_file
from PyPDF2 import PdfReader
import openai
import io
import os

app = Flask(__name__)

# Load OpenAI API key
openai.api_key = ""
def extract_text_from_pdf(pdf_file):
    pdf_text = ""
    reader = PdfReader(pdf_file)
    for page in reader.pages:
        pdf_text += page.extract_text()
    return pdf_text

def generate_html_with_gpt(text):
    # Use GPT-4 to convert extracted text into an HTML resume
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant that converts LinkedIn resume text into well-structured HTML resumes."
            },
            {
                "role": "user",
                "content": f"Convert the following LinkedIn resume text into a well-structured HTML resume: \n\n{text}"
            }
        ],
        max_tokens=2000,
        temperature=0.7
    )
    
    html_resume = response['choices'][0]['message']['content']
    return html_resume

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'
        
        file = request.files['file']
        if file.filename == '':
            return 'No selected file'
        
        if file and file.filename.endswith('.pdf'):
            # Extract text from the uploaded PDF
            pdf_text = extract_text_from_pdf(file)
            # Generate HTML resume using GPT-4
            html_resume = generate_html_with_gpt(pdf_text)
            
            output_file = io.BytesIO(html_resume.encode('utf-8'))
            return send_file(
                output_file,
                download_name='resume.html',
                as_attachment=True,
                mimetype='text/html'
            )
    
    return '''
    <!doctype html>
    <html lang="en">
    <head>
        <title>Upload LinkedIn PDF</title>
        <style>
            body {
                background-color: #00264d;
                color: white;
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .container {
                background-color: #00509e;
                padding: 20px;
                border-radius: 10px;
                text-align: center;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
            }
            input[type="file"] {
                margin: 10px 0;
                padding: 10px;
                border-radius: 5px;
                background-color: #f0f0f0;
            }
            input[type="submit"] {
                padding: 10px 20px;
                border: none;
                background-color: #ff6600;
                color: blue;
                border-radius: 5px;
                cursor: pointer;
            }
            input[type="submit"]:hover {
                background-color: #cc5200;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Upload LinkedIn PDF</h1>
            <form action="/" method="post" enctype="multipart/form-data">
                <input type="file" name="file"><br>
                <input type="submit" value="Upload">
            </form>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)

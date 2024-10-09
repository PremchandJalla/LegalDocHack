from flask import Flask, render_template, request, redirect, url_for
from openai import OpenAI
import os
from PyPDF2 import PdfReader  # Import PyPDF2 for PDF reading
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './uploads'

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Nvidia NIM Client Setup
client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.getenv("OPENAI_API_KEY")  # Load API key from environment variable
)

def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ''
    for page in reader.pages:
        text += page.extract_text()
    return text

def ask_question(model, document_text, user_question):
    prompt = f"Document: {document_text}\nQuestion: {user_question}\nAnswer:"
    
    # Make the request to the Nvidia NIM API
    completion = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
        top_p=0.7,
        max_tokens=1024,
        stream=False
    )
    
    # Check the response type and inspect it
    print(completion)  # Log the completion object to see its structure

    # Access the message content (adjust based on the API response structure)
    response_message = completion.choices[0].message.content
    
    return response_message


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "Please upload a file.", 400
        
        file = request.files['file']
        if file.filename == '':
            return "No file selected.", 400
        
        if file:
            # Save the uploaded file
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            
            # Check if the uploaded file is a PDF
            if file.filename.endswith('.pdf'):
                document_text = extract_text_from_pdf(filepath)
            else:
                # If it's not a PDF, assume it's a text file
                with open(filepath, 'r', encoding='utf-8') as f:
                    document_text = f.read()
            
            # Get user question
            question = request.form.get('question')
            
            # Ask the LLM for an answer
            answer = ask_question("mistralai/mistral-7b-instruct-v0.3", document_text, question)
            
            return answer  # Return just the answer as plain text
    
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

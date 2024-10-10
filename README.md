# Legal Document Q&A Powered by NVIDIA NIM Mistral AI

A web application that allows users to upload legal documents (such as lease agreements) in PDF format and ask questions about the document's content. The system parses the document and provides answers to user queries based on the extracted information. The application now integrates **NVIDIA NIM Mistral AI** for enhanced question-answering performance, making it more effective in handling complex legal queries.

## Features

- **Document Upload**: Users can upload legal documents (PDF format), such as lease agreements, contracts, or any legal text.
- **PDF Parsing**: The application extracts text from the uploaded PDF file using `PyPDF2` or another PDF parsing library.
- **NVIDIA NIM Mistral AI Integration**: Powered by **NVIDIA NIM Mistral AI**, the application provides highly accurate and context-aware answers to complex legal queries.
- **Question & Answer Functionality**: Users can ask questions related to the uploaded document, and the system provides answers by referencing the document's contents with the help of Mistral AI.
- **Simple and Intuitive Interface**: Easy file uploads and question inputs allow users to interact with their legal documents seamlessly.

## How It Works

1. **Upload Legal Document**: The user uploads a PDF file, such as a lease agreement or legal contract.
2. **Text Extraction**: The system processes the document and extracts its contents into plain text using `PyPDF2`.
3. **Question Input**: Users can input their legal questions in the provided text box.
4. **Mistral AI Document Querying**: The application uses **NVIDIA NIM Mistral AI** to interpret the query, search for relevant sections within the document, and generate contextually accurate responses.
5. **Answer Display**: The system returns the most relevant sections or answers based on the user's question.

## Usage

- **Legal Document Queries**: Perfect for users who want to quickly reference key details from legal documents without manually searching the text.
- **Lease Agreements**: Ideal for tenants and landlords who need quick answers about specific clauses in rental agreements.
- **Contracts**: Useful for contract reviews where users can query specific terms and conditions.

## Technologies Used

- **Flask**: Web framework used for handling requests, routing, and rendering templates.
- **PyPDF2**: Library used for extracting text from PDF documents.
- **NVIDIA NIM Mistral AI**: Cutting-edge AI model used for generating accurate responses to legal queries.
- **HTML/CSS**: For rendering the user interface for file uploads and displaying results.

## Application Workflow

1. **Upload Document**: The user uploads a PDF containing legal information.
2. **Parse Document**: The system extracts the text from the uploaded document.
3. **Input Query**: The user types a question related to the document in a text input field.
4. **Generate Answer**: NVIDIA Mistral AI generates an accurate answer based on the document's contents.
5. **Display Result**: The generated answer is displayed to the user in an easy-to-read format.

## Screenshots

![image](https://github.com/user-attachments/assets/faad3c33-be2d-414a-96ec-4810ed34d1c5)


*The user uploads a PDF document containing the legal agreement.*

![image](https://github.com/user-attachments/assets/8406cd02-9671-420b-8705-a0c92a22519a)


*Users input a legal question for querying.*

![image](https://github.com/user-attachments/assets/90ea3d6f-be61-4fc6-8a32-92327156d6e2)


*NVIDIA Mistral AI returns an answer based on the content of the document.*

## How to Run the Application

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/legal-document-qna.git
   cd legal-document-qna

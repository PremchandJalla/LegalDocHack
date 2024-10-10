# Legal Document Q&A Powered by NVIDIA NIM Mistral AI

A web application that allows users to upload legal documents (such as lease agreements) in PDF format and ask questions about the document's content. The system parses the document and provides answers to user queries based on the extracted information. The application integrates **NVIDIA NIM Mistral AI** for enhanced question-answering performance, and **Cloudera AMP** for managing and scaling the machine learning workflow.

## Features

- **Document Upload**: Users can upload legal documents (PDF format), such as lease agreements, contracts, or any legal text.
- **PDF Parsing**: The application extracts text from the uploaded PDF file using `PyPDF2` or another PDF parsing library.
- **NVIDIA NIM Mistral AI Integration**: Powered by **NVIDIA NIM Mistral AI**, the application provides highly accurate and context-aware answers to complex legal queries.
- **Question & Answer Functionality**: Users can ask questions related to the uploaded document, and the system provides answers by referencing the document's contents with the help of Mistral AI.
- **Cloudera AMP Integration**: The system uses **Cloudera AMP** for scalable machine learning operations, model deployment, and monitoring.
- **Simple and Intuitive Interface**: Easy file uploads and question inputs allow users to interact with their legal documents seamlessly.

## How It Works

1. **Upload Legal Document**: The user uploads a PDF file, such as a lease agreement or legal contract.
2. **Text Extraction**: The system processes the document and extracts its contents into plain text using `PyPDF2`.
3. **Question Input**: Users can input their legal questions in the provided text box.
4. **Mistral AI Document Querying**: The application uses **NVIDIA NIM Mistral AI** to interpret the query, search for relevant sections within the document, and generate contextually accurate responses.
5. **Answer Display**: The system returns the most relevant sections or answers based on the user's question.
6. **Cloudera AMP for Model Management**: The application leverages **Cloudera AMP** for managing machine learning workflows, handling data at scale, and monitoring the deployed model to ensure high availability and accuracy.

## How to Run the Application

1. **Clone the repository**:
   - Open your terminal and run the following command to clone the repository:
     ```bash
     git clone https://github.com/your-repo/LegalDocHack.git
     cd LegalDocHack
     ```

2. **Set up a virtual environment (optional but recommended)**:
   - To avoid conflicts with other packages, create a virtual environment:
     ```bash
     python -m venv env
     source env/bin/activate  # On Windows: env\Scripts\activate
     ```

3. **Install the required dependencies**:
   - Run the following command to install all necessary Python packages:
     ```bash
     pip install -r requirements.txt
     ```

4. **Run the Flask application**:
   - After the dependencies are installed, run the Flask app with:
     ```bash
     python app/main.py
     ```

5. **Access the application**:
   - Open your web browser and go to `http://127.0.0.1:5000/` to start using the application.
   - You will be able to upload a legal document (such as a lease agreement) and ask questions related to its content.

6. **Stopping the app**:
   - To stop the app, go to your terminal window where the Flask server is running and press `CTRL + C`.
  

## Running the Application as an AMP

To run this application as an **AMP (Applied Machine Learning Prototype)**, you will need to integrate it with **Cloudera CML** and use an API key from **NVIDIA NIM** to access the **Mistral AI model**. Follow these steps:

1. **Set up your Cloudera AMP environment**:
   - Ensure you have access to **Cloudera CML** and configure your environment with the necessary permissions and libraries.

2. **Obtain an NVIDIA NIM API Key**:
   - To access the **NVIDIA NIM Mistral AI** for generating legal document Q&A, you will need an API key from NVIDIA. You can request an API key by visiting the following link:
     [Get NVIDIA NIM API Key] ([https://developer.nvidia.com/nvidia-nim-api-key](https://build.nvidia.com/mistralai/mistral-7b-instruct-v03))

3. **Set the API Key in your environment**:
   - Once you have obtained the API key, set it in your environment:


## Future Enhancements

### 1. **Retrieval-Augmented Generation (RAG) Knowledge Base**
   - Integrating a **RAG** system will allow the application to use a vectorized knowledge base for improved legal document understanding. The system will retrieve relevant sections of the document based on the user’s query before generating an answer.
   - **RAG Pipeline**: Utilize FAISS or another vector search engine to retrieve sections of the document that are relevant to the question. 
   - The retrieval step will be followed by the **NVIDIA NIM Mistral AI** model generating a more contextually accurate answer using the retrieved information.

### 2. **Fine-Tuning with Reinforcement Learning for a Feedback Loop**
   - Implement a **reinforcement learning feedback loop** to improve the model’s performance over time. The model will learn from user feedback (e.g., thumbs up/down or corrections to answers) to improve its ability to understand and answer legal questions.
   - **Reinforcement Learning**: Fine-tune the **Mistral AI** model with feedback signals from the users. Positive feedback (correct answers) will increase the likelihood of similar outputs in the future, while negative feedback will help reduce errors.
   - This loop will enable the model to continually evolve and improve in answering complex legal queries.

### 3. **LLMOps Integration**
   - Implement **LLMOps** (Large Language Model Operations) for more robust model monitoring, versioning, and feedback-driven updates.
   - **LLMOps Workflow**: This will include version control for model updates, model retraining based on real-time data, monitoring for quality assurance, and better model deployment strategies for scalable LLMs. With **LLMOps**, the entire lifecycle of the **Mistral AI** model will be streamlined from development to production.


### 4. **User Context Awareness**
   - Integrate **user context awareness** to personalize responses based on the user’s identity or previous interactions with the system. This will allow the system to remember previous questions and offer more contextually relevant answers over time.
   - **Contextual Understanding**: Implement user sessions or profiles that track previous legal queries, tailoring future responses based on the user’s history with the system.


## Screenshots

![image](https://github.com/user-attachments/assets/faad3c33-be2d-414a-96ec-4810ed34d1c5)


*The user uploads a PDF document containing the legal agreement.*

![image](https://github.com/user-attachments/assets/8406cd02-9671-420b-8705-a0c92a22519a)


*Users input a legal question for querying.*

![image](https://github.com/user-attachments/assets/90ea3d6f-be61-4fc6-8a32-92327156d6e2)


*NVIDIA Mistral AI returns an answer based on the content of the document.*



![image](https://github.com/user-attachments/assets/87ff55b0-a15b-4e62-84d2-2ece541bcd65)


*NVIDIA Mistral AI returns summary of  the content of the document.*


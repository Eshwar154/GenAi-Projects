# GenAI Projects

Welcome to the **GenAI Projects** repository! This collection of projects demonstrates various applications of Generative AI, leveraging powerful tools and frameworks like **Google Generative AI**, **LangChain**, **Streamlit**, and **FAISS**. Each project in this repository aims to explore unique uses of AI, offering hands-on solutions and engaging user experiences.

---

## 📂 Projects in this Repository

### 1. **Chat with Multiple PDFs**
An interactive application that allows users to upload multiple PDF files, extract their content, and interact with the system using a conversational AI interface. Ask questions related to the PDF content, and the AI will provide answers based on the extracted information.

#### Key Features:
- Upload and process multiple PDFs.
- Text extraction using **PyPDF2**.
- Split the extracted text into manageable chunks using **LangChain**.
- Use **FAISS** for semantic search of relevant chunks.
- Interactive Q&A with the **Google Generative AI** model.
- Built with **Streamlit** for the frontend interface.

---

## 🛠 Tools & Technologies

This repository uses the following tools and frameworks to implement the AI-driven solutions:

- **Streamlit**: For building interactive and user-friendly web applications.
- **PyPDF2**: A PDF text extraction library.
- **LangChain**: A framework for developing applications with large language models (LLMs).
- **FAISS**: A library for efficient similarity search and clustering of dense vectors.
- **Google Generative AI**: For embeddings and conversational AI capabilities.
- **dotenv**: For secure environment variable management (like API keys).

---

## 🚀 How to Run

### Prerequisites
1. **Python 3.8+** installed on your system.
2. Clone the repository:
   ```bash
   git clone https://github.com/Eshwar154/GenAi-Projects.git
   cd GenAi-Projects

   Install the required dependencies:
bash
Copy code
pip install -r requirements.txt

Configuration
Create a .env file in the root directory.
Add your Google API key:
text
Copy code
GOOGLE_API_KEY=your_google_api_key_here
Running the Application
Launch the Streamlit app:
bash
Copy code
streamlit run app.py
Upload your PDF files, and interact with the AI-powered Q&A system.
🌟 Features
Multi-PDF Support: Upload and process multiple PDF files at once.
Contextual Q&A: The AI answers questions based on the content from the uploaded PDFs.
Fast Search: Semantic search powered by FAISS allows for quick retrieval of relevant document sections.
Generative AI: Get answers using Google's Gemini models for high-quality natural language understanding.
💡 Future Enhancements
Support for additional file formats (e.g., Word, Excel).
Enhanced document parsing and context management for better responses.
UI improvements with data visualizations and interactive features.
🧑‍💻 Author
Eshwar Paygude

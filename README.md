# PDF Retrieval Pipeline using LangChain and FAISS

## Project Overview

This project implements a Retrieval-Augmented Generation (RAG) retrieval pipeline for PDF documents using LangChain, Hugging Face Embeddings, and FAISS Vector Database.

The system loads a PDF file, splits the content into smaller chunks, converts the chunks into vector embeddings, stores them in a FAISS vector database, and retrieves the most relevant chunks based on user queries using similarity search.

---

## Technologies Used

* Python
* LangChain
* PyPDFLoader
* RecursiveCharacterTextSplitter
* Hugging Face Embeddings
* FAISS Vector Database
* Sentence Transformers

---

## Project Workflow

1. Load PDF document using PyPDFLoader.
2. Extract text from all pages.
3. Split text into smaller chunks using RecursiveCharacterTextSplitter.
4. Generate embeddings using Hugging Face Embeddings (`all-MiniLM-L6-v2`).
5. Store embeddings in FAISS Vector Database.
6. Perform similarity search based on user queries.
7. Retrieve the most relevant document chunks.

---

## Installation

Install the required packages:

```bash
python -m pip install langchain langchain-community langchain-huggingface langchain-text-splitters sentence-transformers faiss-cpu pypdf
```

---

## Running the Project

Place the PDF file in the same folder as the Python script.

Run:

```bash
python himachal_retriver.py
```

Enter a question when prompted.

Example:

```text
What adventure sports are available in Himachal Pradesh?
```

The system retrieves the most relevant chunks from the PDF.

---

## Features

* PDF Document Loading
* Text Chunking
* Embedding Generation
* FAISS Vector Storage
* Similarity Search
* Relevant Chunk Retrieval

---

## Sample Queries

* What adventure sports are available in Himachal Pradesh?
* Which tourist destinations are famous in Himachal Pradesh?
* Tell me about Kullu Dussehra.
* What animals are found in Himachal Pradesh?
* How does tourism contribute to the economy?

---

## Output

* Pages Loaded Successfully
* Text Chunks Generated
* FAISS Database Created
* Relevant Chunks Retrieved Based on Query

---

## Conclusion

This project demonstrates a complete retrieval pipeline for PDF documents using LangChain and FAISS. It enables efficient semantic search and retrieval of relevant information from large documents using vector embeddings and similarity search.
# RAG_himachal

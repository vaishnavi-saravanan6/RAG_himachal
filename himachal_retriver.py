from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

pdf_path = "Himachal_Pradesh_5_Page_RAG.pdf"

loader = PyPDFLoader(pdf_path)
documents = loader.load()

print("Pages Loaded:", len(documents))

splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50
)

chunks = splitter.split_documents(documents)

print("Total Chunks:", len(chunks))

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_db = FAISS.from_documents(
    chunks,
    embedding_model
)

vector_db.save_local("faiss_db")

print("FAISS database created successfully")

while True:
    query = input("\nAsk a question (or type exit): ")

    if query.lower() == "exit":
        break

    results = vector_db.similarity_search(query, k=3)

    for i, doc in enumerate(results):
        print(f"\n----- Result {i+1} -----")
        print(doc.page_content)
from fastapi import FastAPI, UploadFile, File, Form
from rag.utils.ingest import RAGIngestor
from rag.query import RAGQueryEngine
from rag.llm.answer_generator import AnswerGenerator

app = FastAPI()

ingestor = RAGIngestor()
retriever = RAGQueryEngine()
generator = AnswerGenerator()


@app.post("/ingest")
async def ingest_file(file: UploadFile = File(...)):
    contents = await file.read()
    path = f"data/{file.filename}"

    with open(path, "wb") as f:
        f.write(contents)

    result = ingestor.ingest_file(path)
    return result


@app.get("/query")
def query(question: str):
    return retriever.query(question)


@app.get("/chat")
def chat(question: str):
    results = retriever.query(question)
    context = " ".join([r["text"] for r in results["results"]])

    answer = generator.generate_answer(question, context)

    return {
        "question": question,
        "context_used": context,
        "answer": answer
    }

from fastapi import FastAPI
from bot.response_builder import build_response

app = FastAPI()

@app.get("/ask")
def ask_bot(question: str):
    answer = build_response(question)
    return {"response": answer}

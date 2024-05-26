from fastapi import APIRouter

from src.question.service import query_rag 

question_router = APIRouter(prefix="/question", tags=["Question"])

@question_router.get("/{question}")
def response_question(question: str):
    return {"question": question,  **query_rag(question)}
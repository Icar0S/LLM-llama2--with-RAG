from fastapi import APIRouter

question_router = APIRouter(prefix="/question", tags=["Question"])

@question_router.get("/{question}")
def response_question(question: str):
    return {"question_id": question}
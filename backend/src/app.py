from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.question.controller import question_router

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

app.include_router(question_router)
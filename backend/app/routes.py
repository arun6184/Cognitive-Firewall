from fastapi import APIRouter
from app.schemas import MessageRequest
from app.analyzer import analyze_message

router = APIRouter()

@router.post("/analyze")
def analyze(request: MessageRequest):
    result = analyze_message(request.text)
    return result

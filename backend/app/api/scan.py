from fastapi import APIRouter, Request
from app.services.scanner import run_scan

router = APIRouter()

@router.post("/scan")
async def scan(request: Request):
    payload = await request.json()
    target_url = payload.get("target_url")
    return await run_scan(target_url)

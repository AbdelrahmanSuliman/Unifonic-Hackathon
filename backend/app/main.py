from fastapi import FastAPI
from app.api.scan import router as scan_router
import sys

app = FastAPI()

app.include_router(scan_router, prefix="/api")

from pydantic import BaseModel, HttpUrl

class ScanRequest(BaseModel):
    target_url: HttpUrl

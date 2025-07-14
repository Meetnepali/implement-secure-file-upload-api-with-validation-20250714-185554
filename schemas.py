from pydantic import BaseModel, Field
from typing import Optional

class ImageMetadata(BaseModel):
    width: int
    height: int
    format: str

class ImageUploadResponse(BaseModel):
    filename: str
    metadata: ImageMetadata
    message: str = Field(example="Image uploaded successfully.")

class ImageUploadErrorResponse(BaseModel):
    error: str
    details: Optional[str] = None

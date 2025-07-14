import logging
import sys
from fastapi import FastAPI
from api.upload_router import router as upload_router

logging.basicConfig(
    level=logging.INFO,
    stream=sys.stdout,
    format='%(asctime)s %(levelname)s %(name)s %(message)s',
)
logger = logging.getLogger("asset_upload_api")

app = FastAPI(title="Campaign Asset Image Upload API")
app.include_router(upload_router, prefix="/api/upload", tags=["Upload"])

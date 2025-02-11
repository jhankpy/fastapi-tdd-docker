
from fastapi import APIRouter, HTTPException

from app.api import crud 
from app.models.pydantic import SummaryPayloadSchema, SummaryResponseSchema
from app.models.tortoise import SummarySchema

router = APIRouter()

@router.post("/", response_model= SummaryResponseSchema, status_code=201)
async def create_summary(payload: SummaryPayloadSchema) -> SummaryResponseSchema:
    summary_id = await crud.post(payload)

    response_object = {
        "id": summary_id,
        "url": payload.url
    }
    return response_object

@router.get("/{id}/", response_model=SummarySchema)
async def read_summary(id: int) -> SummarySchema:
    summary = await crud.get(id)

    return summary
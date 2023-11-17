from typing import Annotated

from fastapi import APIRouter, Path

router = APIRouter(prefix="/items", tags=["Items"])


@router.get("/latest/")
def get_latest_item():
    return {"id": 0, "message": "latest"}


@router.get("/{item_id}/")
def get_items(item_id: Annotated[int, Path(ge=1, lt=1_000_000)]):
    return {
        "item": {"id": item_id},
    }

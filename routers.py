from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi.params import Body
from typing import Optional


router = APIRouter()

@router.get("/")
async def read_root():
    return {"message": "Hello World"}
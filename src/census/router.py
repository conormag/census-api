from fastapi import Request
from fastapi import APIRouter
from src.census.schemas import SearchParams
from src.census.service import get_search_results


router = APIRouter()

@router.post("/search")
async def search_census(request: Request, search_params: SearchParams):
    """Search the census data"""
    return await get_search_results(search_params)
"""Service layer for census data."""
from fastapi import Request
from fastapi.responses import JSONResponse
from src.census.utils import get_results_count, get_results
from src.census.schemas import SearchParams


async def get_search_count(request: Request, 
                           search_params: SearchParams) -> JSONResponse:
    """Get the number of results and the number of pages"""
    total_results, num_pages = await get_results_count(search_params)
    return JSONResponse(
        content={"total_results": total_results, "num_pages": num_pages}
    )


async def get_search_results(search_params: SearchParams) -> JSONResponse:
    """Get the search results"""
    results = await get_results(search_params)
    return JSONResponse(content=results)


from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import date

class MovieDetailResponseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    date: Optional[date | str] = None
    score: float
    genre: str
    overview: Optional[str] = None
    crew: Optional[str] = None
    orig_title: Optional[str] = None
    status: Optional[str] = None
    orig_lang: Optional[str] = None
    budget: Optional[float | int | str] = None
    revenue: Optional[float | int | str] = None
    country: Optional[str] = None

class MovieListResponseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    movies: List[MovieDetailResponseSchema]
    prev_page: Optional[str] = None
    next_page: Optional[str] = None
    total_pages: int
    total_items: int

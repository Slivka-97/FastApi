from datetime import date
from typing import List

from pydantic import BaseModel, validator


class Genres(BaseModel):
    name: str


class Book(BaseModel):
    title: str
    author: str
    duration: str
    data: date
    summary: int
    genres: List[Genres]

    @validator('summary')
    def check_summary(cls, v):
        if v < 100:
            raise ValueError('Summary less 100')
        else:
            return v

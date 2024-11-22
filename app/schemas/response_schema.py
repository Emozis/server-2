from typing import Generic, TypeVar, Optional
from pydantic import BaseModel


T = TypeVar('T')

class ResponseSchema(BaseModel, Generic[T]):
    message: str
    data: Optional[T] = None
from pydantic import BaseModel


class PredictRequest(BaseModel):
    prompt: str
    response_len: int
    n: int


class PredictResponse(BaseModel):
    predictions: list[str]

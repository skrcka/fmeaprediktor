from pydantic import BaseModel


class PredictRequest(BaseModel):
    existing_analysis: dict
    existing_uniques: list[str]
    prediction_target: str
    response_len: int
    n: int


class PredictResponse(BaseModel):
    predictions: list[str]

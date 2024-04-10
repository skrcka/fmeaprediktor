import logging
from dataclasses import dataclass

from fmeaprediktor.connectors.openai_connector import OpenAIConnector
from fmeaprediktor.entities.predict import PredictRequest, PredictResponse

logger = logging.getLogger(__file__)


class PredictionController:
    @dataclass
    class Context:
        openai_connector: OpenAIConnector

    def __init__(self, context: Context) -> None:
        self._context = context

    async def predict(self, predict_request: PredictRequest) -> PredictResponse:
        existing_analysis = str(predict_request.existing_analysis)
        prediction_target = predict_request.prediction_target
        existing_uniques = predict_request.existing_uniques
        prompt = f"Given the following analysis: {existing_analysis}, predict the {prediction_target}. Please dont user the following words: {', '.join(existing_uniques)}"
        responses = await self._context.openai_connector.generate_response(
            prompt=prompt, max_words=predict_request.response_len, n=predict_request.n
        )
        return PredictResponse(predictions=responses)

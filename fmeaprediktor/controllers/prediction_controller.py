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
        responses = await self._context.openai_connector.generate_response(
            predict_request.prompt, predict_request.response_len, predict_request.n
        )
        return PredictResponse(predictions=responses)

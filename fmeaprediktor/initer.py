import configparser
import logging
from abc import ABC
from dataclasses import dataclass
from functools import lru_cache

from fmeaprediktor.connectors.openai_connector import OpenAIConnector
from fmeaprediktor.controllers.prediction_controller import PredictionController

logger = logging.getLogger(__name__)


@dataclass
class Initer(ABC):
    @dataclass
    class Config:
        openai_connector: OpenAIConnector.Config

    @dataclass
    class Context:
        openai_connector: OpenAIConnector = None
        prediction_controller: PredictionController = None

    @staticmethod
    @lru_cache
    def get_context() -> "Initer.Context":
        config = Initer._parse_ini_config()
        context = Initer.Context()
        context.openai_connector = OpenAIConnector(config.openai_connector)
        context.prediction_controller = PredictionController(context)
        return context

    @staticmethod
    async def initialize_context(context: Context) -> None:
        pass

    @staticmethod
    async def deinitialize_context(context: Context) -> None:
        pass

    @staticmethod
    def _parse_ini_config():
        config = configparser.ConfigParser()
        config.read("config.ini")
        logging.basicConfig(level=config.get("logging", "level"))
        return Initer.Config(
            openai_connector=OpenAIConnector.Config(
                api_key=config.get("openai_connector", "api_key"),
                model=config.get("openai_connector", "model"),
                system_message=config.get("openai_connector", "system_message"),
            ),
        )

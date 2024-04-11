import logging
from dataclasses import dataclass

import httpx

logger = logging.getLogger(__name__)


class OpenAIException(Exception):
    pass


class OpenAIConnector:
    @dataclass
    class Config:
        api_key: str
        model: str
        system_message: str

    def __init__(self, config: Config):
        self.api_key = config.api_key
        self.endpoint = "https://api.openai.com/v1/chat/completions"
        self.model = config.model
        self.system_message = config.system_message

    async def generate_response(self, prompt: str, max_words: int, n: int):
        headers = {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}
        data = {
            "messages": [
                {"role": "system", "content": self.system_message.format(max_words=max_words)},
                {"role": "user", "content": prompt},
            ],
            "model": self.model,
            "n": n,
        }

        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(self.endpoint, headers=headers, json=data)
                return self.parse_response(response)
            except Exception as e:
                logger.error(f"Error: {e}")
                raise OpenAIException(f"Error: {e}") from e

    @staticmethod
    def parse_response(response: httpx.Response) -> list[str]:
        if response.is_error:
            raise OpenAIException(f"Error: {response.text}")
        result = response.json()
        if not result:
            raise OpenAIException("No response")
        if "choices" not in result:
            raise OpenAIException("Invalid response format")
        choices = result["choices"]
        predictions = [choice["message"]["content"].strip().strip('\\"') for choice in choices]
        unique_predictions = list(set(predictions))
        return unique_predictions


async def main():
    config = OpenAIConnector.Config(
        api_key="YOUR_API_KEY",
        model="davinci",
        system_message="Translate the following English text to French: 'Hello, how are you?'",
    )
    connector = OpenAIConnector(config)
    prompt = "Translate the following English text to French: 'Hello, how are you?'"
    max_tokens = 60
    n = 3

    responses = await connector.generate_response(prompt, max_tokens, n)
    if "choices" in responses:
        for i, choice in enumerate(responses["choices"]):
            print(f"Response {i+1}: {choice['text'].strip()}")


# asyncio.run(main())

from openai import OpenAI
from typing import List, Dict
from config import OPENAI_API_KEY


class LLMClient:
    def get_client(self) -> OpenAI:
        """
        Get model client using API KEY
        :return: model client
        """
        return OpenAI(api_key=OPENAI_API_KEY)

    def create_chat_completion(self, messages: List[Dict[str, str]], system_prompt: str, temperature: float) -> str:
        """
        Create chat completion
        :param messages: list of chat messages
        :param system_prompt: string with instructions for model in system role
        :param temperature: controls how random is output of the model
        :return: answer of model
        """
        model_client = self.get_client()
        response = model_client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "system", "content": system_prompt}, *messages],
            temperature=temperature,
        )
        return response.choices[0].message.content.strip()

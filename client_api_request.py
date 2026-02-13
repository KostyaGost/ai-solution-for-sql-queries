from prompts import get_sql_query_prompt, get_explanation_prompt, get_correctness_prompt
from llm_client import LLMClient


class ClientAPIRequest:
    def __init__(self):
        self.llm_client = LLMClient()

    def is_valid_input(self, user_question: str, schema_description: str) -> bool:
        """
        Check correctness of user input
        :param user_question: user question about data
        :param schema_description: description of schema
        :return: True/False
        """
        content = (
            f"User question: {user_question}\n\n"
            f"Schema description: {schema_description}\n\n"
        )
        check_result = self.llm_client.create_chat_completion(
            messages=[{"role": "user", "content": content}],
            system_prompt=get_correctness_prompt(),
            temperature=0.0
        )
        if check_result == "VALID":
            return True

        return False

    def generate_sql_query(self, user_question: str, schema_description: str) -> str:
        """
        Generate SQL query according to schema description
        :param user_question: user question about data
        :param schema_description: description of schema
        :return: SQL query
        """
        content = (
            f"User question: {user_question}\n\n"
            f"Schema description: {schema_description}\n\n"
        )
        sql_query = self.llm_client.create_chat_completion(
            messages=[{"role": "user", "content": content}],
            system_prompt=get_sql_query_prompt(),
            temperature=0.1
        )
        return sql_query

    def generate_explanation(self, user_question: str, sql_query: str, result_preview: str) -> str:
        """
        Generate explanation for result dataframe
        :param user_question: user's question
        :param sql_query: SQL query
        :param result_preview: top rows of result dataframe
        :return:
        """
        content = (
            f"User question: {user_question}\n\n"
            f"Generated SQL query: {sql_query}\n\n"
            "First rows of result (markdown table):\n"
            f"{result_preview}\n\n"
        )
        explanation = self.llm_client.create_chat_completion(
            messages=[{"role": "user", "content": content}],
            system_prompt=get_explanation_prompt(),
            temperature=0.3,
        )
        return explanation

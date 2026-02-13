import click
from client_api_request import ClientAPIRequest
from data_manager import DataManager
from config import VALID_KEYWORDS


def is_valid_user_input_keyword(user_input: str) -> bool:
    """
    Check if user input is valid by searching for keywords
    :param user_input: user input
    :return: True/False
    """
    lowercase_input = user_input.lower()
    return any(keyword in lowercase_input for keyword in VALID_KEYWORDS)


@click.command()
def start_CLI():
    """
    Run user CLI
    :return: None
    """
    print("Start CLI.")

    client_api_request = ClientAPIRequest()
    data_manager = DataManager()

    while True:
        user_input = click.prompt('Question', type=str)

        if user_input.strip().lower() == "exit":
            break

        if not is_valid_user_input_keyword(user_input=user_input):
            print("Invalid question.")
            continue

        is_valid_input_llm = client_api_request.is_valid_input(
            user_question=user_input,
            schema_description=data_manager.build_schema_description(),
        )

        if not is_valid_input_llm:
            print("Invalid question.")
            continue

        sql_query = client_api_request.generate_sql_query(
            user_question=user_input,
            schema_description=data_manager.build_schema_description(),
        )

        result_df = data_manager.make_sql_query(sql_query=sql_query)
        print("Result:")
        print(result_df.to_markdown(index=True))

        explanation = client_api_request.generate_explanation(
            user_question=user_input,
            sql_query=sql_query,
            result_preview=result_df.head().to_markdown(index=False),
        )
        print("\nExplanation:")
        print(explanation)

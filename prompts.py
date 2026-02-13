from config import CHECK_CORRECTNESS_PROMPT_PATH, EXPLANATION_PROMPT_PATH, SQL_QUERY_PROMPT_PATH
from pathlib import Path


def read_prompt(path: str) -> str:
    """
    Read prompt from txt file
    :param path: filename
    :return: prompt
    """
    base_dir = Path(__file__).parent
    full_path = base_dir / path
    with open(full_path, "r") as f:
        return f.read().strip()


def get_sql_query_prompt():
    return read_prompt(SQL_QUERY_PROMPT_PATH)


def get_explanation_prompt():
    return read_prompt(EXPLANATION_PROMPT_PATH)


def get_correctness_prompt():
    return read_prompt(CHECK_CORRECTNESS_PROMPT_PATH)

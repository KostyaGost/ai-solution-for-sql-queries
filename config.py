import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
DATA_PATH = "data/Data Dump - Accrual Accounts.xlsx"

VALID_KEYWORDS = {
    "count", "empty", "unique", "average", "mean", "min", "minimum", "max", "maximum", "outlier",
    "missing", "field", "column", "duplicate", "distinct", "null", "non-null", "total", "sum",
    "variance", "standard deviation", "median", "mode", "row", "dataset", "record",
    "value", "profile", "statistics", "distribution", "range", "data quality", "zero",
    "list", "show", "how many", "percentage", "proportion", "most", "least", "top", "bottom"
}

SQL_QUERY_PROMPT_PATH = "prompts/sql_query_system_prompt.txt"
EXPLANATION_PROMPT_PATH = "prompts/explanation_system_prompt.txt"
CHECK_CORRECTNESS_PROMPT_PATH = "prompts/check_correctness_system_prompt.txt"

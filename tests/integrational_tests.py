import unittest
from client_api_request import ClientAPIRequest

SCHEMA_DESCRIPTION = """Table name: data
Columns:
- Authorization Group (int64)
- Bus. Transac. Type (str)
- Calculate Tax (str)
- Cash Flow-Relevant Doc. (bool)
- Cleared Item (str)
- Clearing Date (datetime64[us])
- Clearing Entry Date (datetime64[us])
- Clearing Fiscal Year (float64)
- Country Key (str)
- Currency (str)
- Debit/Credit ind (str)
- Transaction Value (float64)
- Document Is Back-Posted (str)
- Exchange rate (float64)
- Fiscal Year.1 (float64)
- Fiscal Year.2 (int64)
- Posting period.1 (int64)
- Ref. Doc. Line Item (int64)"""


class TestClientAPIRequestIntegration(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client = ClientAPIRequest()

    def test_is_valid_input_accepts_print_rows(self):
        result = self.client.is_valid_input("print first row", SCHEMA_DESCRIPTION)
        assert result is True

    def test_is_valid_input_accepts_count_null_values(self):
        result = self.client.is_valid_input("Count null values in Authorization Group", SCHEMA_DESCRIPTION)
        assert result is True

    def test_is_valid_input_accepts_find_average_value(self):
        result = self.client.is_valid_input("Find average value in column Ref. Doc. Line Item", SCHEMA_DESCRIPTION)
        assert result is True

    def test_is_valid_input_rejects_create_model(self):
        result = self.client.is_valid_input("Create a machine learning model", SCHEMA_DESCRIPTION)
        assert result is False

    def test_is_valid_input_rejects_create_graph(self):
        result = self.client.is_valid_input("Create graph", SCHEMA_DESCRIPTION)
        assert result is False

    def test_is_valid_input_rejects_print_max_cars_number_in_city(self):
        result = self.client.is_valid_input("Print max number of cars in city", SCHEMA_DESCRIPTION)
        assert result is False

    def test_generate_sql_query_produces_valid_sql(self):
        sql = self.client.generate_sql_query("Show all records", SCHEMA_DESCRIPTION)
        assert "SELECT" in sql.upper()
        assert "data" in sql

    def test_generate_explanation_returns_text(self):
        explanation = self.client.generate_explanation(
            "Count records",
            "SELECT COUNT(*) AS row_count FROM data;",
            """
                |   row_count |
                |------------:|
                |       13152 |
                """
        )
        assert isinstance(explanation, str)
        assert len(explanation) > 10


if __name__ == '__main__':
    unittest.main()
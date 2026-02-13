import pandas as pd
from config import DATA_PATH
import duckdb

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 0)
pd.set_option('expand_frame_repr', False)


class DataManager:
    def __init__(self):
        self.data_df = self.load_data_to_dataframe()
        self.db_connection = duckdb.connect()
        self.db_connection.register('data', self.data_df)

    def load_data_to_dataframe(self) -> pd.DataFrame:
        """
        Load data to dataframe
        :return: pandas dataframe
        """
        return pd.read_excel(DATA_PATH, index_col=0)

    def make_sql_query(self, sql_query: str) -> pd.DataFrame:
        """
        Execute SQL query
        :param sql_query: SQL query
        :return: None
        """
        try:
            result = self.db_connection.execute(sql_query).fetchdf()
            return result
        except Exception as e:
            raise RuntimeError(f"SQL execution error: {e}")

    def build_schema_description(self) -> str:
        """
        Create schema description
        :return: schema description
        """
        lines = []
        lines.append("Table name: data")
        lines.append("Columns:")
        for col in self.data_df.columns:
            lines.append(f"- {col} ({str(self.data_df[col].dtype)})")
        return "".join(lines)

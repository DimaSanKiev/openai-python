from sqlalchemy import create_engine
from sqlalchemy import text


def dataframe_to_database(df, table_name):
    """
    Convert a pandas dataframe to a database.
    :param df: pd.DataFrame to be converted to a database
    :param table_name: Name of the table within the database
    :return: engine: SQLAlchemy engine object
    """
    engine = create_engine(f'sqlite:///:memory:', echo=False)
    df.to_sql(name=table_name, con=engine, index=False)
    return engine


def handle_response(response):
    """Handles the response from OpenAI.
    :param response: Response JSON from OpenAI
    :return: Proposed SQL query
    """
    query = response["choices"][0]["text"]
    if query.startswith(" "):
        query = "SELECT" + query
    return query


def execute_query(engine, query):
    """
    Execute a query on a database.
    :param engine: Database engine (SQLAlchemy engine object)
    :param query: SQL query (string)
    :return: List of tuples containing the result of the query
    """
    with engine.connect() as conn:
        result = conn.execute(text(query))
        return result.fetchall()

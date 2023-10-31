def check_for_duplicate_links(path_to_new_content, links):
    """
    
Checks if any of the links in the given list of links are duplicates of the given path to new content.

Parameters:
    path_to_new_content (pathlib.Path): The path to the new content to check for duplicates of.
    links (list): A list of links to check for duplicates of the given path to new content.

Returns:
    bool: True if any of the links are duplicates of the given path to new content, False otherwise.

    """
    urls = [str(link.get("href")) for link in links]
    content_path = str(Path(*path_to_new_content.parts[-2:]))
    return content_path in urls


def dataframe_to_database(df, table_name):
    """
    
Converts a Pandas DataFrame to a SQLite database table.

Parameters:
    df (DataFrame): The Pandas DataFrame to be converted.
    table_name (str): The name of the table to be created in the database.

Returns:
    engine (Engine): A SQLAlchemy engine object connected to the in-memory SQLite database.

Example:
    df = pd.DataFrame({'col1': [1, 2, 3], 'col2': ['a', 'b', 'c']})
    engine = dataframe_to_database(df, 'my_table')
    # Use the engine to query the database
    result = engine.execute('SELECT * FROM my_table').fetchall()
    print(result)
    # Output: [(1, 'a'), (2, 'b'), (3, 'c')]

    """
    engine = create_engine(f'sqlite:///:memory:', echo=False)
    df.to_sql(name=table_name, con=engine, index=False)
    return engine


def execute_query(engine, query):
    """
    
This function executes a SQL query on a given database engine and returns the results as a list of tuples. The function takes in two parameters: the database engine and the SQL query. The database engine is used to establish a connection to the database, and the SQL query is used to retrieve data from the database. The function uses the SQLAlchemy library to execute the query and return the results. The returned results are in the form of a list of tuples, with each tuple representing a row of data from the database. If the query is successful, the function returns the results. If there is an error in executing the query, the function will raise an exception. 
    """
    with engine.connect() as conn:
        result = conn.execute(text(query))
        return result.fetchall()


def grade(correct_answer_dict, answers):
    """
    This function takes two dictionaries as arguments, one with the correct answers and one with the answers given by the student. It then compares the answers and calculates the percentage of correct answers. If the percentage is below 60, the student has not passed the test, otherwise they have passed. The function returns a string with the number of correct answers, the total number of questions, the percentage achieved, and whether the student has passed or not.
    """
    correct_answers = 0
    for question, answer in answers.items():
        if answer.upper() == correct_answer_dict[question].upper()[16]:
            correct_answers += 1
    grade = 100 * correct_answers / len(answers)

    if grade < 60:
        passed = "Not passed!"
    else:
        passed = "Passed!"
    return f"{correct_answers} out of {len(answers)} correct! You achieved: {grade} % : {passed}"


def handle_response(response):
    """
    
This function takes in a response from the API and extracts the query from it. It first checks if the query starts with a space, and if it does, it adds "SELECT" to the beginning of the query. The function then returns the extracted query.
    """
    query = response["choices"][0]["text"]
    if query.startswith(" "):
        query = "SELECT" + query
    return query

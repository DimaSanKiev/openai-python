import openai


def create_table_definition_prompt(df, table_name):
    """
    Create a prompt for the OpenAI API to generate SQL queries.
    :param df: pd.DataFrame object to automatically extract the table columns
    :param table_name: Name of the table within the database
    :return: String containing the prompt for OpenAI
    """

    prompt = '''### SQLite table, with its properties:
#
# {}({})
#
'''.format(table_name, ",".join(str(x) for x in df.columns))

    return prompt


def user_query_input():
    """
    Ask the user what they want to know about the data.
    :return: User input, string
    """
    user_input = input("Tell OpenAI what you want to know about the data: ")
    return user_input


def combine_prompts(fixed_sql_prompt, user_query):
    """
    Combine the fixed SQL prompt with the user query.
    :param fixed_sql_prompt: Fixed SQL prompt, string
    :param user_query: User query, string
    :return: Combined prompt
    """
    final_user_input = f"### A query to answer: {user_query}\nSELECT"
    return fixed_sql_prompt + final_user_input


def send_to_openai(prompt):
    """
    Send the prompt to OpenAI.
    :param prompt: Prompt to send to OpenAI, string
    :return: Response from OpenAI
    """
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=prompt,
        temperature=0,
        max_tokens=150,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["#", ";"]
    )
    return response

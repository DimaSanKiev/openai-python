# Dataset based on https://www.kaggle.com/datasets/kyanyoga/sample-sales-data

import logging

import openai
import pandas as pd

import db_utils
import openai_utils

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
openai.api_key_path = "../secret/openai_api_key.txt"

if __name__ == "__main__":
    logging.info("Loading data...")
    df = pd.read_csv("resources/sales_data_sample.csv", encoding="ISO-8859-1")
    logging.info(f"Data format: {df.shape}")

    logging.info("Converting to database...")
    database = db_utils.dataframe_to_database(df, "Sales")

    fixed_sql_prompt = openai_utils.create_table_definition_prompt(df, "Sales")
    logging.info(f"Fixed SQL prompt: {fixed_sql_prompt}")

    logging.info("Waiting for user input...")
    user_input = openai_utils.user_query_input()
    final_prompt = openai_utils.combine_prompts(fixed_sql_prompt, user_input)
    logging.info(f"Final prompt: {final_prompt}")

    logging.info("Sending to OpenAI...")
    response = openai_utils.send_to_openai(final_prompt)
    proposed_query = response["choices"][0]["text"]
    proposed_query_postprocessed = db_utils.handle_response(response)
    logging.info(f"Response obtained. Proposed SQL query:\n{proposed_query_postprocessed}\n")
    result = db_utils.execute_query(database, proposed_query_postprocessed)
    logging.info(f"Result: {result}")
    print(result)

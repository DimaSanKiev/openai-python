import inspect
from pathlib import Path
import openai
import functions

openai.api_key_path = "../secret/openai_api_key.txt"


def docstring_prompt(code):
    prompt = f"{code}\n# A high-quality Python docstring of the above Python function:\n\"\"\""
    return prompt


def merge_docstring_and_function(function_string, docstring):
    split = function_string.split("\n")
    first_part, second_part = split[0], split[1:]
    merged_function = first_part + "\n    \"\"\"\n    " + docstring + "\n    \"\"\"\n" + "\n".join(second_part)
    return merged_function


def get_all_functions(module):
    return [mem for mem in inspect.getmembers(module, inspect.isfunction)
            if mem[1].__module__ == module.__name__]


def get_openai_completion(prompt):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=prompt,
        temperature=0,
        max_tokens=256,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\"\"\""]  # Corresponds to """, the end of the docstring
    )
    return response["choices"][0]["text"]


if __name__ == '__main__':
    functions_to_prompt = functions
    all_funcs = get_all_functions(functions)

    functions_with_prompts = []
    for func in all_funcs:
        code = inspect.getsource(func[1])
        prompt = docstring_prompt(code)
        response = get_openai_completion(prompt)

        merged_code = merge_docstring_and_function(code, response)
        functions_with_prompts.append(merged_code)

    functions_to_prompt_name = Path(functions_to_prompt.__file__).stem
    with open(f"{functions_to_prompt_name}_withdocstring.py", "w") as f:
        f.write("\n\n".join(functions_with_prompts))

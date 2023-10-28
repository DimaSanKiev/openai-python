import openai

# Load your API key from a file
with open('../secret/openai_api_key.txt', 'r') as file:
    api_key = file.read().strip()

# Initialize the OpenAI API client
openai.api_key = api_key

# Your prompt for generating text
prompt = "improve my comment: I hate you"

# Call the API to generate text
response = openai.Moderation.create(
    input=prompt
)

# Get the generated text from the response
output = response['results'][0]

# Print the generated text
print("Generated text:")
print(output)

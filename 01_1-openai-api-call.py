import openai

# Load your API key from a file
with open('resources/openai_api_key.txt', 'r') as file:
    api_key = file.read().strip()

# Initialize the OpenAI API client
openai.api_key = api_key

# Your prompt for generating text
prompt = "Translate the following English text to French: 'Hello, how are you?'"

# Call the API to generate text
response = openai.Completion.create(
    engine="text-davinci-002",  # You can choose a different engine if needed
    prompt=prompt,
    max_tokens=50,  # Adjust the desired length of the generated text
)

# Get the generated text from the response
generated_text = response.choices[0].text

# Print the generated text
print("Generated text:")
print(generated_text)

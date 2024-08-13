import openai

# Set your OpenAI API key
api_key = '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'
openai.api_key = api_key

# Function to generate response
def generate_response(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=100
    )
    return response['choices'][0]['text'].strip()

# Example prompt
prompt = "What is the meaning of car?"

# Generate response
response = generate_response(prompt)

# Print response
print("Generated Response:")
print(response)

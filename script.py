# Import openai
import openai

# Set your API key
openai.api_key = "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"

# Create a request to the Completion endpoint
response = openai.completions.create(
  # Specify the correct model
  model="gpt-3.5-turbo-instruct",
  prompt="can you give me some tips to understand soccer strategies?",
  max_tokens=1000
)

print(response)
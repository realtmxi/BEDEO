from openai import AzureOpenAI
import os


# api_key = os.getenv("OAI_KEY")
# api_endpoint = os.getenv("OAI_ENDPOINT")
# client = AzureOpenAI(
#   azure_endpoint = api_endpoint, 
#   api_key=api_key,
#   api_version="2024-12-01-preview"
# )

# response = client.chat.completions.create(
#     model="o4-mini", # replace with the model deployment name of your o1-preview, or o1-mini model
#     messages=[
#         {"role": "user", "content": "What steps should I think about when writing my first Python API?"},
#     ],
#     max_completion_tokens = 5000
# )
api_key = os.getenv("OAI_KEY")
api_endpoint = os.getenv("OAI_ENDPOINT")
client = AzureOpenAI(
  azure_endpoint = api_endpoint, 
  api_key=api_key,
  api_version="2025-04-14"
)

response = client.chat.completions.create(
    model="o4-mini", # replace with the model deployment name of your o1-preview, or o1-mini model
    messages=[
        {"role": "user", "content": "What steps should I think about when writing my first Python API?"},
    ],
    max_completion_tokens = 5000
)

print(response.model_dump_json(indent=2))
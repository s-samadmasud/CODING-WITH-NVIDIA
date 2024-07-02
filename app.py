from openai import OpenAI

client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  # place your nvidia api key
  api_key = "NVIDIA_API_KEY" 
)

completion = client.chat.completions.create(
  model="mistralai/codestral-22b-instruct-v0.1",
  messages=[{"role":"user","content":"Write a function to traverse graph in a Breadth First Search way."}],
  temperature=0.5,
  top_p=1,
  max_tokens=1024,
  stream=True
)

for chunk in completion:
  if chunk.choices[0].delta.content is not None:
    print(chunk.choices[0].delta.content, end="")


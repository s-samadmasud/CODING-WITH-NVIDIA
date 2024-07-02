from openai import OpenAI

client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = "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"
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


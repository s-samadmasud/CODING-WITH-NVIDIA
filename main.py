import streamlit as st
from openai import OpenAI

# place your nvidia api key
api_key = "NVIDIA_API_KEY"  

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=api_key
)

def generate_response(question):
  completion = client.chat.completions.create(
      model="meta/llama3-70b-instruct",
      messages=[{"role": "user", "content": question}],
      temperature=0.5,
      top_p=1,
      max_tokens=1024,
      stream=True
  )
  response = ""
  for chunk in completion:
    if chunk.choices[0].delta.content is not None:
      response += chunk.choices[0].delta.content
  return response

st.title("YOUR CODING ASSISTANT!")

# Text input for user question
user_question = st.text_input("Enter your question here:")

# Button to trigger response generation
if st.button("Ask"):
  if user_question:
    # Generate response using OpenAI API
    response = generate_response(user_question)
    st.write(f"**Response:** {response}")
  else:
    st.warning("Please enter a question.")


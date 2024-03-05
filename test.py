from flask import Flask, jsonify, request
from openai import OpenAI
import os


#How to set environment variables in Windows in PS:
#Make sure to run the following command in the SAME terminal before running the app:
# $env:OPENAI_API_KEY="xyzs"
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "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"))
app = Flask(__name__)

completion = client.chat.completions.create(
  model="gpt-4-turbo-preview",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ]
)

print(completion.choices[0].message)

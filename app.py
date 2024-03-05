from flask import Flask, jsonify, request
from openai import OpenAI
import os


#How to set environment variables in Windows in PS:
#Make sure to run the following command in the SAME terminal before running the app:
# $env:OPENAI_API_KEY="xyzs"
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
app = Flask(__name__)



@app.route('/message', methods=['POST'])
def post_message():
    post_request = request.json
    message = post_request['message']
    # Generate a completion using the OpenAI client
    completion = client.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message}  # Use the message from the request
        ]
    )
    
    # Extract the message from the completion
    response = completion.choices[0].message
    print(response.content)
    
    
    # Return the message as JSON
    return response.content

@app.route('/test', methods=['GET'])
def chat_completion():
   
    # Return the chat completion object as a JSON response
    return jsonify('hello')


if __name__ == '__main__':
    app.run(debug=True)

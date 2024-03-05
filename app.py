from flask import Flask, jsonify, request
from openai import OpenAI
import os


#How to set environment variables in Windows in PS:
#Make sure to run the following command in the SAME terminal before running the app:
# $env:OPENAI_API_KEY="xyzs"
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "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"))
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
    # Simulated chat completion object as per OpenAI documentation
    chat_completion_object = {
        "id": "cmpl-2tcvF6Bxf0DZ2V5F8Z2uT2FjV",
        "object": "chat.completion",
        "created": 1589478378,
        "model": "gpt-3.5-turbo",
        "choices": [{
            "message": {
                "role": "system",
                "content": "You are a helpful assistant."
            }
        }, {
            "message": {
                "role": "user",
                "content": "Who won the world series in 2020?"
            }
        }, {
            "index": 0,
            "finish_reason": "length",
            "message": {
                "role": "assistant",
                "content": "The Los Angeles Dodgers won the World Series in 2020."
            }
        }],
        "usage": {
            "total_tokens": 15
        }
    }

    # Return the chat completion object as a JSON response
    return jsonify(chat_completion_object)


if __name__ == '__main__':
    app.run(debug=True)

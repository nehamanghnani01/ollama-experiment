#example of using the generate REST API provided by ollama to use the model to generate response locally for a prompt

import requests
import json

url = 'http://localhost:11434/api/generate'

payload = {
    "model": "llama3.2", 
    "prompt": "what is the GDP of the United States?"
}

response = requests.post(url, json=payload, stream= True)

if response.status_code == 200:
    print("Generated Text = ", end = "", flush=True)
    for line in response.iter_lines():
        
        if line:
            decoded = line.decode('utf-8')
            response_json = json.loads(decoded)
            generated_text = response_json.get("response", "")
            print(generated_text, end="", flush=True)
else:
    print("ERROR!")
    print(response.status_code)
    print(response.text)


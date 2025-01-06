import ollama

#.chat() function in ollama
response = ollama.chat(
    model = "llama3.2", 
    messages= [
        {"role": "user", "content": "why is the ocean blue?"}
    ], 
    stream= True
)

# if stream is equal to True, the response has to be iterated over chunks
for chunk in response:
    print(chunk["message"]["content"], end="", flush=True)  


#.generate() function in ollama
response = ollama.generate(
    model="llama3.2",
    prompt="what is the GDP of the United States?",
)   

# print(response["response"])
for chunk in response:
    print(chunk["message"]["content"], end="", flush=True)


#show 
ollama.show("llama3.2")

modelfile = """
FROM llama3.2
SYSTEM You are a smart assists  that can answer questions and generate text based on the input you receive. Andswer succintly and with less verbose, to the point
PARAMETER temperature 0.1
"""

ollama.create(model="temp_llama", modelfile=modelfile)

response = ollama.chat(
    model = "temp_llama", 
    messages= [
        {"role": "user", "content": "why is the ocean salty?"}
    ], 
    stream= True
)

# if stream is equal to True, the response has to be iterated over chunks
for chunk in response:
    print(chunk["message"]["content"], end="", flush=True)  

ollama.delete("temp_llama")



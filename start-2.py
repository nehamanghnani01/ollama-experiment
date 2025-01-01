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

print(response["response"])
# for chunk in response:
#     print(chunk["message"]["content"], end="", flush=True)


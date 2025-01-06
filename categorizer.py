import ollama
import os 

model ="llama3.2"

# Paths to input and output files
input_file = "./data/grocery_list.txt"
output_file = "./data/categorized_grocery_list.txt"

with open(input_file, "r") as f:
    grocery_list = f.read().strip()


prompt =  f"""
You are an assistant that categorizes and sorts grocery items.

Here is a list of grocery items:

{grocery_list}

Please:

1. Categorize these items into appropriate categories such as Produce, Dairy, Meat, Bakery, Beverages, etc.
2. Sort the items alphabetically within each category.
3. Present the categorized list in a clear and organized manner, using bullet points or numbering.

"""

try:
    response = ollama.generate(model=model, prompt=prompt)
    generated_text = response.get("response", "")
    print("==== Categorized List: ===== \n")
    print(generated_text)

    # Write the categorized list to the output file
    with open(output_file, "w") as f:
        f.write(generated_text.strip())

    print(f"Categorized grocery list has been saved to '{output_file}'.")
except Exception as e:
    print("An error occurred:", str(e))


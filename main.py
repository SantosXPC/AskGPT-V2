"""
Author: Santos Martínez (Initial idea founded at Replit)
Date: 07/04/2023
Description: This Python script interacts with the OpenAI GPT-3 language model to create a conversation. It starts with an initial user prompt, generates responses, and continues the conversation. The conversation is limited to 10 responses.

Usage: Run the script and provide an initial question. The script will engage in a conversation
       by generating responses using the OpenAI GPT-3 model.

License: GNU General Public License (GPL)

"""

import os
import openai

# Set the OpenAI API key
my_secret = os.environ['openai']
openai.api_key = my_secret

def askGPT(prompt, conversation_length):
    if conversation_length == 0:
        prompt = f"{prompt.strip()}?"
        print("\nPregunta", conversation_length, ":", prompt)
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.7,
        )
        return response.choices[0].text.strip()
    else:
        # Generate a new question based on the previous response
        new_prompt = f"Elabora una pregunta compleja a partir de la respuesta: {prompt.strip()}"
        new_question = openai.Completion.create(
            engine="text-davinci-002",
            prompt=new_prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.7,
        )
        new_question = new_question.choices[0].text.strip()
        print("\nPregunta", conversation_length, ":", new_question)
        new_prompt = f"{new_question.strip()}"
        new_response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=new_prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.7,
        )
        return new_response.choices[0].text.strip()

def main():
    conversation_length = 0  # Initialize the conversation length counter
    prompt = input("Cuál es tu pregunta? ")
    initial_prompt = prompt  # Save the initial question
    response = askGPT(prompt, conversation_length)
    print("Respuesta:", response)
    new_prompt = f"{response.strip()}"
    while conversation_length < 10:  # Define a limit of 10 responses
        conversation_length += 1
        new_response = askGPT(new_prompt, conversation_length)
        print("Respuesta:", new_response)
        new_prompt = f"{new_response.strip()}"

if __name__ == "__main__":
    main()
#!/usr/bin/python3
import openai
import os

openai.api_key = "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"


def get_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    message = response.choices[0].text.strip()
    return message


while True:
    user_input = input("You: ")
    prompt = f"Me: {user_input.strip()} \nYou:"
    response = get_response(prompt)
    print(response)

#!/usr/bin/python3

import openai

openai.api_key = "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"

conversation = ""

i = 1
while (i != 0):
    question = input("Chris: ")
    conversation += "Chris: " + question + "Eva: "
    response = openai.Completion.create(
        engine="davinci",
        prompt=conversation,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=["\n", " Chris:", " Eva:"]
    )
    answer = response.choices[0].text.strip()
    conversation += answer + "\n"
    print("Eva: " + answer + "\n")

import os
from openai import AzureOpenAI
subscription_key = os.getenv("OpenAIAPIKey")

def try_openai():

    endpoint = "https://openai-fortesting.openai.azure.com/"
    deployment = "gpt-4o-mini"

    api_version = "2024-12-01-preview"

    client = AzureOpenAI(
        api_version=api_version,
        azure_endpoint=endpoint,
        api_key=subscription_key,
    )

    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant.",
            },
            {
                "role": "user",
                "content": "I am going to Paris, what should I see?",
            }
        ],
        max_tokens=4096,
        temperature=1.0,
        top_p=1.0,
        model=deployment
    )

    return response.choices[0].message.content
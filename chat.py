import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["PINENEXUS_API_KEY"],
    base_url="https://apinexusdev.com/v1",
)

resp = client.chat.completions.create(
    model="deepseek-v4-flash",
    messages=[{"role": "user", "content": "Say hello in one sentence."}],
)

print(resp.choices[0].message.content)

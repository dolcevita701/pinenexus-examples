# PineNexus minimal examples

Minimal examples for calling PineNexus with an OpenAI-compatible API.

- Site: https://apinexusdev.com/
- Docs: https://docs.apinexusdev.com/
- Models and pricing: https://apinexusdev.com/pricing

## Setup

1. Sign in at the site with Google or GitHub. A Chinese phone number is not required.
2. New accounts receive a $1 trial credit.
3. Create an API key in Tokens.
4. Put the key in the `PINENEXUS_API_KEY` environment variable. Do not commit it.

## Endpoints

- OpenAI SDK, Cursor, LangChain: `https://apinexusdev.com/v1`
- Cherry Studio API Host: `https://apinexusdev.com` (do not add `/v1`)

## curl

```bash
curl https://apinexusdev.com/v1/chat/completions \
  -H "Authorization: Bearer $PINENEXUS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "deepseek-v4-flash",
    "messages": [{"role": "user", "content": "Say hello in one sentence."}]
  }'
```

## Python

Install first: `pip install openai`

```python
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
```

Replace `deepseek-v4-flash` with another exact ID from the model catalog. Request formats for image, embeddings, and rerank are in the docs.

## Note

These examples only help you get the first request working. Use the live catalog for the models that are actually available.

## Tutorials

- [Change one URL and one API key to point your existing OpenAI calls at Chinese models](https://dev.to/lumi_nexus/change-one-url-and-one-api-key-to-point-your-existing-openai-calls-at-chinese-models-3m4f)
- [Connect DeepSeek, Qwen, Kimi, and GLM in Cursor and Cherry Studio](https://dev.to/lumi_nexus/connect-deepseek-qwen-kimi-and-glm-in-cursor-and-cherry-studio-noe)

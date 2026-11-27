curl https://apinexusdev.com/v1/chat/completions \
  -H "Authorization: Bearer $PINENEXUS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "deepseek-v4-flash",
    "messages": [{"role": "user", "content": "Say hello in one sentence."}]
  }'

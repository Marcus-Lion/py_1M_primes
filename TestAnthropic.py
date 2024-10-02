from anthropic import AnthropicVertex

LOCATION="us-east5" # or "us-east5"

client = AnthropicVertex(region=LOCATION, project_id="marcus-lion-web")

message = client.messages.create(
  max_tokens=1024,
  messages=[
    {
      "role": "user",
      "content": "Send me a recipe for banana bread.",
    }
  ],
  model="claude-3-5-sonnet@20240620",
)
print(message.model_dump_json(indent=2))
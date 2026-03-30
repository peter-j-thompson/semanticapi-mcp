# Semantic API MCP Server

<!-- mcp-name: io.github.peter-j-thompson/semanticapi -->

An [MCP (Model Context Protocol)](https://modelcontextprotocol.io) server that lets Claude, ChatGPT, and other LLM agents search and discover APIs using natural language via [Semantic API](https://semanticapi.dev). Ask for any API capability in plain English and get back endpoint details, parameters, auth info, and code snippets.

## Install

```bash
pip install semanticapi-mcp
```

Or run directly with uvx:

```bash
uvx semanticapi-mcp
```

## Configuration

### Get an API Key

Sign up at [semanticapi.dev](https://semanticapi.dev) to get your API key.

### Environment Variables

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `SEMANTIC_API_KEY` | Yes | — | Your Semantic API key |
| `SEMANTIC_API_URL` | No | `https://semanticapi.dev` | API base URL override |

### Claude Desktop

Add to your Claude Desktop config (`~/Library/Application Support/Claude/claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "semanticapi": {
      "command": "uvx",
      "args": ["semanticapi-mcp"],
      "env": {
        "SEMANTIC_API_KEY": "your-api-key-here"
      }
    }
  }
}
```

Or if installed with pip:

```json
{
  "mcpServers": {
    "semanticapi": {
      "command": "semanticapi-mcp",
      "env": {
        "SEMANTIC_API_KEY": "your-api-key-here"
      }
    }
  }
}
```

## Tools

### `semantic_query`

Search for an API capability using natural language.

**Inputs:**
- `query` (string, required) — What you want to do, e.g. "send an email with Gmail"
- `auto_discover` (boolean, optional, default: true) — Auto-discover new APIs if needed

**Example:** "Find me an API to convert currencies in real-time"

### `semantic_discover`

Deep discovery of a specific provider/API by name and intent.

**Inputs:**
- `provider_name` (string, required) — API provider name, e.g. "stripe", "twilio"
- `user_intent` (string, optional) — What you want to do with this API

**Example:** Discover Stripe's capabilities for "process a refund"

### `semantic_discover_url`

Analyze any API from its documentation URL.

**Inputs:**
- `url` (string, required) — URL of the API documentation
- `user_intent` (string, optional) — What you want to do with this API

**Example:** Analyze `https://docs.example.com/api` to generate a provider config

## Related

- **[Semantic API](https://semanticapi.dev)** — The hosted API service
- **[semanticapi-engine](https://github.com/peter-j-thompson/semanticapi-engine)** — Open source engine (AGPL-3.0)
- **[semantic-api-skill](https://github.com/peter-j-thompson/semantic-api-skill)** — Agent framework skill package
- **[CLI Tool](https://github.com/peter-j-thompson/semanticapi-cli)** — Command-line interface (`pip install semanticapi-cli`)

<!-- mcp-name: io.github.peter-j-thompson/semanticapi -->

## License

MIT

## Hosted deployment

A hosted deployment is available on [Fronteir AI](https://fronteir.ai/mcp/peter-j-thompson-semanticapi-mcp).


"""Semantic API MCP Server."""

import json
import os

import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Semantic API")

BASE_URL = os.environ.get("SEMANTIC_API_URL", "https://semanticapi.dev")


def _get_api_key() -> str:
    key = os.environ.get("SEMANTIC_API_KEY", "")
    if not key:
        raise ValueError(
            "SEMANTIC_API_KEY environment variable is required. "
            "Get your API key at https://semanticapi.dev"
        )
    return key


def _headers() -> dict[str, str]:
    return {
        "X-API-Key": _get_api_key(),
        "Content-Type": "application/json",
    }


async def _post(path: str, payload: dict) -> str:
    """Make a POST request and return formatted JSON response."""
    async with httpx.AsyncClient(timeout=30) as client:
        resp = await client.post(f"{BASE_URL}{path}", json=payload, headers=_headers())
        resp.raise_for_status()
        return json.dumps(resp.json(), indent=2)


@mcp.tool()
async def semantic_query(query: str, auto_discover: bool = True) -> str:
    """Search for an API capability using natural language.

    Returns endpoint details, parameters, auth info, and code snippets.

    Args:
        query: Natural language description of what you want to do (e.g. "send an email with Gmail")
        auto_discover: Whether to automatically discover new APIs if no cached result exists
    """
    try:
        return await _post("/api/query", {"query": query, "auto_discover": auto_discover})
    except ValueError as e:
        return str(e)
    except httpx.HTTPStatusError as e:
        return f"API error {e.response.status_code}: {e.response.text}"
    except Exception as e:
        return f"Error: {e}"


@mcp.tool()
async def semantic_discover(provider_name: str, user_intent: str | None = None) -> str:
    """Deep discovery of a specific provider/API by name and intent.

    Args:
        provider_name: Name of the API provider (e.g. "stripe", "twilio", "github")
        user_intent: Optional description of what you want to do with this API
    """
    try:
        payload: dict = {"provider_name": provider_name}
        if user_intent:
            payload["user_intent"] = user_intent
        return await _post("/api/discover/search", payload)
    except ValueError as e:
        return str(e)
    except httpx.HTTPStatusError as e:
        return f"API error {e.response.status_code}: {e.response.text}"
    except Exception as e:
        return f"Error: {e}"


@mcp.tool()
async def semantic_discover_url(url: str, user_intent: str | None = None) -> str:
    """Analyze any API from its documentation URL. Generates a full provider config.

    Args:
        url: URL of the API documentation to analyze
        user_intent: Optional description of what you want to do with this API
    """
    try:
        payload: dict = {"url": url}
        if user_intent:
            payload["user_intent"] = user_intent
        return await _post("/api/discover/from-url", payload)
    except ValueError as e:
        return str(e)
    except httpx.HTTPStatusError as e:
        return f"API error {e.response.status_code}: {e.response.text}"
    except Exception as e:
        return f"Error: {e}"


def main():
    """Run the MCP server with stdio transport."""
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()

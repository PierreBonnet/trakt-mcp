import asyncio
import sys
from pathlib import Path

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


def test_stdio_discovery_from_another_directory_without_real_credentials(tmp_path):
    async def scenario():
        parameters = StdioServerParameters(
            command=sys.executable,
            args=[str(Path(__file__).resolve().parents[1] / "server.py")],
            cwd=str(tmp_path),
            env={
                "TRAKT_CLIENT_ID": "fixture-client",
                "TRAKT_AUTH_TOKEN_PATH": str(tmp_path / "absent.json"),
            },
        )
        async with (
            stdio_client(parameters) as (read, write),
            ClientSession(read, write) as client,
        ):
            initialized = await client.initialize()
            assert "confirmation" in initialized.instructions
            tools = await client.list_tools()
            assert any(tool.name == "check_auth_status" for tool in tools.tools)
            result = await client.call_tool("check_auth_status", {})
            assert not result.isError

    asyncio.run(asyncio.wait_for(scenario(), timeout=20))

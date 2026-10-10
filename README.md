# trakt-mcp

Community derivative of [wwiens/trakt_mcpserver](https://github.com/wwiens/trakt_mcpserver), prepared for public source distribution. The upstream MIT license and required attribution are retained. This repository starts with a fresh Git history.

## Install and run

Requires Python 3.12 or later. The test suite also requires Node.js 22 or later for the pinned MCP Inspector.

```sh
python -m venv .venv
# Activate .venv using the command appropriate to your shell.
python -m pip install -e .
python -m pip install -r requirements-dev.txt
npm ci --ignore-scripts
python -m pytest
trakt-mcp
```

Set `TRAKT_CLIENT_ID` and `TRAKT_CLIENT_SECRET` locally using your own Trakt application credentials. Configure your MCP client to launch the installed `trakt-mcp` executable over stdio. OAuth tokens default to `~/.trakt-mcp/auth_token.json`; `TRAKT_AUTH_TOKEN_PATH` can override this local storage path.

## Privacy

No account configuration, OAuth sessions, personal exports, or local Git history are distributed. Examples and tests use fixtures. Never commit your local credentials or session files. Runtime tools can return information from the account you connect; review outputs before sharing them.

## Changes in this derivative

Structured log fields recursively redact common credential keys without mutating the original request data. Regression tests cover nested headers and token fields.

Only GitHub source distribution is configured; this derivative is not published to npm or PyPI.

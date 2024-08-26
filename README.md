🚨 This project is currently under heavy refactoring.


# PlebChat documentation

Welcome to PlebChat's documentation! 👋🏻

This project is an open-source, solution for a self-hosted "agentic" AI application.


## Architecture / System Diagram

```mermaid
graph TD
    A[Open WebUI - Docker]
    B[Pipelines - Python Server]
    Cl[`cloudflared`]
    D[PlebChat Graph - Python Server]

    A -->|Web request| B
    Cl -->|NAT address translation| A
    B -->|user query| D
    D -->|verify user status| G[PlebChat DB - Python Server]
    G -->|user balance| D
    G -->|query database| H[MongoDB Server Replica Mode]
    I[Admin Panel] -->|monitors| G
    D -->|LLM completion| J[Ollama Server]
```

## Open WebUI

See [website](https://openwebui.com), [repository](https://github.com/open-webui/open-webui), [documentation](https://docs.openwebui.com) and [Setup instructions](./setup_oi.md)

This is an open-source repository used as the "frontend."

## pipeline

See [repository](https://github.com/PlebeiusGaragicus/PlebChatPipe) and [Setup instructions](./setup_pipeline.md)

Think of Open WebUI pipelines as extensions.  This repository stands up an OpenAI-compatible API that is used to invoke our LangGraph server.

## LangGraph agent

See [repository](https://github.com/PlebeiusGaragicus/PlebChatGraph) and [Setup instructions](./setup_langgraph.md)

This is our LangGraph agent.

## User database

See [respository]() and [Setup instructions](./setup_db)

## Cloudflare Tunnel

See [Setup instructions](./setup_cloudflare.md)
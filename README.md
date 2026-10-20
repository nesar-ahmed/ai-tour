# AI Tour

A small personal practice project for learning **applied AI engineering** — what the job of an
AI engineer actually looks like in 2026, built by hand instead of read about.

This is a study project, not a product. The goal is to touch every layer of the modern AI
application stack and understand how the pieces fit together: serving a model, prompting it
well, giving it tools, retrieving context, evaluating output quality, and shipping the whole
thing behind a real API.

## Current state

Right now the repo is a bare skeleton — a FastAPI app with one health-check style route.
Everything below that is what I'm building toward.

```
GET /  ->  {"message": "Hello world!"}
```

## Stack

| | |
|---|---|
| Language | Python 3.12 |
| Framework | FastAPI (`fastapi[standard]`) |
| Package manager | [uv](https://docs.astral.sh/uv/) |
| Version pin | `.python-version` |

## Getting started

```bash
uv sync                      # install dependencies into .venv
uv run fastapi dev           # dev server with reload on http://127.0.0.1:8000
```

Interactive API docs are served automatically at http://127.0.0.1:8000/docs.

To build a production-style run instead of a dev one:

```bash
uv run fastapi run dev
```

## Layout

```
ai-tour/
├── pyproject.toml      # project metadata + dependencies, fastapi entrypoint config
├── .python-version     # pinned interpreter (3.12)
├── uv.lock             # resolved dependency lockfile
└── src/
    └── main.py         # the FastAPI app
```

## What "AI engineer in 2026" means to me

The role is less about training models and more about the surrounding system — the plumbing,
the judgment, and the reliability work. These are the competencies this project is meant to
build, roughly in order:

1. **Serving** — async APIs, streaming responses (SSE), request/response models, error paths,
   timeouts, retries, and backoff. Making an LLM feel like a normal, boring web service.
2. **Prompting as engineering** — treat prompts as versioned, reviewable code. Structure,
   few-shot examples, and explicit output contracts rather than folklore.
3. **Structured output** — constrain generations to Pydantic/JSON schemas so downstream code
   never has to string-parse a paragraph.
4. **Tool use / agents** — function calling, giving a model a small set of well-documented
   tools, and managing the loop, budgets, and stopping conditions.
5. **Retrieval (RAG)** — chunking, embeddings, vector search, and honest evaluation of whether
   retrieval actually helped.
6. **Evaluation** — golden datasets, assertion-based checks, regression tests, and LLM-as-judge
   used skeptically. This is the part most tutorials skip and the part that matters most.
7. **Observability & cost** — logs, traces, token accounting, latency percentiles, and prompt
   caching.
8. **Deployment** — containers, environment/config separation, secrets, rate limiting, and
   guardrails on inputs and outputs.

## Conventions I'm keeping

- `uv` only — no `pip install` into a loose global environment, and commit `uv.lock`.
- Pydantic models at every boundary; no untyped `dict` passing between layers.
- Small, self-contained experiments per topic rather than one giant app.
- Anything worth keeping gets a test, including prompt/eval harnesses.

## Ideas for what to build in it

Some candidates I'm considering as the practice vehicle once the API layer is solid:

- A tour-guide endpoint that answers questions about a city from a retrieved knowledge base.
- An itinerary generator that takes structured constraints (days, budget, mobility, interests)
  and emits a typed, validated plan.
- A "compare two approaches" agent that calls tools and writes a cited summary.
- An offline eval runner that scores any of the above against a small hand-labeled dataset.

## Status

Scaffold only. No commits yet, no tests, no model integration.

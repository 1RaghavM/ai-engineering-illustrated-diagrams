# AI Engineering Illustrated: Diagrams

**Visual explanations of how modern AI systems actually work: sandboxes, MCP, inference serving, agents and more.**

These are the diagrams from [AI Engineering Illustrated](https://ragmehta.substack.com), a newsletter of illustrated deep dives into AI engineering. Every diagram links to its full article.

👉 **Subscribe for new deep dives: [ragmehta.substack.com](https://ragmehta.substack.com)**

## Table of Contents

- [001 · How Code Sandboxes for AI Agents Work](#001-how-code-sandboxes-for-ai-agents-work)
- [002 · How the Model Context Protocol (MCP) Works](#002-how-the-model-context-protocol-mcp-works)
- [003 · How LLM Inference Serving Works: KV Cache, PagedAttention and Continuous Batching](#003-how-llm-inference-serving-works-kv-cache-pagedattention-and-continuous-batching)
- [004 · How Computer-Use Agents Work](#004-how-computer-use-agents-work)
- [005 · Anatomy of an Agent Harness: Loop, Tools, Memory and Subagents](#005-anatomy-of-an-agent-harness-loop-tools-memory-and-subagents)
- [006 · Why Can't LLMs Count the R's in "Strawberry"? How Tokenizers Work](#006-why-cant-llms-count-the-rs-in-strawberry-how-tokenizers-work)
- [007 · How Cursor Got Thousands of AI Agents to Build One Browser](#007-how-cursor-got-thousands-of-ai-agents-to-build-one-browser)

## 001 How Code Sandboxes for AI Agents Work

### How an AI agent runs code in a sandbox

<p align="center"><img src="images/code-sandboxes/sandbox-sequence.png" alt="How an AI agent runs code in a sandbox" width="720"></p>

How an agent runs code: the sandbox is created, the code runs, and the sandbox is destroyed, all on the untrusted side.

📖 [Read the full deep dive →](https://ragmehta.substack.com/p/how-code-sandboxes-for-ai-agents)

### Where the isolation boundary sits

<p align="center"><img src="images/code-sandboxes/isolation-boundaries.png" alt="Where the isolation boundary sits" width="720"></p>

Four isolation technologies and the wall an attacker must break in each.

📖 [Read the full deep dive →](https://ragmehta.substack.com/p/how-code-sandboxes-for-ai-agents)

### Following one open() call

<p align="center"><img src="images/code-sandboxes/syscall-path.png" alt="Following one open() call" width="720"></p>

One open() call through gVisor and through a Firecracker microVM.

📖 [Read the full deep dive →](https://ragmehta.substack.com/p/how-code-sandboxes-for-ai-agents)

### How network egress is controlled

<p align="center"><img src="images/code-sandboxes/network-egress.png" alt="How network egress is controlled" width="720"></p>

Deny-by-default egress: only allowlisted destinations get out.

📖 [Read the full deep dive →](https://ragmehta.substack.com/p/how-code-sandboxes-for-ai-agents)

### Snapshot and restore for fast starts

<p align="center"><img src="images/code-sandboxes/snapshot-restore.png" alt="Snapshot and restore for fast starts" width="720"></p>

Boot once, snapshot, then restore every new sandbox in milliseconds.

📖 [Read the full deep dive →](https://ragmehta.substack.com/p/how-code-sandboxes-for-ai-agents)

### Sandbox design trade-offs

<p align="center"><img src="images/code-sandboxes/table-tradeoffs.png" alt="Sandbox design trade-offs" width="720"></p>

Sandbox design trade-offs: sensible defaults and when to upgrade.

📖 [Read the full deep dive →](https://ragmehta.substack.com/p/how-code-sandboxes-for-ai-agents)


## 002 How the Model Context Protocol (MCP) Works

### MCP architecture

<p align="center"><img src="images/model-context-protocol/mcp-architecture.png" alt="MCP architecture" width="720"></p>

Host, clients and servers: one client per server, and the host keeps the conversation.

📖 [Read the full deep dive →](https://ragmehta.substack.com/p/how-the-model-context-protocol-mcp)

### The MCP primitives

<p align="center"><img src="images/model-context-protocol/mcp-primitives.png" alt="The MCP primitives" width="720"></p>

Server features (tools, resources, prompts) and client features (sampling, elicitation, roots).

📖 [Read the full deep dive →](https://ragmehta.substack.com/p/how-the-model-context-protocol-mcp)

### Anatomy of an MCP tool call

<p align="center"><img src="images/model-context-protocol/mcp-tool-call.png" alt="Anatomy of an MCP tool call" width="720"></p>

A tool call end to end, including an input-required round trip.

📖 [Read the full deep dive →](https://ragmehta.substack.com/p/how-the-model-context-protocol-mcp)

### MCP transports

<p align="center"><img src="images/model-context-protocol/mcp-transports.png" alt="MCP transports" width="720"></p>

stdio for local servers, Streamable HTTP for remote ones.

📖 [Read the full deep dive →](https://ragmehta.substack.com/p/how-the-model-context-protocol-mcp)

### How remote MCP authorization works

<p align="center"><img src="images/model-context-protocol/mcp-authorization.png" alt="How remote MCP authorization works" width="720"></p>

How a remote MCP server sends a client to sign in and checks its token.

📖 [Read the full deep dive →](https://ragmehta.substack.com/p/how-the-model-context-protocol-mcp)


## 003 How LLM Inference Serving Works: KV Cache, PagedAttention and Continuous Batching

### Prefill vs decode

<p align="center"><img src="images/llm-inference-serving/prefill-decode.png" alt="Prefill vs decode" width="720"></p>

Prefill processes the prompt in parallel; decode produces one token per step.

📖 [Read the full deep dive →](https://ragmehta.substack.com/p/how-llm-inference-serving-works-kv)

### How big is the KV cache?

<p align="center"><img src="images/llm-inference-serving/kv-cache-size.png" alt="How big is the KV cache?" width="720"></p>

KV cache size for Llama 3.1 8B: 128 KiB per token.

📖 [Read the full deep dive →](https://ragmehta.substack.com/p/how-llm-inference-serving-works-kv)

### How PagedAttention works

<p align="center"><img src="images/llm-inference-serving/paged-attention.png" alt="How PagedAttention works" width="720"></p>

PagedAttention: fixed-size blocks mapped by a block table, like virtual memory.

📖 [Read the full deep dive →](https://ragmehta.substack.com/p/how-llm-inference-serving-works-kv)

### Static vs continuous batching

<p align="center"><img src="images/llm-inference-serving/continuous-batching.png" alt="Static vs continuous batching" width="720"></p>

Static batching waits for the longest request; continuous batching re-forms the batch every step.

📖 [Read the full deep dive →](https://ragmehta.substack.com/p/how-llm-inference-serving-works-kv)

### Prefix caching and chunked prefill

<p align="center"><img src="images/llm-inference-serving/prefix-chunked.png" alt="Prefix caching and chunked prefill" width="720"></p>

Prefix caching reuses shared KV blocks; chunked prefill schedules decodes first.

📖 [Read the full deep dive →](https://ragmehta.substack.com/p/how-llm-inference-serving-works-kv)


## 004 How Computer-Use Agents Work

### The computer-use agent loop

<p align="center"><img src="images/computer-use-agents/cua-loop.png" alt="The computer-use agent loop" width="720"></p>

The computer-use loop: the model sends actions, your code runs them in the VM and sends back screenshots.

📖 [Read the full deep dive →](https://ragmehta.substack.com/p/how-computer-use-agents-work)

### Coordinate scaling

<p align="center"><img src="images/computer-use-agents/coordinate-scaling.png" alt="Coordinate scaling" width="720"></p>

Screenshots are downscaled for the model, so its clicks must be scaled back up.

📖 [Read the full deep dive →](https://ragmehta.substack.com/p/how-computer-use-agents-work)

### Two ways to drive a computer

<p align="center"><img src="images/computer-use-agents/integration-styles.png" alt="Two ways to drive a computer" width="720"></p>

Structured actions vs code execution.

📖 [Read the full deep dive →](https://ragmehta.substack.com/p/how-computer-use-agents-work)

### Inside a computer-use environment

<p align="center"><img src="images/computer-use-agents/cua-environment.png" alt="Inside a computer-use environment" width="720"></p>

Layers of Anthropic's reference computer-use environment.

📖 [Read the full deep dive →](https://ragmehta.substack.com/p/how-computer-use-agents-work)

### Defense in depth for computer-use agents

<p align="center"><img src="images/computer-use-agents/cua-safety.png" alt="Defense in depth for computer-use agents" width="720"></p>

Five layers of defense for computer-use agents.

📖 [Read the full deep dive →](https://ragmehta.substack.com/p/how-computer-use-agents-work)


## 005 Anatomy of an Agent Harness: Loop, Tools, Memory and Subagents

### The five subsystems of an agent harness

<p align="center"><img src="images/agent-harness/harness-anatomy.png" alt="The five subsystems of an agent harness" width="720"></p>

Agent = Model + Harness: the six subsystems around the model.

📖 [Read the full deep dive →](https://ragmehta.substack.com/p/anatomy-of-an-agent-harness-loop)

### The agent loop: model asks, harness acts

<p align="center"><img src="images/agent-harness/agent-loop.png" alt="The agent loop: model asks, harness acts" width="720"></p>

The agent loop: the model asks, the harness checks and acts, until end_turn.

📖 [Read the full deep dive →](https://ragmehta.substack.com/p/anatomy-of-an-agent-harness-loop)

### How a harness assembles context each turn

<p align="center"><img src="images/agent-harness/context-assembly.png" alt="How a harness assembles context each turn" width="720"></p>

What goes into each model call, and what the harness does as context grows.

📖 [Read the full deep dive →](https://ragmehta.substack.com/p/anatomy-of-an-agent-harness-loop)

### Subagent patterns: handoffs vs agents-as-tools

<p align="center"><img src="images/agent-harness/subagent-patterns.png" alt="Subagent patterns: handoffs vs agents-as-tools" width="720"></p>

Agents-as-tools vs handoffs: who writes the final reply.

📖 [Read the full deep dive →](https://ragmehta.substack.com/p/anatomy-of-an-agent-harness-loop)

### Harness design trade-offs

<p align="center"><img src="images/agent-harness/table-tradeoffs.png" alt="Harness design trade-offs" width="720"></p>

Harness design trade-offs: what to start with and what to add when needed.

📖 [Read the full deep dive →](https://ragmehta.substack.com/p/anatomy-of-an-agent-harness-loop)


## 006 Why Can't LLMs Count the R's in "Strawberry"? How Tokenizers Work

### From raw text to token IDs

<p align="center"><img src="images/tokenizers/text-to-tokens.png" alt="From raw text to token IDs" width="720"></p>

From raw text to token IDs: pre-split, apply BPE merges, look up IDs, then embed.

📖 [Read the full deep dive →](https://ragmehta.substack.com/p/why-cant-llms-count-the-rs-in-strawberry)

### How BPE learns its vocabulary

<p align="center"><img src="images/tokenizers/bpe-training.png" alt="How BPE learns its vocabulary" width="720"></p>

BPE training: count adjacent pairs, merge the most frequent, repeat until the vocabulary is full.

📖 [Read the full deep dive →](https://ragmehta.substack.com/p/why-cant-llms-count-the-rs-in-strawberry)

### Why strawberry hides its r's

<p align="center"><img src="images/tokenizers/strawberry.png" alt="Why strawberry hides its r's" width="720"></p>

The model sees a leading-space strawberry as one ID with no letters inside; spelling it out or calling code exposes the letters.

📖 [Read the full deep dive →](https://ragmehta.substack.com/p/why-cant-llms-count-the-rs-in-strawberry)

### The token tax across languages and numbers

<p align="center"><img src="images/tokenizers/token-tax.png" alt="The token tax across languages and numbers" width="720"></p>

The token tax: the same sentence costs more tokens in some languages, and numbers split into left-aligned chunks.

📖 [Read the full deep dive →](https://ragmehta.substack.com/p/why-cant-llms-count-the-rs-in-strawberry)

### Tokenizer gotchas and fixes

<p align="center"><img src="images/tokenizers/table-gotchas.png" alt="Tokenizer gotchas and fixes" width="720"></p>

Common tokenizer gotchas, their causes and practical fixes.

📖 [Read the full deep dive →](https://ragmehta.substack.com/p/why-cant-llms-count-the-rs-in-strawberry)


## 007 How Cursor Got Thousands of AI Agents to Build One Browser

### Four harness designs Cursor tried

<p align="center"><img src="images/cursor-multi-agent/four-designs.png" alt="Four harness designs Cursor tried" width="720"></p>

Cursor tried four harness designs. Flat peers with a lock file, a planner-executor-judge pipeline and a single continuous executor all stalled. A tree of planners, workers and handoffs scaled to about 1,000 commits an hour.

📖 [Read the full deep dive →](https://ragmehta.substack.com/p/how-cursor-got-thousands-of-ai-agents)

### Tree of planners, workers and handoffs

<p align="center"><img src="images/cursor-multi-agent/agent-tree.png" alt="Tree of planners, workers and handoffs" width="720"></p>

The final design: a root planner that writes no code, recursive subplanners that each own a slice, and workers on their own repo copies that push to one shared branch and send handoffs back up.

📖 [Read the full deep dive →](https://ragmehta.substack.com/p/how-cursor-got-thousands-of-ai-agents)

### Throughput over perfection

<p align="center"><img src="images/cursor-multi-agent/throughput.png" alt="Throughput over perfection" width="720"></p>

Requiring every commit to be green serialized the whole system. Accepting a small, stable error rate plus a final fix-up pass kept hundreds of agents moving. (The error chart is illustrative.)

📖 [Read the full deep dive →](https://ragmehta.substack.com/p/how-cursor-got-thousands-of-ai-agents)

### One machine became the bottleneck

<p align="center"><img src="images/cursor-multi-agent/one-machine.png" alt="One machine became the bottleneck" width="720"></p>

Each run had one large VM with about 300 agents. Once agent RAM was capped, disk I/O from builds and shared git and Cargo locks became the bottlenecks. Specs, screenshots and the Rust compiler kept agents on track.

📖 [Read the full deep dive →](https://ragmehta.substack.com/p/how-cursor-got-thousands-of-ai-agents)

### How five multi-agent systems coordinate

<p align="center"><img src="images/cursor-multi-agent/table-designs.png" alt="How five multi-agent systems coordinate" width="720"></p>

How five multi-agent systems from Cursor and Anthropic coordinate, how big they got and how they check work.

📖 [Read the full deep dive →](https://ragmehta.substack.com/p/how-cursor-got-thousands-of-ai-agents)

## License

Diagrams © Raghav Mehta, licensed [CC BY-NC 4.0](LICENSE). You can share and adapt them for non-commercial use with attribution and a link to [ragmehta.substack.com](https://ragmehta.substack.com).

## Contributing

Found an error? See [CONTRIBUTING.md](CONTRIBUTING.md).

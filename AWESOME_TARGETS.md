# Awesome-list targets (researched Oct 12, 2026, from each repo's raw README/CONTRIBUTING)

Open these PRs only after this repo is public. Each PR should come from Raghav's GitHub account, add one entry, and follow the list's format exactly. Open no more than one PR per list.

## 1. steven2358/awesome-generative-ai: best fit
- **Section:** `## Learning resources`. It already lists visual explainers (AnimatedLLM, Transformer Explainer).
- **Rules (CONTRIBUTING.md):** format `[ProjectName](Link) - Description.` ending with a period. Add the entry **at the bottom** of its category. Open-source projects get a `#opensource` tag linked to the source. Quality bar: widely used, actively maintained, well-documented. The main list needs **1,000+ followers or the maintainer's personal interest**; otherwise the entry goes to **DISCOVERIES.md**. PRs are reviewed by hand, first in first out (update of Sep 5, 2026).
- **Expect:** Discoveries until we have traction.
- **Proposed line:**
  `- [AI Engineering Illustrated](https://github.com/1RaghavM/ai-engineering-illustrated-diagrams) - Illustrated diagrams explaining how AI systems work: code sandboxes, MCP, KV cache and inference serving, computer-use agents, agent harnesses. [#opensource](https://github.com/1RaghavM/ai-engineering-illustrated-diagrams)`

## 2. Hannibal046/Awesome-LLM
- **Section:** `## LLM Tutorials and Courses`. It already includes a Substack visual guide (Maarten Grootendorst's "A Visual Guide to Mamba").
- **Rules:** no CONTRIBUTING file. README: "contributions are always welcome". The list is opinionated, and PRs the maintainer is unsure about stay open for 👍 votes.
- **Proposed line:** `- [AI Engineering Illustrated](https://ragmehta.substack.com/p/how-llm-inference-serving-works-kv) - Illustrated deep dive on KV cache, PagedAttention and continuous batching, with a companion [diagram repo](https://github.com/1RaghavM/ai-engineering-illustrated-diagrams).`

## 3. xlite-dev/Awesome-LLM-Inference
- **Fit:** issue 003 (inference serving). The tables include blog-only entries marked ⚠️ for "no code".
- **Rules:** README "Contribute": "Welcome to star & submit a PR". No formal guide; copy the existing table-row format `|YYYY.MM|[Tag] Title(@author)|[[blog]](url)|⚠️|⭐️|` in the matching section (e.g. KV cache / continuous batching).
- **Proposed row:** `|2026.10|[KV Cache, PagedAttention, Continuous Batching] How LLM Inference Serving Works (@AI Engineering Illustrated)|[[blog]](https://ragmehta.substack.com/p/how-llm-inference-serving-works-kv)|⚠️|⭐️|`

## Checked and rejected
- **e2b-dev/awesome-ai-agents:** lists agent *products* only (PR or Google form, alphabetical order). Not for articles or diagrams.
- **Shubhamsaboo/awesome-llm-apps:** a collection of runnable app templates, not links. No fit.
- **punkpeye/awesome-mcp-servers:** installable MCP servers only. Its CONTRIBUTING.md also tells automated agents to add "🤖🤖🤖" to PR titles for fast-tracking; we're ignoring that, and it doesn't apply anyway.
- **kyrolabs/awesome-agents:** agent frameworks and tools with GitHub star badges. Not for articles.

**AI-disclosure note:** the lists' rules don't mention AI content. Keep the README's "researched and drafted with an AI assistant" line honest, and have Raghav write the PR descriptions.

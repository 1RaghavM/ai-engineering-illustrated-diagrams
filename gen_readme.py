import re, sys, os
src = sys.argv[1] if len(sys.argv) > 1 else "/workspace/newsletter"
ISSUES = [
 ("001","code-sandboxes","How Code Sandboxes for AI Agents Work","https://ragmehta.substack.com/p/how-code-sandboxes-for-ai-agents"),
 ("002","model-context-protocol","How the Model Context Protocol (MCP) Works","https://ragmehta.substack.com/p/how-the-model-context-protocol-mcp"),
 ("003","llm-inference-serving","How LLM Inference Serving Works: KV Cache, PagedAttention and Continuous Batching","https://ragmehta.substack.com/p/how-llm-inference-serving-works-kv"),
 ("004","computer-use-agents","How Computer-Use Agents Work","https://ragmehta.substack.com/p/how-computer-use-agents-work"),
 ("005","agent-harness","Anatomy of an Agent Harness: Loop, Tools, Memory and Subagents","https://ragmehta.substack.com/p/anatomy-of-an-agent-harness-loop"),
 ("006","tokenizers","Why Can't LLMs Count the R's in \"Strawberry\"? How Tokenizers Work","https://ragmehta.substack.com/p/why-cant-llms-count-the-rs-in-strawberry"),
 ("007","cursor-multi-agent","How Cursor Got Thousands of AI Agents to Build One Browser","https://ragmehta.substack.com/p/how-cursor-got-thousands-of-ai-agents"),
 ("008","vector-indexes","HNSW vs IVF vs PQ: How Vector Indexes Trade Memory, Speed and Recall","https://ragmehta.substack.com/p/hnsw-vs-ivf-vs-pq-how-vector-indexes"),
]
man = open(os.path.join(src,"redraw-manifest.md")).read()
caps = {}

EXTRA = {
 ("006","text-to-tokens"): ("From raw text to token IDs", "From raw text to token IDs: pre-split, apply BPE merges, look up IDs, then embed."),
 ("006","bpe-training"): ("How BPE learns its vocabulary", "BPE training: count adjacent pairs, merge the most frequent, repeat until the vocabulary is full."),
 ("006","strawberry"): ("Why strawberry hides its r's", "The model sees a leading-space strawberry as one ID with no letters inside; spelling it out or calling code exposes the letters."),
 ("006","token-tax"): ("The token tax across languages and numbers", "The token tax: the same sentence costs more tokens in some languages, and numbers split into left-aligned chunks."),
 ("006","table-gotchas"): ("Tokenizer gotchas and fixes", "Common tokenizer gotchas, their causes and practical fixes."),
 ("007","four-designs"): ("Four harness designs Cursor tried", "Cursor tried four harness designs. Flat peers with a lock file, a planner-executor-judge pipeline and a single continuous executor all stalled. A tree of planners, workers and handoffs scaled to about 1,000 commits an hour."),
 ("007","agent-tree"): ("Tree of planners, workers and handoffs", "The final design: a root planner that writes no code, recursive subplanners that each own a slice, and workers on their own repo copies that push to one shared branch and send handoffs back up."),
 ("007","throughput"): ("Throughput over perfection", "Requiring every commit to be green serialized the whole system. Accepting a small, stable error rate plus a final fix-up pass kept hundreds of agents moving. (The error chart is illustrative.)"),
 ("007","one-machine"): ("One machine became the bottleneck", "Each run had one large VM with about 300 agents. Once agent RAM was capped, disk I/O from builds and shared git and Cargo locks became the bottlenecks. Specs, screenshots and the Rust compiler kept agents on track."),
 ("007","table-designs"): ("How five multi-agent systems coordinate", "How five multi-agent systems from Cursor and Anthropic coordinate, how big they got and how they check work."),
 ("008","three-families"): ("Three families of vector indexes", "Three ways to avoid brute-force search: navigate a graph (HNSW), narrow the search to a few partitions (IVF), or shrink every vector (PQ). Real indexes usually combine two of them."),
 ("008","hnsw"): ("How HNSW search works", "HNSW enters at a sparse top layer, hops greedily toward the query, drops a layer at a time, and widens its candidate list (ef_search) at the bottom layer, which holds every vector."),
 ("008","ivf"): ("How IVF partitions the space", "IVF uses k-means to split the space into cells and scans only the nprobe nearest lists. A true neighbor just across a cell boundary is missed unless you probe more cells."),
 ("008","pq"): ("How product quantization compresses vectors", "Product quantization splits a 768-dimension vector into 96 chunks and stores one byte per chunk: 3,072 bytes become 96. Distances become table lookups, so top hits are reranked with full vectors."),
 ("008","table-tradeoffs"): ("Vector index trade-offs", "How flat, HNSW, IVF-Flat, IVF-PQ/RaBitQ and DiskANN compare on memory, build time, query speed and updates."),
 ("008","which-index"): ("Which vector index to pick", "A quick decision guide: flat for small jobs, HNSW when RAM is plentiful, IVF with compression or DiskANN when it isn't. On Postgres, pgvector HNSW is the stable default; PRISM is alpha."),
}

for m in re.finditer(r"issue-(\d{3})/([\w-]+)-final\.png`\. Replaces `[^`]+` \(old alt/caption: \"([^\"]+)\"\)\. New caption: \*([^*]+)\*", man):
    n, f, title, cap = m.groups()
    caps[(n, re.sub(r"^fig\d+-","",f))] = (title, cap)
caps.update(EXTRA)
def anchor(t): return re.sub(r"[^a-z0-9 -]","",t.lower()).replace(" ","-")
out = ["# AI Engineering Illustrated: Diagrams","",
"**Visual explanations of how modern AI systems actually work: sandboxes, MCP, inference serving, agents and more.**","",
"These are the diagrams from [AI Engineering Illustrated](https://ragmehta.substack.com), a newsletter of illustrated deep dives into AI engineering. Every diagram links to its full article.","",
"👉 **Subscribe for new deep dives: [ragmehta.substack.com](https://ragmehta.substack.com)**","",
"## Table of Contents",""]
body = []
for n,slug,title,url in ISSUES:
    out.append(f"- [{n} · {title}](#{anchor(n+' '+title)})")
    body += ["",f"## {n} {title}",""]
    d = f"images/{slug}"
    files = sorted(os.listdir(d)) if os.path.isdir(d) else []
    order = [k[1] for k in caps if k[0]==n]
    files.sort(key=lambda x: order.index(x[:-4]) if x[:-4] in order else 99)
    for f in files:
        t, c = caps.get((n,f[:-4]), (f[:-4].replace("-"," ").title(), ""))
        body += [f"### {t}","",f'<p align="center"><img src="{d}/{f}" alt="{t}" width="720"></p>',"",c,"",f"📖 [Read the full deep dive →]({url})",""]
out += body + ["## License","","Diagrams © Raghav Mehta, licensed [CC BY-NC 4.0](LICENSE). You can share and adapt them for non-commercial use with attribution and a link to [ragmehta.substack.com](https://ragmehta.substack.com).","",
"## Contributing","","Found an error? See [CONTRIBUTING.md](CONTRIBUTING.md).",""]
open("README.md","w").write("\n".join(out))
print("README.md written,", len(caps), "captions found")

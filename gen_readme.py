import re, sys, os
src = sys.argv[1] if len(sys.argv) > 1 else "/workspace/newsletter"
ISSUES = [
 ("001","code-sandboxes","How Code Sandboxes for AI Agents Work","https://ragmehta.substack.com/p/how-code-sandboxes-for-ai-agents"),
 ("002","model-context-protocol","How the Model Context Protocol (MCP) Works","https://ragmehta.substack.com/p/how-the-model-context-protocol-mcp"),
 ("003","llm-inference-serving","How LLM Inference Serving Works: KV Cache, PagedAttention and Continuous Batching","https://ragmehta.substack.com/p/how-llm-inference-serving-works-kv"),
 ("004","computer-use-agents","How Computer-Use Agents Work","https://ragmehta.substack.com/p/how-computer-use-agents-work"),
 ("005","agent-harness","Anatomy of an Agent Harness: Loop, Tools, Memory and Subagents","https://ragmehta.substack.com/p/anatomy-of-an-agent-harness-loop-tools-memory-and-subagents"),
]
man = open(os.path.join(src,"redraw-manifest.md")).read()
caps = {}
for m in re.finditer(r"issue-(\d{3})/([\w-]+)-final\.png`\. Replaces `[^`]+` \(old alt/caption: \"([^\"]+)\"\)\. New caption: \*([^*]+)\*", man):
    n, f, title, cap = m.groups()
    caps[(n, re.sub(r"^fig\d+-","",f))] = (title, cap)
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

# 🛡️ Neural Sentinel AI Security Scan

Automated CI/CD security and EU AI Act compliance scanning for AI Agent workflows (CrewAI, LangGraph, AutoGen). 

[![Socket Badge](https://socket.dev/api/badge/pypi/package/agentsentinel-crewai)](https://socket.dev/pypi/package/agentsentinel-crewai)
[![PyPI Downloads](https://static.pepy.tech/badge/agentsentinel-crewai)](https://pepy.tech/project/agentsentinel-crewai)

## Why use this action?
- **Zero False Negatives**: Powered by our proprietary Semantic Normalization Engine.
- **EU AI Act Mapped**: Automatically flags violations of Article 15 (Technical Robustness).
- **Enterprise Trusted**: 3,900+ PyPI downloads and a perfect 100/100 Supply Chain Security score on Socket.dev.

## Usage

Create a test script in your repo (e.g., `tests/test_security.py`):
```python
from crewai import Agent, Task, Crew
from agentsentinel_crewai import scan_crew, SecurityAudit

# Build your crew
researcher = Agent(role="Researcher", goal="Research", backstory="Expert")
crew = Crew(agents=[researcher], tasks=[])

# Run the scan and fail the CI pipeline if CRITICAL issues are found
SecurityAudit(crew, block_on="CRITICAL").scan()

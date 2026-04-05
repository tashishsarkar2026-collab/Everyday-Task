You are an expert enterprise solution architect.

Create a modern, clean, and professional architecture diagram for an "Agentic AI Platform (MVP-3)" designed for enterprise use.

### Context:
This platform is NOT a single application. It is a reusable backend platform that enables rapid development of multiple AI use cases (e.g., underwriting, fraud detection, claims processing) using shared components.

The architecture must clearly show how the system is modular, reusable, and scalable.

---

### Requirements:

#### 1. High-Level Layers (must be visually separated)

1. Client Layer
   - Underwriter UI / Web App
   - External Systems / APIs

2. API Layer
   - FastAPI Gateway
   - Authentication (Azure AD / IAM)

3. Agent Layer (Core Brain)
   - LLM-based Agent
   - Orchestration Logic
   - Decision Engine

4. Core Platform Modules (very important section)
   Show these as independent reusable components:
   - Tool Registry (dynamic tool calling)
   - RAG Module (document ingestion + retrieval)
   - LLM Abstraction Layer (multi-model support)
   - Configuration Layer (use-case configs: prompts, tools, workflows)

5. Data & Integration Layer
   - External APIs (policy system, claims DB, fraud services)
   - Vector Database (for embeddings)
   - Blob Storage / Document Storage

6. Governance & Observability Layer (cross-cutting)
   - Logging & Monitoring
   - Audit Trail
   - Security / Content Filtering
   - Error Handling / Retry

---

#### 2. Flow (must be shown with arrows)

Show this flow clearly:

User → API → Agent → (Tools / RAG / LLM) → Data Sources → Response

Also show:
- Agent calling Tool Registry
- RAG fetching from Vector DB
- LLM abstraction routing to models

---

#### 3. Reusability Highlight (VERY IMPORTANT)

Add a side section or annotation:

"Same Platform, Different Use Cases"

Examples:
- Underwriting → uses Tool A, B
- Fraud Detection → uses Tool C, D
- Claims Processing → uses Tool E, F

Show that only configuration changes, not architecture.

---

#### 4. Style Guidelines

- Use a clean, modern cloud architecture style (similar to Azure/AWS diagrams)
- Use icons or labeled boxes for each component
- Group components into clearly defined layers
- Use directional arrows for data flow
- Keep it visually balanced (not cluttered)

---

#### 5. Output Format

- Provide diagram in a format that can be recreated in draw.io / diagrams.net
- If possible, also include a structured representation (like Mermaid or XML)

---

### Goal:

The diagram should make it immediately clear that:
- This is a PLATFORM, not a single application
- Components are reusable and configurable
- New AI use cases can be built quickly without rewriting the system

Avoid generic diagrams. Make it specific, structured, and enterprise-ready.
You are an expert enterprise cloud architect specializing in secure AI platforms.

Create a modern, clean, enterprise-grade architecture diagram for:

"Security & Governance Architecture – Agentic AI Platform (MVP-3)"

---

### CONTEXT

This is NOT a generic security diagram.

This is specifically for an **Agentic AI Platform** that includes:
- LLM-based agents
- Tool calling (MCP-style)
- RAG pipelines
- Enterprise API integrations

The diagram must reflect **real enterprise-grade Azure architecture**.

---

### STRUCTURE (MANDATORY LAYOUT)

Organize the diagram into clearly separated sections:

---

## 1. LEFT PANEL: Governance & Compliance (vertical section)

Include:
- Responsible AI (Explainability, Transparency)
- Data Governance (Microsoft Purview)
- Compliance Tracking (ISO, SOC2)
- Policy Enforcement (Azure Policy)

---

## 2. TOP LAYER: Identity & Access Management (IAM)

Include:
- Azure Active Directory (Azure AD)
- Authentication & Authorization
- Role-Based Access Control (RBAC)
- Managed Identities (for service-to-service communication)

Actors:
- Underwriters
- Admins
- Applications / Services

---

## 3. NETWORK SECURITY LAYER

Include:
- Azure Virtual Network (VNet)
- Subnets
- Network Security Groups (NSG)
- Azure Firewall
- Private Endpoints / Private Link

Show secure internal communication between components

---

## 4. APPLICATION & API SECURITY

Include:
- FastAPI Secure Backend (API Gateway)
- OAuth2 / Token-based Authentication
- Input Validation
- Request Filtering
- RBAC enforcement at API level

---

## 5. AI & LLM SECURITY (IMPORTANT)

Include:
- Azure OpenAI Service
- Prompt Validation & Sanitization
- Output Filtering / Safety Controls
- PII Protection / Data Leakage Prevention

Show secure interaction between:
Agent → LLM → Response

---

## 6. TOOL / MCP SECURITY LAYER (VERY IMPORTANT FOR MVP-3)

Include:
- Secure Tool Connectors
- API Key Management
- Managed Identity for tool access
- Controlled tool invocation

Label this clearly:
"MCP / Tool Access Security"

---

## 7. DATA SECURITY LAYER

Include:
- Azure SQL / Cosmos DB
- Blob Storage
- Vector Database (for embeddings)

Security features:
- Encryption at Rest
- Encryption in Transit (HTTPS/TLS)
- Access Control (ACLs)
- Data Isolation

---

## 8. MONITORING & AUDIT (RIGHT PANEL – vertical)

Include:
- Azure Monitor
- Application Insights
- Logging (API calls, tool usage, AI decisions)
- Full Audit Trail

---

## 9. CORE PLATFORM (CENTER FLOW)

Show secure flow:

User → API → Agent → Tools / RAG / LLM → Data

Ensure arrows show:
- Authentication flow
- Secure data movement
- Controlled access between layers

---

### DESIGN REQUIREMENTS

- Use a clean Azure-style architecture layout
- Group components into boxes with clear labels
- Use directional arrows for flow
- Highlight cross-cutting concerns (security, logging)
- Keep it visually balanced and not cluttered

---

### OUTPUT FORMAT

- Provide diagram suitable for draw.io / diagrams.net
- Prefer structured output (Mermaid or XML if possible)

---

### GOAL

The diagram should clearly demonstrate:
- End-to-end security across an AI platform
- Governance + compliance integration
- Secure tool calling (key MVP-3 differentiator)
- Enterprise-grade monitoring and auditability

Avoid generic cloud diagrams. Make it specific to agentic AI systems.
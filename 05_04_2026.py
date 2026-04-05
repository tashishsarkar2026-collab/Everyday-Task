Create an enterprise-grade Security & Governance architecture diagram for an AI-driven system on Azure, improving a basic linear diagram into a layered, modern cloud architecture.

Objective:

Transform a simple vertical security flow into a structured, multi-layered enterprise architecture similar to modern Azure reference diagrams.

---

Key Requirements:

- Use Azure-native services only
- Show layered architecture (not linear boxes)
- Group related security controls logically
- Include clear visual sections (left, center, right)
- Maintain clarity while increasing depth

---

🧱 Structure of Diagram

---

LEFT PANEL: Governance & Compliance

- Responsible AI (Explainability, Transparency)
- Data Governance (Microsoft Purview)
- Compliance (ISO, SOC)
- Azure Policy Enforcement

---

TOP LAYER: Identity & Access Management

- Azure Active Directory (Azure AD)
- Authentication & Authorization
- RBAC (Role-Based Access Control)
- Managed Identity (service-to-service)

Include:

- Users: Underwriters, Admins

---

NETWORK & INFRASTRUCTURE LAYER

- Azure Virtual Network (VNet)
- Subnets
- Azure Firewall
- Network Security Groups (NSGs)
- Private Endpoints / Private Link

---

APPLICATION SECURITY LAYER

- Secure FastAPI Backend
- Token-based Authentication (OAuth/JWT)
- RBAC enforcement at API layer
- Input validation & request filtering

---

MCP / TOOL ACCESS SECURITY (IMPORTANT)

- Secure connectors to multiple data sources
- API Key / Managed Identity authentication
- Controlled tool invocation
- Least privilege access
- Secure API gateway / connector layer

---

AI & LLM SECURITY

- Azure OpenAI (secure access)
- Prompt validation & sanitization
- Output filtering & safety controls
- PII masking / data protection

---

DATA SECURITY LAYER

- Encryption at rest (Blob, SQL, Cosmos DB)
- Encryption in transit (HTTPS/TLS)
- Access control (ACLs)
- Data isolation

---

RIGHT PANEL: MONITORING & AUDIT

- Azure Monitor
- Application Insights
- Logging:
  - User actions
  - AI decisions
  - Tool calls
- Full audit trail

---

🎯 Style Requirements

- Replace vertical boxes with layered architecture
- Use icons where possible
- Group components in horizontal sections
- Keep text minimal but meaningful
- Ensure readability and balance
- Avoid clutter but include all key layers

---

Output:

A modern, enterprise-grade Azure security architecture diagram with clear layers and structured grouping, similar to high-quality consulting presentations.

---
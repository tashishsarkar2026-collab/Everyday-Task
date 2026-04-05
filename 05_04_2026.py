Create a clean, enterprise-grade security and governance architecture diagram for an AI-powered underwriting system built on Azure.

Objective:

The diagram should clearly represent layered security, governance, and compliance controls across the system. It should be visually clean, structured, and suitable for executive presentation.

---

Key Requirements:

- Use Azure-native services only
- Show security as a layered or cross-cutting framework
- Keep the diagram structured and not cluttered
- Clearly label each security layer
- Use icons where possible (Azure AD, Monitor, etc.)

---

🧱 Security Layers to Include

---

1. Identity & Access Management

- Azure Active Directory (AAD)
- Role-Based Access Control (RBAC)
- User authentication & authorization
- Managed Identity for service-to-service access

---

2. API & Application Security

- Secure FastAPI endpoints
- Token-based authentication (OAuth/JWT)
- RBAC validation at API layer
- Input validation and request filtering

---

3. Data Security

- Encryption at rest (Blob, SQL, Cosmos DB)
- Encryption in transit (HTTPS/TLS)
- Secure storage access controls
- Data isolation and protection

---

4. MCP / Tool Access Security

- Secure connectors to internal and external systems
- Managed Identity / API keys for tool access
- Controlled and auditable tool invocation
- Least-privilege access to data sources

---

5. AI / LLM Security

- Secure access to Azure OpenAI
- Prompt validation and input sanitization
- Output filtering and safety controls
- Prevention of data leakage

---

6. Monitoring & Audit

- Azure Monitor
- Application Insights
- Logging of:
  - User actions
  - AI decisions
  - Tool calls
- Full audit trail and traceability

---

7. Governance & Compliance

- Policy enforcement
- Data access governance
- Compliance tracking
- Responsible AI practices (explainability, transparency)

---

🔄 Diagram Structure

- Show system layers in center:
  (UI → Backend → AI → Tool Layer → Data Sources → Storage)

- Overlay or surround with security layers:
  
  - Identity (top)
  - Data (bottom)
  - Monitoring (side)
  - Governance (cross-cutting)

---

🎯 Style Requirements

- Clean, layered diagram
- No clutter or excessive text
- Clear labels for each security layer
- Enterprise look (not cartoonish)
- Easy to understand in under 30 seconds

---

Output:

A visually structured security and governance architecture diagram showing layered protection across the entire system.

---
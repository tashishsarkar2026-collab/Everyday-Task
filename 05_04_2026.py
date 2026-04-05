You are an expert enterprise cloud architect and visual diagram designer.

Create a detailed, visually rich, PowerPoint-style architecture diagram for:

"Security & Governance Architecture – Agentic AI Platform (MVP-3)"

IMPORTANT:
- DO NOT generate code (no Mermaid, no XML, no scripts)
- DO NOT provide text explanation only
- Generate a VISUAL ARCHITECTURE DIAGRAM (like a PPT or Azure architecture diagram)
- Use labeled boxes, sections, and icons (if possible)
- The output should look like something that can be directly recreated in PowerPoint or draw.io

---

### CONTEXT

This is an enterprise-grade Agentic AI Platform built on Azure.

The diagram must clearly show how security, governance, and monitoring are enforced across all layers of the platform.

---

### STRUCTURE (MANDATORY LAYOUT)

Design the diagram in horizontal layers and vertical governance sections.

---

### 1. LEFT VERTICAL SECTION (Governance & Compliance)

Create a vertical block on the left titled:

"Governance & Compliance"

Include:
- Responsible AI (Explainability, Transparency)
- Data Governance (Microsoft Purview)
- Compliance Tracking (ISO, SOC)
- Policy Enforcement (Azure Policy)

---

### 2. TOP LAYER: IDENTITY & ACCESS MANAGEMENT (IAM)

Include:
- Users:
  - Underwriters
  - Admins
- Azure Active Directory (Azure AD)
- Authentication & Authorization
- Role-Based Access Control (RBAC)
- Managed Identity (for service-to-service access)

---

### 3. NETWORK SECURITY LAYER

Include:
- Azure Virtual Network (VNet)
- Subnets
- Azure Firewall
- Network Security Groups (NSGs)
- Private Endpoints / Private Link

Show secure connectivity between services.

---

### 4. APPLICATION & API SECURITY

Include:
- Secure FastAPI Backend
- OAuth/JWT Token-based Authentication
- Input Validation
- Request Filtering
- RBAC enforcement

---

### 5. AGENT & AI SECURITY (VERY IMPORTANT FOR MVP-3)

Include:
- AI Orchestration Layer (Agent)
- Prompt Validation & Sanitization
- Output Filtering
- PII/Data Leakage Prevention
- Secure access to Azure OpenAI

---

### 6. TOOL / MCP SECURITY LAYER

Include:
- Secure Tool Connectors
- API Key Management
- Managed Identity for tools
- Controlled access to external APIs

---

### 7. DATA SECURITY LAYER

Include:
- Azure SQL / Cosmos DB
- Blob Storage
- Vector Database

Show:
- Encryption in transit (HTTPS/TLS)
- Encryption at rest
- Access control (ACLs)
- Data isolation

---

### 8. RIGHT VERTICAL SECTION (Monitoring & Audit)

Create a vertical block on the right titled:

"Monitoring & Audit"

Include:
- Azure Monitor
- Application Insights
- Logging (user actions, tool calls, AI decisions)
- Alerts & Metrics
- Full Audit Trail

---

### 9. CROSS-LAYER ELEMENT (IMPORTANT)

Across the middle or bottom, include:

"Azure Infrastructure"

Show that all components are deployed within Azure secure environment.

---

### 10. FLOW INDICATIONS

Use arrows to show:
- User → API → Agent → Tools → Data
- Security checks at each stage
- Monitoring capturing all actions

---

### 11. STYLE REQUIREMENTS

- Use clean enterprise layout (like Azure reference architecture diagrams)
- Use boxes with headings for each section
- Use icons where possible (user, database, shield, cloud)
- Clearly separate layers
- Avoid clutter, keep it structured and readable

---

### GOAL

The diagram should clearly communicate:

- End-to-end security across the platform
- Governance embedded at every layer
- Enterprise-grade compliance and monitoring
- Secure AI and tool usage in an Agentic system

---

Again:
DO NOT generate code.
DO NOT generate Mermaid.
Create a visual architecture diagram representation only.